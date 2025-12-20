from datetime import datetime

import requests

from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.services import auth
from surehub_api.utils import http_utils


def get_pet_report(household_id: int, pet_id: int, from_datetime: datetime,
                   to_datetime: datetime) -> official.PetReport:
    uri = f"{settings.endpoint}/api/v2/report/household/{household_id}/pet/{pet_id}/aggregate"

    params = {
        "From": from_datetime.isoformat(),
        "To": to_datetime.isoformat()
    }

    response = requests.get(uri, headers=auth.auth_headers(), params=params)
    return http_utils.extract_response_data(response)
