from typing import List, Annotated

from fastapi import APIRouter, Query

from surehub_api.entities import official, custom
from surehub_api.entities.openapi import Tags
from surehub_api.services import devices

router = APIRouter(
    prefix="/devices",
    tags=[Tags.DEVICE],
)


@router.get("/",
            response_model_exclude_none=True)
async def get_devices() -> List[official.Device]:
    return devices.get_devices()


@router.get("/{device_id}",
            response_model_exclude_none=True)
async def get_device_by_id(device_id: int) -> official.Device:
    return devices.get_devices_by_id(device_id)


@router.patch("/{device_id}/control",
              response_model_exclude_none=True)
async def set_device_lock_mode(device_id: int, lock_mode: Annotated[custom.LockMode, Query(
    description="**none** = Pets can enter and leave the house \n\n"
                "**out** = Pets can leave the house but can no longer enter it \n\n"
                "**in** = Pets can enter the house but can no longer leave it \n\n"
                "**both** = Pets can no longer enter and leave the house \n\n")
]) -> official.DeviceControl:
    return devices.set_lock_mode(device_id, lock_mode)


@router.get("/{device_id}/tags",
            response_model_exclude_none=True)
def get_tags_of_device(device_id: int) -> List[official.Tag]:
    return devices.get_tags_of_device(device_id)


@router.get("/{device_id}/tags/{tag_id}",
            response_model_exclude_none=True)
def get_tag_of_device(device_id: int, tag_id: int) -> official.Tag:
    return devices.get_tag_of_device(device_id, tag_id)


@router.put("/{device_id}/tags/{tag_id}",
            response_model_exclude_none=True)
def assign_tag_to_device(device_id: int, tag_id: int) -> official.Tag:
    return devices.assign_tag_to_device(device_id, tag_id)


@router.delete('/{device_id}/tags/{tag_id}',
               response_model_exclude_none=True)
def remove_tag_from_device(device_id: int, tag_id: int) -> official.Tag:
    return devices.remove_tag_from_device(device_id, tag_id)
