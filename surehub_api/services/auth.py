import requests
from cachetools import TTLCache

from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.utils import response_handler

DEFAULT_HEADERS = {
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
        auth_login = official.AuthLogin(
            device_id="web",
            email_address=settings.email,
            password=settings.password,
        )

        response = requests.post(
            f"{settings.endpoint}/api/auth/login",
            json=auth_login.model_dump(mode='json'),
            headers=DEFAULT_HEADERS
        )
        auth_token = response_handler.parse(response, model=official.AuthToken)

        token = auth_token.token
        cache["token"] = token

    return token
