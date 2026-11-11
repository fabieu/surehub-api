from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.services import api


def get_dashboard() -> official.MeStart:
    uri = f"{settings.endpoint}/api/me/start"

    response = api.get(uri)
    return api.parse(response, model=official.MeStart)
