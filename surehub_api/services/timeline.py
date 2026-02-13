import math

import requests

from surehub_api.config import settings
from surehub_api.services import auth
from surehub_api.utils import http_utils


def get_timeline_of_household(household_id: int) -> list:
    uri = f"{settings.endpoint}/api/timeline/household/{household_id}"

    result = []
    fetch_size = 100

    response = requests.get(uri, headers=auth.auth_headers())
    meta = http_utils.extract_response_data(response, key='meta')
    count = meta['count']
    page_size = meta['page_size']

    request_count = math.ceil(count / page_size)

    for i in range(1, request_count + 1):
        payload = {'page_size': fetch_size, 'page': i}
        response2 = requests.get(uri, headers=auth.auth_headers(), params=payload)
        result += http_utils.extract_response_data(response2)

    return result
