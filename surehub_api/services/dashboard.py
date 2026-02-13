import requests

from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.services import auth
from surehub_api.utils import http_utils


def get_dashboard() -> official.MeStart:
    uri = f"{settings.endpoint}/api/me/start"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response, model=official.MeStart)
