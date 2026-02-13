from logging import getLogger
from typing import Any

from fastapi import HTTPException
from pydantic import TypeAdapter, ValidationError
from requests import Response

logger = getLogger(__name__)


def raise_for_status(response: Response) -> None:
    """Raise FastAPI HTTPException if response indicates an error.

    :param response: requests.Response object
    :raise HTTPException: If status code indicates client or server error
    """
    _log_request(response)

    if not response.ok:
        raise HTTPException(status_code=response.status_code, detail=_extract_error_detail(response))


def parse(response: Response, key: str = "data", model: Any | None = None) -> Any:
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


def _log_request(response: Response) -> None:
    method = response.request.method
    url = response.request.url
    status_code = response.status_code

    if 200 <= status_code < 300:
        logger.info("External API request %s %s returned %s", method, url, status_code)
    elif 400 <= status_code < 600:
        logger.error("External API request %s %s returned %s", method, url, status_code)
