from enum import IntEnum
from typing import Any, Optional

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
    pet_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    pet_weight: Optional[Any] = None
    amount: Optional[Any] = None
    time_noticed_utc: Optional[Any] = None
    created_at: Optional[Any] = None


class ConsumptionHabitOutcomeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class ConsumptionHabitResource(BaseModel):
    outcome: Optional[Any] = None
    calendar_day: Optional[Any] = None
    amount: Optional[Any] = None
    lower_limit: Optional[Any] = None
    upper_limit: Optional[Any] = None
    created_at: Optional[Any] = None


class DeviceControlCurfewResource(BaseModel):
    enabled: Optional[Any] = None
    lock_time: Optional[Any] = None
    unlock_time: Optional[Any] = None


class DeviceControlDualScanPetDoorResourceV2(BaseModel):
    fast_polling: Optional[Any] = None
    tag_profiles: Optional[Any] = None
    timed_access: Optional[Any] = None
    locking: Optional[Any] = None
    lockdown: Optional[Any] = None
    timed_access_override: Optional[Any] = None


class DeviceControlDualScanPetDoorResourceV2DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlDualScanPetDoorResourceV2DeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlDualScanResourceV2(BaseModel):
    fast_polling: Optional[Any] = None
    tag_profiles: Optional[Any] = None
    timed_access: Optional[Any] = None
    locking: Optional[Any] = None
    lockdown: Optional[Any] = None


class DeviceControlDualScanResourceV2DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlDualScanResourceV2DeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlFeederBowlResource(BaseModel):
    settings: Optional[Any] = None
    type: Optional[Any] = None


class DeviceControlFeederBowlSettingsResource(BaseModel):
    food_type: Optional[Any] = None
    target: Optional[Any] = None


class DeviceControlFeederLidResource(BaseModel):
    close_delay: Optional[Any] = None


class DeviceControlFeederResourceV2(BaseModel):
    fast_polling: Optional[Any] = None
    tag_profiles: Optional[Any] = None
    bowls: Optional[Any] = None
    lid: Optional[Any] = None
    tare: Optional[Any] = None
    training_mode: Optional[Any] = None
    timed_feeding: Optional[Any] = None


class DeviceControlFeederResourceV2DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlFeederResourceV2DeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlFeederTagTimedFeedingResource(BaseModel):
    tag_id: Optional[Any] = None
    fasting: Optional[Any] = None


class DeviceControlFeederTimedFeedingResource(BaseModel):
    enabled: Optional[Any] = None
    start_time: Optional[Any] = None
    end_time: Optional[Any] = None


class DeviceControlHubResource(BaseModel):
    led_mode: Optional[Any] = None
    pairing_mode: Optional[Any] = None
    flash_leds: Optional[Any] = None


class DeviceControlHubResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlHubResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlNoIdDogBowlResource(BaseModel):
    fast_polling: Optional[Any] = None
    tag_profiles: Optional[Any] = None
    food_type: Optional[Any] = None
    substance_type: Optional[Any] = None


class DeviceControlNoIdDogBowlResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlNoIdDogBowlResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlPetDoorMicrochipResource(BaseModel):
    microchip_number: Optional[Any] = None
    type: Optional[Any] = None


class DeviceControlPetDoorResource(BaseModel):
    fast_polling: Optional[Any] = None
    curfew: Optional[Any] = None
    locking: Optional[Any] = None
    tag_profiles: Optional[Any] = None


class DeviceControlPetDoorResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlPetDoorResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlPetDoorTagProfileResource(BaseModel):
    tag_id: Optional[Any] = None
    index: Optional[Any] = None
    microchip: Optional[Any] = None


class DeviceControlPoseidonResource(BaseModel):
    fast_polling: Optional[Any] = None
    tag_profiles: Optional[Any] = None
    learn_mode: Optional[Any] = None


class DeviceControlPoseidonResourceDeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlPoseidonResourceDeviceControlResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceControlResultResource(BaseModel):
    request_id: Optional[Any] = None
    response_id: Optional[Any] = None
    status: Optional[Any] = None
    status_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    committed_at: Optional[Any] = None


class DeviceControlThalamusMicrochipResource(BaseModel):
    microchip_number: Optional[Any] = None
    type: Optional[Any] = None


class DeviceControlThalamusMovementTagTimedAccessResource(BaseModel):
    tag_id: Optional[Any] = None
    timed_access: Optional[Any] = None


class DeviceControlThalamusMovementTimedAccessResource(BaseModel):
    profile: Optional[Any] = None
    lock_time: Optional[Any] = None
    unlock_time: Optional[Any] = None


class DeviceControlThalamusTagProfileResource(BaseModel):
    tag_id: Optional[Any] = None
    index: Optional[Any] = None
    profile: Optional[Any] = None
    action: Optional[Any] = None
    request_action: Optional[Any] = None
    microchip: Optional[Any] = None


class DeviceResourceV2(BaseModel):
    id: Optional[Any] = None


class DeviceTagDataResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceTagProfiles(IntEnum):
    VALUE_2 = 2
    VALUE_3 = 3


class DeviceTagResource(BaseModel):
    id: Optional[Any] = None
    device_id: Optional[Any] = None
    index: Optional[Any] = None
    profile: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


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
    success: Optional[Any] = None
    error: Optional[Any] = None


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
    id: Optional[Any] = None


class LedModeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_128 = 128


class MovementResource(BaseModel):
    id: Optional[Any] = None
    device_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    user_id: Optional[Any] = None
    direction: Optional[Any] = None
    side: Optional[Any] = None
    type: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class PaginatedMetaDataResult(BaseModel):
    page: Optional[Any] = None
    page_size: Optional[Any] = None
    count: Optional[Any] = None
    total_pages: Optional[Any] = None


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
    id: Optional[Any] = None


class PhotoResource(BaseModel):
    id: Optional[Any] = None
    title: Optional[Any] = None
    location: Optional[Any] = None
    hash: Optional[Any] = None
    uploading_user_id: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class ProblemDetails(BaseModel):
    type: Optional[Any] = None
    title: Optional[Any] = None
    status: Optional[Any] = None
    detail: Optional[Any] = None
    instance: Optional[Any] = None


class PublicUserResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    photo_id: Optional[Any] = None
    photo: Optional[Any] = None


class ReportHouseholdDrinkingDataPoint(BaseModel):
    datapoints: Optional[Any] = None


class ReportHouseholdDrinkingResource(BaseModel):
    from_: Optional[Any] = Field(default=None, alias='from')
    to: Optional[Any] = None
    duration: Optional[Any] = None
    context: Optional[Any] = None
    bowl_count: Optional[Any] = None
    device_id: Optional[Any] = None
    weights: Optional[Any] = None
    actual_weight: Optional[Any] = None
    entry_user_id: Optional[Any] = None
    exit_user_id: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    tag_id: Optional[Any] = None
    user_id: Optional[Any] = None


class ReportHouseholdEvent(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class ReportHouseholdFeedingDataPoint(BaseModel):
    datapoints: Optional[Any] = None


class ReportHouseholdFeedingResource(BaseModel):
    from_: Optional[Any] = Field(default=None, alias='from')
    to: Optional[Any] = None
    duration: Optional[Any] = None
    context: Optional[Any] = None
    bowl_count: Optional[Any] = None
    device_id: Optional[Any] = None
    weights: Optional[Any] = None
    actual_weight: Optional[Any] = None
    entry_user_id: Optional[Any] = None
    exit_user_id: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    tag_id: Optional[Any] = None
    user_id: Optional[Any] = None


class ReportHouseholdMovementDataPoint(BaseModel):
    datapoints: Optional[Any] = None


class ReportHouseholdMovementResource(BaseModel):
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    device_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    user_id: Optional[Any] = None
    from_: Optional[Any] = Field(default=None, alias='from')
    to: Optional[Any] = None
    duration: Optional[Any] = None
    entry_device_id: Optional[Any] = None
    entry_user_id: Optional[Any] = None
    exit_device_id: Optional[Any] = None
    exit_user_id: Optional[Any] = None
    active: Optional[Any] = None
    exit_movement_id: Optional[Any] = None
    entry_movement_id: Optional[Any] = None


class ReportHouseholdResource(BaseModel):
    pet_id: Optional[Any] = None
    device_id: Optional[Any] = None
    movement: Optional[Any] = None
    feeding: Optional[Any] = None
    drinking: Optional[Any] = None
    consumption_habit: Optional[Any] = None
    consumption_alert: Optional[Any] = None


class ReportHouseholdResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class ReportHouseholdV2QueryResource(BaseModel):
    from_: Optional[Any] = Field(default=None, alias='from')
    to: Optional[Any] = None
    event_type: Optional[Any] = None


class ReportWeightFrame(BaseModel):
    index: Optional[Any] = None
    weight: Optional[Any] = None
    change: Optional[Any] = None
    food_type_id: Optional[Any] = None
    target_weight: Optional[Any] = None
    multi: Optional[Any] = None


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
    id: Optional[Any] = None


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
    id: Optional[Any] = None
    type: Optional[Any] = None
    data: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    household: Optional[Any] = None
    devices: Optional[Any] = None
    movements: Optional[Any] = None
    pets: Optional[Any] = None
    tags: Optional[Any] = None
    users: Optional[Any] = None
    weights: Optional[Any] = None


class TimelineResourceV2PaginatedDataResult(BaseModel):
    data: Optional[Any] = None
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
    tag_id: Optional[Any] = None
    request_action: Optional[Any] = None
    profile: Optional[Any] = None
    timed_access: Optional[Any] = None


class WeightFrameResource(BaseModel):
    id: Optional[Any] = None
    index: Optional[Any] = None
    current_weight: Optional[Any] = None
    change: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class WeightResource(BaseModel):
    id: Optional[Any] = None
    device_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    context: Optional[Any] = None
    duration: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    frames: Optional[Any] = None


class ZeroAction(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
