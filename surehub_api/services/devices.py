import json
from typing import List

import requests
from fastapi import HTTPException

from surehub_api.config import settings
from surehub_api.entities import official, custom
from surehub_api.services import auth


def get_devices() -> List[official.Device]:
    uri = f"{settings.endpoint}/api/device"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_devices_by_id(device_id: int) -> official.Device:
    uri = f"{settings.endpoint}/api/device/{device_id}"

    payload = {'with[]': ['children', 'status', 'control']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def set_lock_mode(device_id: int, lock_mode: custom.LockMode) -> official.DeviceControl:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    data = {
        "locking": lock_mode.mode_id
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_tags_of_device(device_id: int) -> List[official.Tag]:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_tag_of_device(device_id: int, tag_id: int) -> official.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def assign_tag_to_device(device_id: int, tag_id: int) -> official.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    data = {
        "profile": official.SpecialProfile.SPECIAL_PROFILE_0  # It is currently not known what this is for
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def remove_tag_from_device(device_id: int, tag_id: int) -> official.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    response = requests.delete(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
