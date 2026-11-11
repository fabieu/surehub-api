import random
import re
import threading
import time
from datetime import datetime, timedelta, timezone
from logging import ERROR, INFO, getLogger
from typing import Any

import jwt
import requests
from fastapi import HTTPException
from pydantic import TypeAdapter, ValidationError
from uvicorn.logging import AccessFormatter

from surehub_api.config import settings
from surehub_api.entities import official

logger = getLogger(__name__)

_DEFAULT_HEADERS = {
    "Accept": "application/json, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en-GB;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://surehub.io",
    "Referer": "https://surehub.io",
}

_lock = threading.Lock()
_cached_token: str = ""
_token_expiry: datetime = datetime.min.replace(tzinfo=timezone.utc)

_LOGIN_RETRIES = 3
_LOGIN_BACKOFF_BASE = 1.0  # seconds; doubled each retry: 1s, 2s
_REQUEST_TIMEOUT = 10  # seconds
_TOKEN_EXPIRY_MARGIN = timedelta(seconds=60)  # Refresh token 60s before actual expiry

# URLs whose response body must not be logged, e.g. because it contains credentials
BODY_LOG_EXCLUDED_URLS = {
    re.compile(r"/api/auth/login$"),
}


def _build_headers(token: str) -> dict[str, str]:
    return _DEFAULT_HEADERS | {"Authorization": f"Bearer {token}"}


def request(method: str, url: str, **kwargs) -> requests.Response:
    original_headers = kwargs.pop("headers", {})

    response = requests.request(
        method=method,
        url=url,
        headers=_build_headers(_get_token()) | original_headers,
        timeout=_REQUEST_TIMEOUT,
        **kwargs
    )

    # Token was rotated upstream — evict, re-auth, retry once
    if response.status_code == 401:
        response = requests.request(
            method=method,
            url=url,
            headers=_build_headers(_get_token(force_refresh=True)) | original_headers,
            timeout=_REQUEST_TIMEOUT,
            **kwargs
        )

    return response


def get(url: str, **kwargs) -> requests.Response:
    return request("GET", url, **kwargs)


def post(url: str, **kwargs) -> requests.Response:
    return request("POST", url, **kwargs)


def put(url: str, **kwargs) -> requests.Response:
    return request("PUT", url, **kwargs)


def delete(url: str, **kwargs) -> requests.Response:
    return request("DELETE", url, **kwargs)


def _get_token(force_refresh: bool = False) -> str:
    global _cached_token, _token_expiry

    with _lock:
        if force_refresh or not _cached_token or datetime.now(timezone.utc) >= _token_expiry:
            try:
                token = _login()
            except (requests.exceptions.RequestException, RuntimeError) as exc:
                raise HTTPException(status_code=502, detail=str(exc)) from exc

            _token_expiry = _parse_expiry(token)
            _cached_token = token
            return token

        return _cached_token


def _parse_expiry(token: str) -> datetime:
    try:
        payload = jwt.decode(token, options={"verify_signature": False})  # NOSONAR(S5659)
        return datetime.fromtimestamp(payload["exp"], tz=timezone.utc) - _TOKEN_EXPIRY_MARGIN
    except (jwt.exceptions.DecodeError, KeyError) as exc:
        raise HTTPException(status_code=502, detail=f"Invalid token from upstream: {exc}") from exc


def _login() -> str:
    auth_login = official.AuthLogin(
        device_id="web",
        email_address=settings.email,
        password=settings.password,
    )

    for attempt in range(_LOGIN_RETRIES):
        if attempt > 0:
            backoff = _LOGIN_BACKOFF_BASE * (2 ** (attempt - 1))
            time.sleep(backoff + random.uniform(0, backoff))
        try:
            response = requests.post(
                f"{settings.endpoint}/api/auth/login",
                json=auth_login.model_dump(mode='json'),
                headers=_DEFAULT_HEADERS,
                timeout=_REQUEST_TIMEOUT,
            )

            # Retry on 5xx; on the final attempt let parse raise
            if response.status_code >= 500 and attempt < _LOGIN_RETRIES - 1:
                continue

            auth_token = parse(response, model=official.AuthToken)
            return auth_token.token
        except requests.exceptions.RequestException as exc:
            if attempt == _LOGIN_RETRIES - 1:
                raise requests.exceptions.RequestException(
                    f"Upstream auth unavailable after {_LOGIN_RETRIES} attempts: {exc}"
                ) from exc


def log_response(response: requests.Response) -> None:
    method = response.request.method
    url = response.request.url
    status_code = response.status_code
    reason = response.reason
    http_version = response.raw.version_string

    if 200 <= status_code < 300 or 400 <= status_code < 600:
        # Colored like uvicorn's access log: bold request line, status colored by its class
        status_color = AccessFormatter.status_code_colours[status_code // 100]
        color_message = '"\033[1m%s %s %s\033[0m" ' + status_color("%s %s")
        logger.log(
            INFO if status_code < 300 else ERROR,
            '"%s %s %s" %s %s',
            method,
            url,
            http_version,
            status_code,
            reason,
            extra={"color_message": color_message},
        )

    if url and not any(pattern.search(url) for pattern in BODY_LOG_EXCLUDED_URLS):
        logger.debug("Response body: %s", response.text)


def raise_for_status(response: requests.Response) -> None:
    """Raise FastAPI HTTPException if response indicates an error.

    :param response: requests.Response object
    :raise HTTPException: If status code indicates client or server error
    """
    log_response(response)

    if not response.ok:
        raise HTTPException(status_code=response.status_code, detail=_extract_error_detail(response))


def parse(response: requests.Response, key: str = "data", model: Any | None = None) -> Any:
    """
    Validates an HTTP response and raises HTTPException on errors.

    - Raises HTTPException if status code is 4xx or 5xx
    - Preserves original status code from upstream service
    - Extracts error details from response body when available

    :param response: requests.Response object
    :param key: root level key to extract payload (default: "data")
    :param model: Pydantic model class to validate the extracted payload against (optional)
    :raise HTTPException: If status code indicates client or server error
    """

    raise_for_status(response)

    try:
        payload = response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Response is not valid JSON")

    if key not in payload:
        raise HTTPException(status_code=500, detail=f"Invalid response format: missing '{key}'")

    data = payload[key]

    if model is None:
        return data

    try:
        return TypeAdapter(model).validate_python(data)
    except ValidationError as ex:
        raise HTTPException(status_code=500, detail=f"Invalid response format: {ex.errors()}")


def _extract_error_detail(response) -> str | dict:
    try:
        return response.json()
    except ValueError:
        return response.text.replace('"', "'")
