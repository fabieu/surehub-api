from datetime import datetime, timezone
from typing import List

import requests
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from surehub_api.config import settings
from surehub_api.entities import official, dto, official_v2
from surehub_api.services import auth, devices
from surehub_api.utils import http_utils


def get_pets() -> List[official.Pet]:
    uri = f"{settings.endpoint}/api/pet"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def get_pet(pet_id: int) -> official.Pet:
    uri = f"{settings.endpoint}/api/pet/{pet_id}"

    response = requests.get(uri, headers=auth.auth_headers())
    return http_utils.extract_response_data(response)


def get_pet_status(pet_id: int) -> dto.PetStatusResponse:
    pet = official.Pet.model_validate(get_pet(pet_id))

    # TODO: Fetch information about indoor mode
    indoor_only = None

    return dto.PetStatusResponse(
        position=pet.position,
        feeding=pet.status.feeding if pet.status else None,
        drinking=pet.status.drinking if pet.status else None,
        indoor_only=indoor_only
    )


def update_pet_status(pet_id: int, payload: dto.UpdatePetStatusRequest) -> dto.PetStatusResponse:
    if payload.position:
        _update_pet_position(pet_id, payload.position)

    if payload.indoor_only is not None:
        _update_indoor_mode(pet_id, payload.indoor_only, payload.household_ids)

    return get_pet_status(pet_id)


def _update_pet_position(pet_id: int, position: official.PetPositionWhere):
    uri = f"{settings.endpoint}/api/pet/{pet_id}/position"

    payload = official.CreatePetPosition(
        where=position,
        since=datetime.now(timezone.utc)
    )

    response = requests.post(uri, headers=auth.auth_headers(), json=payload.model_dump(mode='json'))
    http_utils.raise_for_status(response)


def _update_indoor_mode(pet_id: int, indoor_only: bool, household_ids: list[int] = None):
    pet = official.Pet.model_validate(get_pet(pet_id))

    if not pet.tag or not pet.tag.supported_product_ids:
        return

    all_devices = [official.Device.model_validate(device) for device in
                   devices.get_devices(household_ids=household_ids)]
    supported_devices = [device for device in all_devices if device.product_id in pet.tag.supported_product_ids]

    for device in supported_devices:
        uri = f"{settings.endpoint}/api/v2/device/{device.id}/tag/async"

        payload = official_v2.UpdateDeviceTag(
            tag_id=pet.tag.id,
            request_action=official_v2.DeviceTagAction.ACTION_0,
            profile=official_v2.DeviceTagProfile.ENABLED if indoor_only else official_v2.DeviceTagProfile.DISABLED,
        )

        response = requests.put(uri, headers=auth.auth_headers(), json=[payload.model_dump(mode='json')])
        http_utils.raise_for_status(response)


def get_pet_position(pet_id: int) -> official.PetPosition:
    pet = get_pet(pet_id)
    pet_position = pet.get('position')

    if not pet_position:
        raise HTTPException(status_code=500, detail=f"Invalid position '{pet_position}' for pet_id {pet_id}")

    return pet_position


def get_pet_positions() -> List[official.PetPosition]:
    pet_positions = []

    for pet in get_pets():
        pet_position = pet.get('position')

        if not pet_position:
            raise HTTPException(status_code=500, detail=f"Invalid position '{pet_position}' for pet_id {pet.get('id')}")

        pet_positions.append(pet_position)

    return pet_positions


def set_pet_position(pet_id: int, pet_position: official.CreatePetPosition) -> official.PetPosition:
    uri = f"{settings.endpoint}/api/pet/{pet_id}/position"

    pet_position_dict = jsonable_encoder(pet_position)

    if not pet_position_dict['since']:
        pet_position_dict['since'] = datetime.now(timezone.utc).isoformat()

    response = requests.post(uri, headers=auth.auth_headers(), json=pet_position_dict)
    return http_utils.extract_response_data(response)
