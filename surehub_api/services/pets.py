from datetime import datetime, timezone
from typing import List

from fastapi import HTTPException

from surehub_api.config import settings
from surehub_api.entities import official, dto, official_v2
from surehub_api.services import api, devices
from surehub_api.utils import response_handler


def get_pets() -> List[official.Pet]:
    uri = f"{settings.endpoint}/api/pet"

    response = api.get(uri)
    return response_handler.parse(response, model=List[official.Pet])


def get_pet(pet_id: int) -> official.Pet:
    uri = f"{settings.endpoint}/api/pet/{pet_id}"

    response = api.get(uri)
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

    response = api.post(uri, json=payload.model_dump(mode='json'))
    response_handler.raise_for_status(response)


def _update_indoor_only_mode(pet_id: int, indoor_only: bool, household_ids: List[int] | None = None) -> None:
    pet = get_pet(pet_id)

    if not pet.tag_id:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to update indoor mode, because pet with id {pet_id} has no associated tag"
        )

    supported_devices = [device for device in devices.get_devices(household_ids=household_ids)
                         if device.product_id in devices.DEVICE_TYPES_SUPPORTING_INDOOR_ONLY_MODE]

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

        response = api.put(uri, json=[payload.model_dump(mode='json')])
        response_handler.raise_for_status(response)
