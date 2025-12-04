import requests
from cachetools import TTLCache
from fastapi import HTTPException

from surehub_api.config import settings

DEFAULT_HEADERS = {
    "Host": "app-api.production.surehub.io",
    "Accept": "application/json, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en-GB;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://surehub.io",
    "Referer": "https://surehub.io",
}

cache = TTLCache(maxsize=128, ttl=86400)


def auth_headers() -> dict[str, str]:
    return DEFAULT_HEADERS | {
        "Authorization": f"Bearer {_get_token()}",
    }


def _get_token() -> str:
    token = cache.get("token")

    if not token:
        payload = {
            "email_address": settings.email,
            "password": settings.password,
            "device_id": "web",
        }
        response = requests.post(f"{settings.endpoint}/api/auth/login", json=payload, headers=DEFAULT_HEADERS)

        if response.ok:
            token = response.json()["data"]["token"]
            cache["token"] = token
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))

    return token
