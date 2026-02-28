from __future__ import annotations

from datetime import datetime, date
from typing import Any, Optional, List

from pydantic import BaseModel, Field

from surehub_api.entities.enums import (
    ChangeProfileAction,
    ConsumptionHabitOutcome,
    DeviceTagProfiles,
    DoorDirection,
    DoorSide,
    DoorStatus,
    DualScanLockingMode,
    FailSafeOptions,
    FeederBowlType,
    FoodTypes,
    LedMode,
    PairingMode,
    PetDoorLockingMode,
    PetDoorTagType,
    ReportHouseholdEvent,
    RequestChangeStateResponseStatus,
    SpecialProfiles,
    SubstanceTypes,
    ThalamusMovementTimedAccessAllowedSpecialProfiles,
    ThalamusTagType,
    TrainingMode,
    UpdateDeviceTagActions,
    ZeroAction,
)


class ConsumptionAlert(BaseModel):
    pet_id: Optional[int] = None
    tag_id: Optional[int] = None
    pet_weight: Optional[int] = None
    amount: Optional[int] = None
    time_noticed_utc: Optional[datetime] = None
    created_at: Optional[datetime] = None


class ConsumptionHabit(BaseModel):
    outcome: Optional[ConsumptionHabitOutcome] = None
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
    tag_profiles: Optional[List[DeviceControlThalamusTagProfile]] = None
    timed_access: Optional[List[DeviceControlThalamusMovementTagTimedAccess]] = None
    locking: Optional[DualScanLockingMode] = None
    lockdown: Optional[bool] = None
    timed_access_override: Optional[bool] = None
    fail_safe: Optional[FailSafeOptions] = None


class DeviceControlDualScanPetDoorV2DeviceControl(BaseModel):
    data: Optional[DeviceControlDualScanPetDoorV2] = None
    pending: Optional[List[DeviceControlDualScanPetDoorV2DeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlDualScanPetDoorV2DeviceControlPending(BaseModel):
    state: Optional[DeviceControlDualScanPetDoorV2] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlDualScanV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[DeviceControlThalamusTagProfile]] = None
    timed_access: Optional[List[DeviceControlThalamusMovementTagTimedAccess]] = None
    locking: Optional[DualScanLockingMode] = None
    lockdown: Optional[bool] = None
    fail_safe: Optional[FailSafeOptions] = None


class DeviceControlDualScanV2DeviceControl(BaseModel):
    data: Optional[DeviceControlDualScanV2] = None
    pending: Optional[List[DeviceControlDualScanV2DeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlDualScanV2DeviceControlPending(BaseModel):
    state: Optional[DeviceControlDualScanV2] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlFeederBowl(BaseModel):
    settings: Optional[List[DeviceControlFeederBowlSettings]] = None
    type: Optional[FeederBowlType] = None


class DeviceControlFeederBowlSettings(BaseModel):
    food_type: Optional[FoodTypes] = None
    target: Optional[float] = None


class DeviceControlFeederLid(BaseModel):
    close_delay: Optional[int] = None


class DeviceControlFeederTagTimedFeeding(BaseModel):
    tag_id: Optional[int] = None
    fasting: Optional[List[DeviceControlFeederTimedFeeding]] = None


class DeviceControlFeederTimedFeeding(BaseModel):
    enabled: Optional[bool] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class DeviceControlFeederV2(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[DeviceControlThalamusTagProfile]] = None
    bowls: Optional[DeviceControlFeederBowl] = None
    lid: Optional[DeviceControlFeederLid] = None
    tare: Optional[ZeroAction] = None
    training_mode: Optional[TrainingMode] = None
    timed_feeding: Optional[List[DeviceControlFeederTagTimedFeeding]] = None


class DeviceControlFeederV2DeviceControl(BaseModel):
    data: Optional[DeviceControlFeederV2] = None
    pending: Optional[List[DeviceControlFeederV2DeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlFeederV2DeviceControlPending(BaseModel):
    state: Optional[DeviceControlFeederV2] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlHub(BaseModel):
    led_mode: Optional[LedMode] = None
    pairing_mode: Optional[PairingMode] = None
    flash_leds: Optional[bool] = None


class DeviceControlHubDeviceControl(BaseModel):
    data: Optional[DeviceControlHub] = None
    pending: Optional[List[DeviceControlHubDeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlHubDeviceControlPending(BaseModel):
    state: Optional[DeviceControlHub] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlNoIdDogBowl(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[DeviceControlThalamusTagProfile]] = None
    food_type: Optional[FoodTypes] = None
    substance_type: Optional[SubstanceTypes] = None


class DeviceControlNoIdDogBowlDeviceControl(BaseModel):
    data: Optional[DeviceControlNoIdDogBowl] = None
    pending: Optional[List[DeviceControlNoIdDogBowlDeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlNoIdDogBowlDeviceControlPending(BaseModel):
    state: Optional[DeviceControlNoIdDogBowl] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPending(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPetDoor(BaseModel):
    fast_polling: Optional[bool] = None
    curfew: Optional[DeviceControlCurfew] = None
    locking: Optional[PetDoorLockingMode] = None
    tag_profiles: Optional[List[DeviceControlPetDoorTagProfile]] = None


class DeviceControlPetDoorDeviceControl(BaseModel):
    data: Optional[DeviceControlPetDoor] = None
    pending: Optional[List[DeviceControlPetDoorDeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlPetDoorDeviceControlPending(BaseModel):
    state: Optional[DeviceControlPetDoor] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlPetDoorMicrochip(BaseModel):
    microchip_number: Optional[str] = None
    type: Optional[PetDoorTagType] = None


class DeviceControlPetDoorTagProfile(BaseModel):
    tag_id: Optional[int] = None
    index: Optional[int] = None
    microchip: Optional[DeviceControlPetDoorMicrochip] = None


class DeviceControlPoseidon(BaseModel):
    fast_polling: Optional[bool] = None
    tag_profiles: Optional[List[DeviceControlThalamusTagProfile]] = None
    learn_mode: Optional[bool] = None


class DeviceControlPoseidonDeviceControl(BaseModel):
    data: Optional[DeviceControlPoseidon] = None
    pending: Optional[List[DeviceControlPoseidonDeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlPoseidonDeviceControlPending(BaseModel):
    state: Optional[DeviceControlPoseidon] = None
    request_id: Optional[str] = None
    requested_at: Optional[datetime] = None
    requested_by: Optional[str] = None


class DeviceControlResult(BaseModel):
    request_id: Optional[str] = None
    response_id: Optional[str] = None
    status: Optional[RequestChangeStateResponseStatus] = None
    status_id: Optional[RequestChangeStateResponseStatus] = None
    requested_at: Optional[datetime] = None
    committed_at: Optional[datetime] = None


class DeviceControlThalamusMicrochip(BaseModel):
    microchip_number: Optional[str] = None
    type: Optional[ThalamusTagType] = None


class DeviceControlThalamusMovementTagTimedAccess(BaseModel):
    tag_id: Optional[int] = None
    timed_access: Optional[List[DeviceControlThalamusMovementTimedAccess]] = None


class DeviceControlThalamusMovementTimedAccess(BaseModel):
    profile: Optional[ThalamusMovementTimedAccessAllowedSpecialProfiles]
    lock_time: Optional[str] = None
    unlock_time: Optional[str] = None


class DeviceControlThalamusTagProfile(BaseModel):
    tag_id: Optional[int] = None
    index: Optional[int] = None
    profile: Optional[SpecialProfiles] = None
    action: Optional[ChangeProfileAction] = None
    request_action: Optional[UpdateDeviceTagActions] = None
    microchip: Optional[DeviceControlThalamusMicrochip] = None


class DeviceTag(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    index: Optional[int] = None
    profile: Optional[int] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DeviceTagData(BaseModel):
    data: Optional[DeviceTag] = None
    pending: Optional[List[DeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceV2(BaseModel):
    id: Optional[int] = None


class Error(BaseModel):
    success: Optional[bool] = None
    error: Optional[dict] = None


class HouseholdV2(BaseModel):
    id: Optional[int] = None


class Movement(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None
    direction: Optional[DoorDirection] = None
    side: Optional[DoorSide] = None
    type: Optional[DoorStatus] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PaginatedMetaDataResult(BaseModel):
    page: Optional[int] = None
    page_size: Optional[int] = None
    count: Optional[int] = None
    total_pages: Optional[int] = None


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
    photo: Optional[Photo] = None


class ReportHousehold(BaseModel):
    pet_id: Optional[int] = None
    device_id: Optional[int] = None
    movement: Optional[ReportHouseholdMovementDataPoint] = None
    feeding: Optional[ReportHouseholdFeedingDataPoint] = None
    drinking: Optional[ReportHouseholdDrinkingDataPoint] = None
    consumption_habit: Optional[List[ConsumptionHabit]] = None
    consumption_alert: Optional[List[ConsumptionAlert]] = None


class ReportHouseholdDataResponse(BaseModel):
    data: Optional[ReportHousehold] = None


class ReportHouseholdDrinking(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None
    duration: Optional[int] = None
    context: Optional[int] = None
    bowl_count: Optional[int] = None
    device_id: Optional[int] = None
    weights: Optional[List[ReportWeightFrame]] = None
    actual_weight: Optional[float] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None


class ReportHouseholdDrinkingDataPoint(BaseModel):
    datapoints: Optional[List[ReportHouseholdDrinking]] = None


class ReportHouseholdFeeding(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None
    duration: Optional[int] = None
    context: Optional[int] = None
    bowl_count: Optional[int] = None
    device_id: Optional[int] = None
    weights: Optional[List[ReportWeightFrame]] = None
    actual_weight: Optional[float] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None


class ReportHouseholdFeedingDataPoint(BaseModel):
    datapoints: Optional[List[ReportHouseholdFeeding]] = None


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


class ReportHouseholdMovementDataPoint(BaseModel):
    datapoints: Optional[List[ReportHouseholdMovement]] = None


class ReportHouseholdV2Query(BaseModel):
    from_: datetime = Field(alias='from')
    to: datetime
    event_type: Optional[ReportHouseholdEvent] = None


class ReportWeightFrame(BaseModel):
    index: Optional[int] = None
    weight: Optional[float] = None
    change: Optional[float] = None
    food_type_id: Optional[int] = None
    target_weight: Optional[int] = None
    multi: Optional[bool] = None


class TagV2(BaseModel):
    id: Optional[int] = None


class TimelineV2(BaseModel):
    id: Optional[int] = None
    type: Optional[int] = None
    data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    household: Optional[List[HouseholdV2]] = None
    devices: Optional[List[DeviceV2]] = None
    movements: Optional[List[Movement]] = None
    pets: Optional[List[PetV2]] = None
    tags: Optional[List[TagV2]] = None
    users: Optional[List[PublicUser]] = None
    weights: Optional[List[Weight]] = None


class TimelineV2PaginatedDataResult(BaseModel):
    data: Optional[List[TimelineV2]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class UpdateDeviceTag(BaseModel):
    tag_id: Optional[int] = None
    request_action: UpdateDeviceTagActions
    profile: DeviceTagProfiles
    timed_access: Optional[DeviceControlThalamusMovementTimedAccess] = None


class UpdateDeviceTagV2(BaseModel):
    tag_id: Optional[int] = None
    request_action: Optional[UpdateDeviceTagActions] = None
    profile: Optional[DeviceTagProfiles] = None
    timed_access: Optional[List[DeviceControlThalamusMovementTimedAccess]] = None


class Weight(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None
    context: Optional[int] = None
    duration: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    frames: Optional[List[WeightFrame]] = None


class WeightFrame(BaseModel):
    id: Optional[int] = None
    index: Optional[int] = None
    current_weight: Optional[float] = None
    change: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
