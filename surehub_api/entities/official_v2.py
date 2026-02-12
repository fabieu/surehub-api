from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


# TODO: Add descriptive names to device tag actions
class DeviceTagAction(IntEnum):
    ACTION_0 = 0
    ACTION_1 = 1
    ACTION_2 = 2


class DeviceTagProfile(IntEnum):
    DISABLED = 2
    ENABLED = 3


class ThalamusMovementTimedAccessAllowedSpecialProfile(IntEnum):
    SPECIAL_PROFILE_3 = 3
    SPECIAL_PROFILE_5 = 5
    SPECIAL_PROFILE_6 = 6


class DeviceControlThalamusMovementTimedAccess(BaseModel):
    profile: ThalamusMovementTimedAccessAllowedSpecialProfile
    lock_time: Optional[str] = None
    unlock_time: Optional[str] = None


class UpdateDeviceTag(BaseModel):
    tag_id: Optional[int] = None
    request_action: DeviceTagAction
    profile: DeviceTagProfile
    timed_access: Optional[DeviceControlThalamusMovementTimedAccess] = None
