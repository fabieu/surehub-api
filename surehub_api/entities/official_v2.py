from datetime import datetime, date
from enum import IntEnum
from typing import Any, Optional, List

from pydantic import BaseModel, Field


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


class ChangeProfileActionEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class ConsumptionAlert(BaseModel):
    pet_id: Optional[int] = None
    tag_id: Optional[int] = None
    pet_weight: Optional[int] = None
    amount: Optional[int] = None
    time_noticed_utc: Optional[datetime] = None
    created_at: Optional[datetime] = None


class ConsumptionHabitOutcomeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class ConsumptionHabit(BaseModel):
    outcome: Optional[Any] = None
    calendar_day: Optional[date] = None
    amount: Optional[int] = None
    lower_limit: Optional[int] = None
    upper_limit: Optional[int] = None
    created_at: Optional[datetime] = None


class DeviceControlCurfew(BaseModel):
    enabled: Optional[bool] = None
    lock_time: Optional[str] = None
    unlock_time: Optional[str] = None


class DeviceControlDualScanPetDoorV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    timed_access: Optional[List[Any]] = None
    locking: Optional[Any] = None
    lockdown: Optional[bool] = None
    timed_access_override: Optional[bool] = None


class DeviceControlDualScanPetDoorV2DeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlDualScanPetDoorV2DeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlDualScanV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    timed_access: Optional[List[Any]] = None
    locking: Optional[Any] = None
    lockdown: Optional[bool] = None


class DeviceControlDualScanV2DeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlDualScanV2DeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlFeederBowl(BaseModel):
    settings: Optional[List[Any]] = None
    type: Optional[Any] = None


class DeviceControlFeederBowlSettings(BaseModel):
    food_type: Optional[Any] = None
    target: Optional[float] = None


class DeviceControlFeederLid(BaseModel):
    close_delay: Optional[int] = None


class DeviceControlFeederV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    bowls: Optional[Any] = None
    lid: Optional[Any] = None
    tare: Optional[Any] = None
    training_mode: Optional[Any] = None
    timed_feeding: Optional[List[Any]] = None


class DeviceControlFeederV2DeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlFeederV2DeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlFeederTagTimedFeeding(BaseModel):
    tag_id: Optional[int] = None
    fasting: Optional[List[Any]] = None


class DeviceControlFeederTimedFeeding(BaseModel):
    enabled: Optional[bool] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class DeviceControlHub(BaseModel):
    led_mode: Optional[Any] = None
    pairing_mode: Optional[Any] = None
    flash_leds: Optional[bool] = None


class DeviceControlHubDeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlHubDeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlNoIdDogBowl(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    food_type: Optional[Any] = None
    substance_type: Optional[Any] = None


class DeviceControlNoIdDogBowlDeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlNoIdDogBowlDeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPetDoorMicrochip(BaseModel):
    microchip_number: Optional[str] = None
    type: Optional[Any] = None


class DeviceControlPetDoor(BaseModel):
    fast_polling: Optional[bool] = None
    curfew: Optional[Any] = None
    locking: Optional[Any] = None
    tag_profiles: Optional[List[Any]] = None


class DeviceControlPetDoorDeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPetDoorDeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlPetDoorTagProfile(BaseModel):
    tag_id: Optional[int] = None
    index: Optional[int] = None
    microchip: Optional[Any] = None


class DeviceControlPoseidon(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    learn_mode: Optional[bool] = None


class DeviceControlPoseidonDeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPoseidonDeviceControl(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlResult(BaseModel):
    request_id: Optional[str] = None
    response_id: Optional[str] = None
    status: Optional[Any] = None
    status_id: Optional[Any] = None
    requested_at: Optional[datetime] = None
    committed_at: Optional[datetime] = None


class DeviceControlThalamusMicrochip(BaseModel):
    microchip_number: Optional[str] = None
    type: Optional[Any] = None


class DeviceControlThalamusMovementTagTimedAccess(BaseModel):
    tag_id: Optional[int] = None
    timed_access: Optional[List[Any]] = None


class DeviceControlThalamusTagProfile(BaseModel):
    tag_id: Optional[int] = None
    index: Optional[int] = None
    profile: Optional[Any] = None
    action: Optional[Any] = None
    request_action: Optional[Any] = None
    microchip: Optional[Any] = None


class DeviceV2(BaseModel):
    id: Optional[int] = None


class DeviceTagData(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceTagProfiles(IntEnum):
    VALUE_2 = 2
    VALUE_3 = 3


class DeviceTag(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    index: Optional[int] = None
    profile: Optional[int] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DoorDirectionEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class DoorSide(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DoorStatusEnum(IntEnum):
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_8 = 8
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13


class DualScanLockingModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class Error(BaseModel):
    success: Optional[bool] = None
    error: Optional[dict] = None


class FeederBowlTypeEnum(IntEnum):
    VALUE_1 = 1
    VALUE_4 = 4
    VALUE_5 = 5


class FoodTypesEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class HouseholdV2(BaseModel):
    id: Optional[int] = None


class LedModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_128 = 128


class Movement(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None
    direction: Optional[Any] = None
    side: Optional[Any] = None
    type: Optional[Any] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PaginatedMetaDataResult(BaseModel):
    page: Optional[int] = None
    page_size: Optional[int] = None
    count: Optional[int] = None
    total_pages: Optional[int] = None


class PairingModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_128 = 128


class PetDoorLockingModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class PetDoorTagType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_128 = 128


class PetV2(BaseModel):
    id: Optional[int] = None


class Photo(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    location: Optional[str] = None
    hash: Optional[str] = None
    uploading_user_id: Optional[int] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProblemDetails(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    status: Optional[int] = None
    detail: Optional[str] = None
    instance: Optional[str] = None


class PublicUser(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    photo_id: Optional[int] = None
    photo: Optional[Any] = None


class ReportHouseholdDrinkingDataPoint(BaseModel):
    datapoints: Optional[List[Any]] = None


class ReportHouseholdDrinking(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None
    duration: Optional[int] = None
    context: Optional[int] = None
    bowl_count: Optional[int] = None
    device_id: Optional[int] = None
    weights: Optional[List[Any]] = None
    actual_weight: Optional[float] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None


class ReportHouseholdEvent(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class ReportHouseholdFeedingDataPoint(BaseModel):
    datapoints: Optional[List[Any]] = None


class ReportHouseholdFeeding(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None
    duration: Optional[int] = None
    context: Optional[int] = None
    bowl_count: Optional[int] = None
    device_id: Optional[int] = None
    weights: Optional[List[Any]] = None
    actual_weight: Optional[float] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None


class ReportHouseholdMovementDataPoint(BaseModel):
    datapoints: Optional[List[Any]] = None


class ReportHouseholdMovement(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None
    duration: Optional[int] = None
    entry_device_id: Optional[int] = None
    entry_user_id: Optional[int] = None
    exit_device_id: Optional[int] = None
    exit_user_id: Optional[int] = None
    active: Optional[bool] = None
    exit_movement_id: Optional[int] = None
    entry_movement_id: Optional[int] = None


class ReportHousehold(BaseModel):
    pet_id: Optional[int] = None
    device_id: Optional[int] = None
    movement: Optional[Any] = None
    feeding: Optional[Any] = None
    drinking: Optional[Any] = None
    consumption_habit: Optional[List[Any]] = None
    consumption_alert: Optional[List[Any]] = None


class ReportHouseholdDataResponse(BaseModel):
    data: Optional[Any] = None


class ReportHouseholdV2Query(BaseModel):
    from_: datetime = Field(alias='from')
    to: datetime
    event_type: Optional[Any] = None


class ReportWeightFrame(BaseModel):
    index: Optional[int] = None
    weight: Optional[float] = None
    change: Optional[float] = None
    food_type_id: Optional[int] = None
    target_weight: Optional[int] = None
    multi: Optional[bool] = None


class RequestChangeStateResponseStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class SpecialProfiles(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class SubstanceTypesEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class TagV2(BaseModel):
    id: Optional[int] = None


class ThalamusMovementTimedAccessAllowedSpecialProfiles(IntEnum):
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_6 = 6


class ThalamusTagType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class TimelineV2(BaseModel):
    id: Optional[int] = None
    type: Optional[int] = None
    data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    household: Optional[List[Any]] = None
    devices: Optional[List[Any]] = None
    movements: Optional[List[Any]] = None
    pets: Optional[List[Any]] = None
    tags: Optional[List[Any]] = None
    users: Optional[List[Any]] = None
    weights: Optional[List[Any]] = None


class TimelineV2PaginatedDataResult(BaseModel):
    data: Optional[List[Any]] = None
    meta: Optional[Any] = None


class TrainingMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class UpdateDeviceTagActions(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class UpdateDeviceTagV2(BaseModel):
    tag_id: Optional[int] = None
    request_action: Optional[Any] = None
    profile: Optional[Any] = None
    timed_access: Optional[List[Any]] = None


class WeightFrame(BaseModel):
    id: Optional[int] = None
    index: Optional[int] = None
    current_weight: Optional[float] = None
    change: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Weight(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None
    context: Optional[int] = None
    duration: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    frames: Optional[List[Any]] = None


class ZeroAction(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

