from datetime import datetime, timezone
from typing import List

import requests
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from surehub_api.config import settings
from surehub_api.entities import official, dto, official_v2
from surehub_api.services import auth, devices
from surehub_api.utils import response_handler


def get_pets() -> List[official.Pet]:
    uri = f"{settings.endpoint}/api/pet"

    response = requests.get(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=List[official.Pet])


def get_pet(pet_id: int) -> official.Pet:
    uri = f"{settings.endpoint}/api/pet/{pet_id}"

    response = requests.get(uri, headers=auth.auth_headers())
    return response_handler.parse(response, model=official.Pet)


def get_pet_state(pet_id: int) -> dto.PetStateResponse:
    pet = get_pet(pet_id)

    return dto.PetStateResponse(
        position=pet.position,
        feeding=pet.status.feeding if pet.status else None,
        drinking=pet.status.drinking if pet.status else None,
    )


def update_pet_state(
        pet_id: int,
        payload: dto.UpdatePetStateRequest,
        household_ids: List[int] | None = None
) -> None:
    if payload.position is not None:
        _update_pet_position(pet_id, payload.position)

    if payload.indoor_only is not None:
        _update_indoor_only_mode(pet_id, payload.indoor_only, household_ids)


def _update_pet_position(pet_id: int, position: official.PetPositionWhere) -> None:
    uri = f"{settings.endpoint}/api/pet/{pet_id}/position"

    payload = official.CreatePetPosition(
        where=position,
        since=datetime.now(timezone.utc)
    )

    response = requests.post(uri, headers=auth.auth_headers(), json=payload.model_dump(mode='json'))
    response_handler.raise_for_status(response)


def _update_indoor_only_mode(pet_id: int, indoor_only: bool, household_ids: List[int] | None = None) -> None:
    pet = get_pet(pet_id)

    if not pet.tag_id:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to update indoor mode, because pet with id {pet_id} has no associated tag"
        )

    supported_devices = [device for device in devices.get_devices(household_ids=household_ids)
                         if device.get("product_id") in devices.DEVICE_TYPES_SUPPORTING_INDOOR_ONLY_MODE]

    if not supported_devices:
        raise HTTPException(
            status_code=422,
            detail=f"Failed to update indoor mode for pet id {pet_id}, because no devices supporting indoor-only mode were found",
        )

    request_action = official_v2.UpdateDeviceTagActions.VALUE_0
    profile = official_v2.DeviceTagProfiles.ENABLED if indoor_only else official_v2.DeviceTagProfiles.DISABLED

    for device in supported_devices:
        uri = f"{settings.endpoint}/api/v2/device/{device.id}/tag/async"

        payload = official_v2.UpdateDeviceTag(
            tag_id=pet.tag_id,
            request_action=request_action,
            profile=profile,
        )

        response = requests.put(uri, headers=auth.auth_headers(), json=[payload.model_dump(mode='json')])
        response_handler.raise_for_status(response)


def get_pet_position(pet_id: int) -> official.PetPosition:
    pet = get_pet(pet_id)
    pet_position = pet.position

    if not pet_position:
        raise HTTPException(status_code=500, detail=f"Invalid position '{pet_position}' for pet_id {pet_id}")

    return pet_position


def get_pet_positions() -> List[official.PetPosition]:
    pet_positions = []

    for pet in get_pets():
        pet_position = pet.position

        if not pet_position:
            raise HTTPException(status_code=500, detail=f"Invalid position '{pet_position}' for pet_id {pet.id}")

        pet_positions.append(pet_position)

    return pet_positions


def set_pet_position(pet_id: int, pet_position: official.CreatePetPosition) -> official.PetPosition:
    uri = f"{settings.endpoint}/api/pet/{pet_id}/position"

    pet_position_dict = jsonable_encoder(pet_position)

    if not pet_position_dict['since']:
        pet_position_dict['since'] = datetime.now(timezone.utc).isoformat()

    response = requests.post(uri, headers=auth.auth_headers(), json=pet_position_dict)
    return response_handler.parse(response, model=official.PetPosition)
