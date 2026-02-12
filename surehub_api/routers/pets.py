from typing import List, Annotated

from fastapi import APIRouter, Query

from surehub_api.entities import official, dto
from surehub_api.entities.openapi import Tags
from surehub_api.services import pets

router = APIRouter(
    prefix="/pets",
    tags=[Tags.PET],
)


@router.get("/",
            response_model_exclude_none=True)
async def get_all_pets() -> List[official.Pet]:
    return pets.get_pets()


@router.get("/position",
            response_model_exclude_none=True,
            deprecated=True)
async def get_all_pets_positions() -> List[official.PetPosition]:
    return pets.get_pet_positions()


@router.get("/{pet_id}",
            response_model_exclude_none=True)
async def get_pet(pet_id: int) -> official.Pet:
    return pets.get_pet(pet_id)


@router.get("/{pet_id}/status",
            response_model_exclude_none=True)
async def get_pet_status(pet_id: int) -> dto.PetStatusResponse:
    return pets.get_pet_status(pet_id)


@router.patch("/{pet_id}/status",
              response_model_exclude_none=True,
              description="""
              `position`: INSIDE = 1, OUTSIDE = 2
              """
              )
async def update_pet_status(
        pet_id: int,
        payload: dto.UpdatePetStatusRequest,
        household_ids: Annotated[List[int], Query(
            alias="householdIds",
            description="Limit status update to specific household ids")
        ] = None
) -> None:
    return pets.update_pet_status(pet_id, payload, household_ids)


@router.get("/{pet_id}/position",
            response_model_exclude_none=True,
            deprecated=True)
async def get_pet_position(pet_id: int) -> official.PetPosition:
    return pets.get_pet_position(pet_id)


@router.post("/{pet_id}/position",
             response_model_exclude_none=True,
             deprecated=True,
             description="""
          Parameter `where`: **1** = Inside, **2** = Outside
          """)
async def set_pet_position(pet_id: int, payload: official.CreatePetPosition) -> official.PetPosition:
    return pets.set_pet_position(pet_id, payload)
