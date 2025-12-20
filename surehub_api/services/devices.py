from typing import List, Any

import requests

from surehub_api.config import settings
from surehub_api.entities import official, custom
from surehub_api.services import auth
from surehub_api.utils import http_utils


def get_devices() -> List[official.Device]:
    uri = f"{settings.endpoint}/api/device"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def get_device_by_id(device_id: int) -> official.Device:
    uri = f"{settings.endpoint}/api/device/{device_id}"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def get_device_state_by_id(device_id) -> Any:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def set_lock_mode(device_id: int, lock_mode: custom.LockMode) -> official.DeviceControl:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    data = {
        "locking": lock_mode.mode_id
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)
    return http_utils.extract_response_data(response)


def get_tags_of_device(device_id: int) -> List[official.Tag]:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def get_tag_of_device(device_id: int, tag_id: int) -> official.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def assign_tag_to_device(device_id: int, tag_id: int) -> official.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    data = {
        "profile": official.SpecialProfile.SPECIAL_PROFILE_0  # It is currently not known what this is for
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)
    return http_utils.extract_response_data(response)


def remove_tag_from_device(device_id: int, tag_id: int) -> official.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    response = requests.delete(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)
