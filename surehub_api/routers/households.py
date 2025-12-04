from typing import List

from fastapi import APIRouter

from surehub_api.entities import surehub
from surehub_api.entities.openapi import Tags
from surehub_api.services import households

router = APIRouter(
    prefix="/households",
    tags=[Tags.HOUSEHOLD],
)


@router.get("/",
            response_model_exclude_none=True)
async def get_households() -> List[surehub.Household]:
    return households.get_households()


@router.get("/{household_id}",
            response_model_exclude_none=True)
async def get_household_by_id(household_id: int) -> surehub.Household:
    return households.get_household_by_id(household_id)


@router.get("/{household_id}/users",
            response_model_exclude_none=True)
async def get_users_of_household(household_id: int) -> List[surehub.HouseholdUser]:
    return households.get_users_of_household(household_id)


@router.get("/{household_id}/users/{user_id}",
            response_model_exclude_none=True)
async def get_user(household_id: int, user_id: int) -> surehub.HouseholdUser:
    return households.get_user_of_household(household_id, user_id)


@router.get("/{household_id}/pets",
            response_model_exclude_none=True)
async def get_pets_of_household(household_id: int) -> List[surehub.Pet]:
    return households.get_pets_of_household(household_id)


@router.get("/{household_id}/pets/{pet_id}",
            response_model_exclude_none=True)
async def get_pet_of_household(household_id: int, pet_id: int) -> surehub.Pet:
    return households.get_pet_of_household(household_id, pet_id)


@router.get("/{household_id}/devices",
            response_model_exclude_none=True)
async def get_devices_of_household(household_id: int) -> List[surehub.Device]:
    return households.get_devices_of_household(household_id)


@router.get("/{household_id}/devices/{device_id}",
            response_model_exclude_none=True)
async def get_device_of_household(household_id: int, device_id: int) -> surehub.Device:
    return households.get_device_of_household(household_id, device_id)
