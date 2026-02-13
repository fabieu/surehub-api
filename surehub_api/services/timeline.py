import math

import requests
from fastapi import HTTPException

from surehub_api.config import settings
from surehub_api.services import auth
from surehub_api.utils import response_handler


def get_timeline_of_household(household_id: int) -> list:
    uri = f"{settings.endpoint}/api/timeline/household/{household_id}"

    result = []
    fetch_size = 100

    response = requests.get(uri, headers=auth.auth_headers())
    meta = response_handler.parse(response, key='meta')
    count = meta.get('count')
    page_size = meta.get('page_size')

    if count is None or page_size in (None, 0):
        raise HTTPException(status_code=500, detail="Invalid response format: missing timeline meta fields")

    request_count = math.ceil(count / page_size)

    for i in range(1, request_count + 1):
        payload = {'page_size': fetch_size, 'page': i}
        response2 = requests.get(uri, headers=auth.auth_headers(), params=payload)
        result += response_handler.parse(response2)

    return result
