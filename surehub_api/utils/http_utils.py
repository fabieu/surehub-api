from typing import Any

from fastapi import HTTPException
from requests import Response


def raise_for_status(response: Response) -> None:
    """Raise FastAPI HTTPException if response indicates an error.

    :param response: requests.Response object
    :raise HTTPException: If status code indicates client or server error
    """
    if not response.ok:
        raise HTTPException(status_code=response.status_code, detail=_extract_error_detail(response))


def extract_response_data(response: Response, key: str = "data") -> Any:
    """
    Validates an HTTP response and raises HTTPException on errors.

    - Raises HTTPException if status code is 4xx or 5xx
    - Preserves original status code from upstream service
    - Extracts error details from response body when available

    :param response: requests.Response object
    :param key: root level key to extract payload
    :raise HTTPException: If status code indicates client or server error
    """

    raise_for_status(response)

    try:
        payload = response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Response is not valid JSON")

    if key not in payload:
        raise HTTPException(status_code=500, detail=f"Invalid response format: missing '{key}'")

    return payload[key]


def _extract_error_detail(response) -> str | dict:
    try:
        return response.json()
    except ValueError:
        return response.text.replace('"', "'")
