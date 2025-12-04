from typing import List

from fastapi import APIRouter

from surehub_api.entities import surehub
from surehub_api.entities.openapi import Tags
from surehub_api.services import pets

router = APIRouter(
    prefix="/pets",
    tags=[Tags.PET],
)


@router.get("/",
            response_model_exclude_none=True)
async def get_all_pets() -> List[surehub.Pet]:
    return pets.get_pets()


@router.get("/pets/position",
            response_model_exclude_none=True)
async def get_all_pets_positions() -> List[surehub.PetPosition]:
    return pets.get_pet_positions()


@router.get("/pets/{pet_id}",
            response_model_exclude_none=True)
def get_pet(pet_id: int) -> surehub.Pet:
    return pets.get_pet(pet_id)


@router.get("/pets/{pet_id}/position",
            response_model_exclude_none=True)
async def get_pet_position(pet_id: int) -> surehub.PetPosition:
    return pets.get_pet_position(pet_id)


@router.post("/pets/{pet_id}/position",
             response_model_exclude_none=True,
             description="""
          Parameter `where`: **1** = Inside, **2** = Outside
          """)
async def set_pet_position(pet_id: int, payload: surehub.CreatePetPosition) -> surehub.PetPosition:
    return pets.set_pet_position(pet_id, payload)
