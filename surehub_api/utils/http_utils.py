from typing import Any

from fastapi import HTTPException


def extract_response_data(
        response,
        key: str = "data",
) -> Any:
    """
    Validates an HTTP response and extracts a payload.

    - Raises HTTPException on non-2xx responses
    - Parses JSON safely
    - Validates presence of expected key
    """

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=_extract_error_detail(response),
        )

    try:
        payload = response.json()
    except ValueError:
        raise HTTPException(
            status_code=500,
            detail="Response is not valid JSON",
        )

    if key not in payload:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid response format: missing '{key}'",
        )

    return payload[key]


def _extract_error_detail(response) -> str | dict:
    try:
        return response.json()
    except ValueError:
        return response.text.replace('"', "'")
