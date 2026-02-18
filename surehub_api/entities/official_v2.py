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


class ConsumptionAlertResource(BaseModel):
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


class ConsumptionHabitResource(BaseModel):
    outcome: Optional[Any] = None
    calendar_day: Optional[date] = None
    amount: Optional[int] = None
    lower_limit: Optional[int] = None
    upper_limit: Optional[int] = None
    created_at: Optional[datetime] = None


class DeviceControlCurfewResource(BaseModel):
    enabled: Optional[bool] = None
    lock_time: Optional[str] = None
    unlock_time: Optional[str] = None


class DeviceControlDualScanPetDoorResourceV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    timed_access: Optional[List[Any]] = None
    locking: Optional[Any] = None
    lockdown: Optional[bool] = None
    timed_access_override: Optional[bool] = None


class DeviceControlDualScanPetDoorResourceV2DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlDualScanPetDoorResourceV2DeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlDualScanResourceV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    timed_access: Optional[List[Any]] = None
    locking: Optional[Any] = None
    lockdown: Optional[bool] = None


class DeviceControlDualScanResourceV2DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlDualScanResourceV2DeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlFeederBowlResource(BaseModel):
    settings: Optional[List[Any]] = None
    type: Optional[Any] = None


class DeviceControlFeederBowlSettingsResource(BaseModel):
    food_type: Optional[Any] = None
    target: Optional[float] = None


class DeviceControlFeederLidResource(BaseModel):
    close_delay: Optional[int] = None


class DeviceControlFeederResourceV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    bowls: Optional[Any] = None
    lid: Optional[Any] = None
    tare: Optional[Any] = None
    training_mode: Optional[Any] = None
    timed_feeding: Optional[List[Any]] = None


class DeviceControlFeederResourceV2DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlFeederResourceV2DeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlFeederTagTimedFeedingResource(BaseModel):
    tag_id: Optional[int] = None
    fasting: Optional[List[Any]] = None


class DeviceControlFeederTimedFeedingResource(BaseModel):
    enabled: Optional[bool] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class DeviceControlHubResource(BaseModel):
    led_mode: Optional[Any] = None
    pairing_mode: Optional[Any] = None
    flash_leds: Optional[bool] = None


class DeviceControlHubResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlHubResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlNoIdDogBowlResource(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    food_type: Optional[Any] = None
    substance_type: Optional[Any] = None


class DeviceControlNoIdDogBowlResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlNoIdDogBowlResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPetDoorMicrochipResource(BaseModel):
    microchip_number: Optional[str] = None
    type: Optional[Any] = None


class DeviceControlPetDoorResource(BaseModel):
    fast_polling: Optional[bool] = None
    curfew: Optional[Any] = None
    locking: Optional[Any] = None
    tag_profiles: Optional[List[Any]] = None


class DeviceControlPetDoorResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPetDoorResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlPetDoorTagProfileResource(BaseModel):
    tag_id: Optional[int] = None
    index: Optional[int] = None
    microchip: Optional[Any] = None


class DeviceControlPoseidonResource(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[Any]] = None
    learn_mode: Optional[bool] = None


class DeviceControlPoseidonResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPoseidonResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceControlResultResource(BaseModel):
    request_id: Optional[str] = None
    response_id: Optional[str] = None
    status: Optional[Any] = None
    status_id: Optional[Any] = None
    requested_at: Optional[datetime] = None
    committed_at: Optional[datetime] = None


class DeviceControlThalamusMicrochipResource(BaseModel):
    microchip_number: Optional[str] = None
    type: Optional[Any] = None


class DeviceControlThalamusMovementTagTimedAccessResource(BaseModel):
    tag_id: Optional[int] = None
    timed_access: Optional[List[Any]] = None


class DeviceControlThalamusMovementTimedAccessResource(BaseModel):
    profile: Optional[Any] = None
    lock_time: Optional[str] = None
    unlock_time: Optional[str] = None


class DeviceControlThalamusTagProfileResource(BaseModel):
    tag_id: Optional[int] = None
    index: Optional[int] = None
    profile: Optional[Any] = None
    action: Optional[Any] = None
    request_action: Optional[Any] = None
    microchip: Optional[Any] = None


class DeviceResourceV2(BaseModel):
    id: Optional[int] = None


class DeviceTagDataResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[Any]] = None
    results: Optional[List[Any]] = None


class DeviceTagProfiles(IntEnum):
    VALUE_2 = 2
    VALUE_3 = 3


class DeviceTagResource(BaseModel):
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


class ErrorResource(BaseModel):
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


class HouseholdResourceV2(BaseModel):
    id: Optional[int] = None


class LedModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_128 = 128


class MovementResource(BaseModel):
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


class PetResourceV2(BaseModel):
    id: Optional[int] = None


class PhotoResource(BaseModel):
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


class PublicUserResource(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    photo_id: Optional[int] = None
    photo: Optional[Any] = None


class ReportHouseholdDrinkingDataPoint(BaseModel):
    datapoints: Optional[List[Any]] = None


class ReportHouseholdDrinkingResource(BaseModel):
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


class ReportHouseholdFeedingResource(BaseModel):
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


class ReportHouseholdMovementResource(BaseModel):
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


class ReportHouseholdResource(BaseModel):
    pet_id: Optional[int] = None
    device_id: Optional[int] = None
    movement: Optional[Any] = None
    feeding: Optional[Any] = None
    drinking: Optional[Any] = None
    consumption_habit: Optional[List[Any]] = None
    consumption_alert: Optional[List[Any]] = None


class ReportHouseholdResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class ReportHouseholdV2QueryResource(BaseModel):
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


class TagResourceV2(BaseModel):
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


class TimelineResourceV2(BaseModel):
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


class TimelineResourceV2PaginatedDataResult(BaseModel):
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


class UpdateDeviceTagV2Resource(BaseModel):
    tag_id: Optional[int] = None
    request_action: Optional[Any] = None
    profile: Optional[Any] = None
    timed_access: Optional[List[Any]] = None


class WeightFrameResource(BaseModel):
    id: Optional[int] = None
    index: Optional[int] = None
    current_weight: Optional[float] = None
    change: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class WeightResource(BaseModel):
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
