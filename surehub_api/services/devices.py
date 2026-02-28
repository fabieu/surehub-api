from typing import List

import requests

from surehub_api.config import settings
from surehub_api.entities import official, custom
from surehub_api.services import auth
from surehub_api.utils import response_handler

DEVICE_TYPES_SUPPORTING_INDOOR_ONLY_MODE = [
    official.DeviceType.DUALSCAN_PET_DOOR_CONNECT,
    official.DeviceType.DUALSCAN_CAT_FLAP_CONNECT,
    official.DeviceType.CAT_FLAP_CONNECT
]


def get_devices(
        household_ids: List[int] | None = None,
) -> List[official.Device]:
    uri = f"{settings.endpoint}/api/device"

    params = {}

    if household_ids:
        params["HouseholdId"] = household_ids

    response = requests.get(uri, headers=auth.auth_headers(), params=params)
    return response_handler.parse(response, model=List[official.Device])


def get_device_by_id(device_id: int) -> official.Device:
    uri = f"{settings.endpoint}/api/device/{device_id}"

    response = requests.get(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=official.Device)


def get_device_state_by_id(device_id) -> official.DeviceControl:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    response = requests.get(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=official.DeviceControl)


def set_lock_mode(device_id: int, lock_mode: custom.LockMode) -> official.DeviceControl:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    data = {
        "locking": lock_mode.mode_id
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)
    return response_handler.parse(response, model=official.DeviceControl)


def get_tags_of_device(device_id: int) -> List[official.DeviceTag]:
    uri = f"{settings.endpoint}/api/device/{device_id}/tag"

    response = requests.get(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=List[official.Tag])

def update_device_state(device_id: int, device_state: official.DeviceControl) -> official.DeviceControl:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    response = requests.put(uri, headers=auth.auth_headers(), json=device_state.model_dump(mode='json'))
    return http_utils.extract_response_data(response)


def get_tag_of_device(device_id: int, tag_id: int) -> official.DeviceTag:
    uri = f"{settings.endpoint}/api/device/{device_id}/tag/{tag_id}"

    response = requests.get(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=official.Tag)


def assign_tag_to_device(device_id: int, tag_id: int) -> official.DeviceTag:
    uri = f"{settings.endpoint}/api/device/{device_id}/tag/{tag_id}"

    data = {
        "profile": official.SpecialProfiles.SPECIAL_PROFILE_0  # It is currently not known what this is for
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)
    return response_handler.parse(response, model=official.Tag)


def remove_tag_from_device(device_id: int, tag_id: int) -> official.DeviceTag:
    uri = f"{settings.endpoint}/api/device/{device_id}/tag/{tag_id}"

    response = requests.delete(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=official.Tag)
