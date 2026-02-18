from datetime import datetime, time, date
from enum import IntEnum
from typing import Any, Optional, List

from pydantic import BaseModel, Field


class DeviceType(IntEnum):
    UNKNOWN_DEVICE_0 = 0
    HUB = 1
    REPEATER = 2
    PET_DOOR_CONNECT = 3
    PET_FEEDER_CONNECT = 4
    PROGRAMMER = 5
    DUALSCAN_CAT_FLAP_CONNECT = 6
    MICROCHIP_FEEDER = 7
    FELAQUA_CONNECT = 8  # Poseidon
    CAT_FLAP_CONNECT = 9
    DUALSCAN_PET_DOOR_CONNECT = 10
    DOG_BOWL_CONNECT = 32  # Cerberus
    UNKNOWN_DEVICE_255 = 255


# TODO: Add descriptive names to numeric special profiles
class SpecialProfile(IntEnum):
    SPECIAL_PROFILE_0 = 0
    SPECIAL_PROFILE_1 = 1
    SPECIAL_PROFILE_2 = 2
    SPECIAL_PROFILE_3 = 3
    SPECIAL_PROFILE_4 = 4
    SPECIAL_PROFILE_5 = 5
    SPECIAL_PROFILE_6 = 6


class AuthLogin(BaseModel):
    client_uid: str
    email_address: str
    password: str


class AuthToken(BaseModel):
    token: str


class Tag(BaseModel):
    id: int
    tag: Optional[str] = None
    supported_product_ids: Optional[List[DeviceType]] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class Curfew(BaseModel):
    enabled: Optional[bool] = None
    lock_time: Optional[time] = None
    unlock_time: Optional[time] = None


class DeviceControl(BaseModel):
    curfew: Curfew | List[Curfew] | None = None
    fast_polling: Optional[bool] = None
    locking: Optional[int] = None
    led_mode: Optional[int] = None
    pairing_mode: Optional[int] = None


class DeviceStatus(BaseModel):
    led_mode: Optional[int] = None
    pairing_mode: Optional[int] = None
    status: Optional[bool] = None


class Device(BaseModel):
    id: int
    parent_device_id: Optional[int] = None
    product_id: int
    household_id: Optional[int] = None
    index: Optional[int] = None
    name: Optional[str] = None
    serial_number: Optional[str] = None
    mac_address: Optional[str] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    pairing_at: Optional[datetime] = None
    last_activity_at: Optional[datetime] = None
    last_new_event_at: Optional[datetime] = None
    control: Optional[DeviceControl] = None


class Photo(BaseModel):
    id: int
    title: Optional[str] = None
    location: Optional[str] = None
    hash: Optional[str] = None
    uploading_user_id: Optional[int] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PetPositionWhere(IntEnum):
    INSIDE = 1
    OUTSIDE = 2


class CreatePetPosition(BaseModel):
    where: PetPositionWhere
    since: Optional[datetime] = None


class PetPosition(BaseModel):
    id: int
    pet_id: Optional[int] = None
    tag_id: Optional[int] = None
    device_id: Optional[int] = None
    user_id: Optional[int] = None
    where: Optional[PetPositionWhere] = None
    since: Optional[datetime] = None


class PetConsumptionStatus(BaseModel):
    id: int
    tag_id: Optional[int] = None
    device_id: Optional[int] = None
    change: Optional[List[float]] = None
    at: Optional[datetime] = None


class PetStatus(BaseModel):
    pet_id: Optional[int] = None
    activity: Optional[PetPosition] = None
    feeding: Optional[PetConsumptionStatus] = None
    drinking: Optional[PetConsumptionStatus] = None


class PetCondition(BaseModel):
    id: int
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PetGender(IntEnum):
    FEMALE = 0
    MALE = 1


class Spayed(IntEnum):
    UNKNOWN = 0
    YES = 1
    NO = 2


class Pet(BaseModel):
    id: int
    name: Optional[str] = None
    gender: Optional[PetGender] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[str] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id_2: Optional[int] = None
    food_type_id: Optional[int] = None
    household_id: Optional[int] = None
    photo_id: Optional[int] = None
    species_id: Optional[int] = None
    spayed: Optional[Spayed] = None
    tag_id: Optional[int] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    photo: Optional[Photo] = None
    conditions: Optional[List[PetCondition]] = None
    tag: Optional[Tag] = None
    status: Optional[PetStatus] = None
    position: Optional[PetPosition] = None


class PublicUser(BaseModel):
    id: int
    name: Optional[str] = None
    photo_id: Optional[int] = None
    photo: Optional[Photo] = None


class HouseholdInviteUser(BaseModel):
    creator: Optional[PublicUser] = None
    acceptor: Optional[PublicUser] = None


class HouseholdInviteStatus(IntEnum):
    PENDING = 0
    ACCEPTED = 1
    EXPIRED = 2


class HouseholdInvite(BaseModel):
    id: int
    code: Optional[str] = None
    email_address: Optional[str] = None
    owner: Optional[bool] = None
    write: Optional[bool] = None
    status: Optional[HouseholdInviteStatus] = None
    user: Optional[HouseholdInviteUser] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    used_at: Optional[datetime] = None


class HouseholdUser(BaseModel):
    id: int
    owner: Optional[bool] = None
    write: Optional[bool] = None
    user: Optional[PublicUser] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Timezone(BaseModel):
    id: int
    name: Optional[str] = None
    timezone: Optional[str] = None
    utc_offset: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Household(BaseModel):
    id: int
    name: Optional[str] = None
    share_code: Optional[str] = None
    created_user_id: Optional[int] = None
    timezone_id: Optional[int] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    invites: Optional[List[HouseholdInvite]] = None
    users: Optional[List[HouseholdUser]] = None
    timezone: Optional[Timezone] = None


class MeStart(BaseModel):
    devices: Optional[List[Device]] = None
    households: Optional[List[Household]] = None
    pets: Optional[List[Pet]] = None
    photos: Optional[List[Photo]] = None
    tags: Optional[List[Tag]] = None
    user: Optional[HouseholdUser] = None


class ConsumptionHabitOutcomeEnum(IntEnum):
    OK = 0
    BELOW_LIMIT = 1
    ABOVE_LIMIT = 2


class ReportWeightFrame(BaseModel):
    index: Optional[int] = None
    weight: float
    change: float
    food_type_id: Optional[int] = None
    target_weight: Optional[int] = None
    multi: Optional[bool] = None


class FeedingReportDataPoint(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias="from")
    to: Optional[datetime] = None
    duration: Optional[int] = None

    context: Optional[int] = None
    bowl_count: Optional[int] = None
    actual_weight: Optional[float] = None
    weights: Optional[List[ReportWeightFrame]] = None

    device_id: Optional[int] = None
    tag_id: Optional[int] = None

    user_id: Optional[int] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class FeedingReport(BaseModel):
    datapoints: Optional[List[FeedingReportDataPoint]] = None


class DrinkingReportDataPoint(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias="from")
    to: Optional[datetime] = None
    duration: Optional[int] = None

    context: Optional[int] = None
    bowl_count: Optional[int] = None
    weights: Optional[List[ReportWeightFrame]] = None
    actual_weight: Optional[float] = None

    device_id: Optional[int] = None
    tag_id: Optional[int] = None

    user_id: Optional[int] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class DrinkingReport(BaseModel):
    datapoints: Optional[List[DrinkingReportDataPoint]] = None


class MovementReportDataPoint(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias="from")
    to: Optional[datetime] = None
    duration: Optional[int] = None

    active: Optional[bool] = None
    device_id: Optional[int] = None
    entry_device_id: Optional[int] = None
    exit_device_id: Optional[int] = None
    tag_id: Optional[int] = None

    user_id: Optional[int] = None
    entry_user_id: Optional[int] = None
    exit_user_id: Optional[int] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class MovementReport(BaseModel):
    datapoints: Optional[List[MovementReportDataPoint]] = None


class ConsumptionHabit(BaseModel):
    outcome: ConsumptionHabitOutcomeEnum
    calendar_day: date
    amount: int
    lower_limit: Optional[int] = None
    upper_limit: Optional[int] = None
    created_at: datetime


class ConsumptionAlert(BaseModel):
    pet_id: int
    tag_id: int
    pet_weight: int
    amount: int
    time_noticed_utc: datetime
    created_at: datetime


class PetReport(BaseModel):
    movement: MovementReport
    feeding: FeedingReport
    drinking: DrinkingReport

    consumption_habit: Optional[List[ConsumptionHabit]] = None
    consumption_alert: Optional[List[ConsumptionAlert]] = None


class AnimoPetResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    gender: Optional[Any] = None
    date_of_birth: Optional[Any] = None
    weight: Optional[Any] = None
    breed_id: Optional[Any] = None
    household_id: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class AnimoPetResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class AuthChangePasswordResource(BaseModel):
    user_id: Optional[Any] = None
    password: Optional[Any] = None
    new_password: Optional[Any] = None


class AuthLoginResource(BaseModel):
    client_uid: Optional[Any] = None
    device_id: Optional[Any] = None
    email_address: Optional[Any] = None
    password: Optional[Any] = None


class AuthLogoutResource(BaseModel):
    client_uid: Optional[Any] = None
    device_id: Optional[Any] = None


class AuthRegisterResource(BaseModel):
    email_address: Optional[Any] = None
    first_name: Optional[Any] = None
    last_name: Optional[Any] = None
    password: Optional[Any] = None
    language_id: Optional[Any] = None
    country_id: Optional[Any] = None
    photo_id: Optional[Any] = None
    marketing_opt_in: Optional[Any] = None
    weight_units: Optional[Any] = None
    time_format: Optional[Any] = None
    device_id: Optional[Any] = None


class AuthResetPasswordRequestResource(BaseModel):
    email_address: Optional[Any] = None


class AuthResetPasswordResource(BaseModel):
    email_address: Optional[Any] = None
    password: Optional[Any] = None
    token: Optional[Any] = None
    client_uid: Optional[Any] = None
    device_id: Optional[Any] = None


class BreedQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    species_id: Optional[Any] = None
    lang: Optional[Any] = None


class BreedResource(BaseModel):
    id: Optional[Any] = None
    species_id: Optional[Any] = None
    name: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class BreedResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class BreedResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class ConditionQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    lang: Optional[Any] = None


class ConditionResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class ConditionResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class ConditionResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class ConsumptionAlertResource(BaseModel):
    pet_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    pet_weight: Optional[Any] = None
    amount: Optional[Any] = None
    time_noticed_utc: Optional[Any] = None
    created_at: Optional[Any] = None


class ConsumptionHabitModelStateEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ConsumptionHabitModelStateResource(BaseModel):
    pet_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    state: Optional[Any] = None


class ConsumptionHabitResource(BaseModel):
    outcome: Optional[Any] = None
    calendar_day: Optional[Any] = None
    amount: Optional[Any] = None
    lower_limit: Optional[Any] = None
    upper_limit: Optional[Any] = None
    created_at: Optional[Any] = None


class CountryQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    iso_code2: Optional[Any] = None
    lang: Optional[Any] = None


class CountryResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    native_name: Optional[Any] = None
    code: Optional[Any] = None
    default_language_id: Optional[Any] = None
    default_timezone_id: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class CountryResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class CountryResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class CreateHouseholdInviteResource(BaseModel):
    code: Optional[Any] = None
    email_address: Optional[Any] = None
    owner: Optional[Any] = None
    write: Optional[Any] = None


class CreateHouseholdResource(BaseModel):
    name: Optional[Any] = None
    timezone_id: Optional[Any] = None


class CreatePetPositionResource(BaseModel):
    where: Optional[Any] = None
    since: Optional[Any] = None


class CreatePetResource(BaseModel):
    name: Optional[Any] = None
    gender: Optional[Any] = None
    date_of_birth: Optional[Any] = None
    weight: Optional[Any] = None
    comments: Optional[Any] = None
    breed_id: Optional[Any] = None
    breed_id2: Optional[Any] = None
    spayed: Optional[Any] = None
    food_type_id: Optional[Any] = None
    photo_id: Optional[Any] = None
    species_id: Optional[Any] = None
    conditions: Optional[Any] = None
    household_id: Optional[Any] = None


class CreateUserSettingsResource(BaseModel):
    key: Optional[Any] = None
    value: Optional[Any] = None


class DeleteAccountResource(BaseModel):
    password: Optional[Any] = None
    households: Optional[Any] = None


class DeviceControlPendingResource(BaseModel):
    state: Optional[Any] = None
    request_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    requested_by: Optional[Any] = None


class DeviceControlResource(BaseModel):
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


class DeviceControlStateChangeResource(BaseModel):
    request_id: Optional[Any] = None
    response_id: Optional[Any] = None
    status: Optional[Any] = None
    status_id: Optional[Any] = None
    requested_at: Optional[Any] = None
    committed_at: Optional[Any] = None
    device_id: Optional[Any] = None
    state: Optional[Any] = None
    requested_by: Optional[Any] = None
    child_state_changes: Optional[Any] = None
    parent_request_id: Optional[Any] = None


class DeviceControlStateChangeResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class DeviceControlStateChangeResourceListDataResponse(BaseModel):
    data: Optional[Any] = None


class DeviceNeedsUpdateResource(BaseModel):
    needs_manual_update: Optional[Any] = None


class DeviceNeedsUpdateResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class DevicePairByCodeResource(BaseModel):
    pairing_code: Optional[Any] = None


class DeviceReadinessResource(BaseModel):
    device_ready: Optional[Any] = None
    profiles_available: Optional[Any] = None
    profiles_updated_at: Optional[Any] = None


class DeviceReadinessResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class DeviceResource(BaseModel):
    id: Optional[Any] = None
    parent_device_id: Optional[Any] = None
    product_id: Optional[Any] = None
    household_id: Optional[Any] = None
    index: Optional[Any] = None
    name: Optional[Any] = None
    serial_number: Optional[Any] = None
    mac_address: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    pairing_at: Optional[Any] = None
    last_activity_at: Optional[Any] = None
    last_new_event_at: Optional[Any] = None
    control: Optional[Any] = None
    status: Optional[Any] = None
    tags: Optional[Any] = None


class DeviceResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class DeviceResourceIEnumerableDataResponse(BaseModel):
    data: Optional[Any] = None


class DeviceResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class DeviceTagDataResource(BaseModel):
    data: Optional[Any] = None
    pending: Optional[Any] = None
    results: Optional[Any] = None


class DeviceTagResource(BaseModel):
    id: Optional[Any] = None
    device_id: Optional[Any] = None
    index: Optional[Any] = None
    profile: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class DeviceTagResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class DeviceTagResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


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


class ErrorResource(BaseModel):
    success: Optional[Any] = None
    error: Optional[Any] = None


class FoodTypeQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    lang: Optional[Any] = None


class FoodTypeResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class FoodTypeResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class FoodTypeResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class HouseholdInviteResource(BaseModel):
    id: Optional[Any] = None
    code: Optional[Any] = None
    email_address: Optional[Any] = None
    owner: Optional[Any] = None
    write: Optional[Any] = None
    status: Optional[Any] = None
    user: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    used_at: Optional[Any] = None


class HouseholdInviteResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class HouseholdInviteResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class HouseholdInviteUserResource(BaseModel):
    creator: Optional[Any] = None
    acceptor: Optional[Any] = None


class HouseholdResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    share_code: Optional[Any] = None
    created_user_id: Optional[Any] = None
    timezone_id: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    invites: Optional[Any] = None
    users: Optional[Any] = None
    timezone: Optional[Any] = None


class HouseholdResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class HouseholdResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class HouseholdUserResource(BaseModel):
    id: Optional[Any] = None
    owner: Optional[Any] = None
    write: Optional[Any] = None
    user: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class HouseholdUserResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class HouseholdUserResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class InfoResource(BaseModel):
    language: Optional[Any] = None
    country: Optional[Any] = None


class InfoResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class InviteResource(BaseModel):
    id: Optional[Any] = None
    code: Optional[Any] = None
    email_address: Optional[Any] = None
    owner: Optional[Any] = None
    write: Optional[Any] = None
    status: Optional[Any] = None
    user: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    used_at: Optional[Any] = None


class InviteResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class InviteResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class LanguageResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    native_name: Optional[Any] = None
    code: Optional[Any] = None
    enabled: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class LanguageResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class LanguageResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class MeStartResource(BaseModel):
    devices: Optional[Any] = None
    households: Optional[Any] = None
    pets: Optional[Any] = None
    photos: Optional[Any] = None
    tags: Optional[Any] = None
    user: Optional[Any] = None
    segments: Optional[Any] = None


class MeStartResourceDataResponse(BaseModel):
    data: Optional[Any] = None


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


class NotificationResource(BaseModel):
    id: Optional[Any] = None
    type: Optional[Any] = None
    text: Optional[Any] = None
    created_at: Optional[Any] = None


class NotificationResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class ObjectDataResponse(BaseModel):
    data: Optional[Any] = None


class PaginatedMetaDataResult(BaseModel):
    page: Optional[Any] = None
    page_size: Optional[Any] = None
    count: Optional[Any] = None
    total_pages: Optional[Any] = None


class PetConditionResource(BaseModel):
    id: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class PetConditionResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class PetConditionResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class PetConsumption(BaseModel):
    total_consumption: Optional[Any] = None
    date: Optional[Any] = None


class PetConsumptionResource(BaseModel):
    date: Optional[Any] = None
    last_consumption: Optional[Any] = None
    substance_type: Optional[Any] = None
    total_consumption: Optional[Any] = None
    number_of_visits: Optional[Any] = None
    consumption_time: Optional[Any] = None
    activity: Optional[Any] = None
    device_ids: Optional[Any] = None


class PetConsumptionStatusResource(BaseModel):
    id: Optional[Any] = None
    tag_id: Optional[Any] = None
    device_id: Optional[Any] = None
    change: Optional[Any] = None
    at: Optional[Any] = None


class PetDashboardQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    pet_id: Optional[Any] = None
    from_: Optional[Any] = Field(default=None, alias='from')
    days_history: Optional[Any] = None


class PetDashboardResource(BaseModel):
    pet_id: Optional[Any] = None
    movement: Optional[Any] = None
    drinking: Optional[Any] = None
    feeding: Optional[Any] = None
    drinking_habit: Optional[Any] = None
    drinking_alert: Optional[Any] = None
    habit_model_state: Optional[Any] = None


class PetDashboardResourceListDataResponse(BaseModel):
    data: Optional[Any] = None


class PetGenderEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class PetInsightQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    from_: Optional[Any] = Field(default=None, alias='from')
    to: Optional[Any] = None


class PetInsightResource(BaseModel):
    pet_id: Optional[Any] = None
    drinking_habit: Optional[Any] = None
    drinking_alert: Optional[Any] = None
    habit_model_state: Optional[Any] = None


class PetInsightResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class PetMovement(BaseModel):
    date: Optional[Any] = None
    time_outside: Optional[Any] = None


class PetMovementResource(BaseModel):
    date: Optional[Any] = None
    where: Optional[Any] = None
    time_outside: Optional[Any] = None
    since: Optional[Any] = None
    last_entry: Optional[Any] = None
    trips_outside: Optional[Any] = None
    entries: Optional[Any] = None
    time_outside_in_seconds: Optional[Any] = None
    activity: Optional[Any] = None
    device_ids: Optional[Any] = None


class PetPositionResource(BaseModel):
    id: Optional[Any] = None
    pet_id: Optional[Any] = None
    tag_id: Optional[Any] = None
    device_id: Optional[Any] = None
    user_id: Optional[Any] = None
    where: Optional[Any] = None
    since: Optional[Any] = None


class PetPositionResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class PetPositionResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class PetResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    gender: Optional[Any] = None
    date_of_birth: Optional[Any] = None
    weight: Optional[Any] = None
    comments: Optional[Any] = None
    breed_id: Optional[Any] = None
    breed_id2: Optional[Any] = None
    food_type_id: Optional[Any] = None
    household_id: Optional[Any] = None
    photo_id: Optional[Any] = None
    species_id: Optional[Any] = None
    spayed: Optional[Any] = None
    tag_id: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None
    photo: Optional[Any] = None
    conditions: Optional[Any] = None
    tag: Optional[Any] = None
    status: Optional[Any] = None
    position: Optional[Any] = None


class PetResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class PetResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class PetStatusResource(BaseModel):
    pet_id: Optional[Any] = None
    activity: Optional[Any] = None
    feeding: Optional[Any] = None
    drinking: Optional[Any] = None


class PetStatusResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class PetStatusResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class PhotoResource(BaseModel):
    id: Optional[Any] = None
    title: Optional[Any] = None
    location: Optional[Any] = None
    hash: Optional[Any] = None
    uploading_user_id: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class PhotoResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class PhotoResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class ProblemDetails(BaseModel):
    type: Optional[Any] = None
    title: Optional[Any] = None
    status: Optional[Any] = None
    detail: Optional[Any] = None
    instance: Optional[Any] = None


class ProductQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    lang: Optional[Any] = None


class ProductResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class ProductResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class ProductResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class PublicUserResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    photo_id: Optional[Any] = None
    photo: Optional[Any] = None


class PublicUserResourceDataResponse(BaseModel):
    data: Optional[Any] = None


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


class ReportHouseholdQueryResource(BaseModel):
    from_: Optional[Any] = Field(default=None, alias='from')
    to: Optional[Any] = None


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


class ReportHouseholdResourceListDataResponse(BaseModel):
    data: Optional[Any] = None


class RequestChangeStateResponseStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class SpayedEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class SpecialProfiles(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class SpeciesQueryResource(BaseModel):
    page: Optional[Any] = None
    items_per_page: Optional[Any] = None
    page_size: Optional[Any] = None
    lang: Optional[Any] = None


class SpeciesResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class SpeciesResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class SpeciesResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class StartQueryResource(BaseModel):
    lang: Optional[Any] = None


class StartResource(BaseModel):
    breed: Optional[Any] = None
    condition: Optional[Any] = None
    country: Optional[Any] = None
    language: Optional[Any] = None
    product: Optional[Any] = None
    timezone: Optional[Any] = None


class StartResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class SubstanceTypesEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class TagDeviceResource(BaseModel):
    id: Optional[Any] = None
    index: Optional[Any] = None
    profile: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class TagDeviceResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class TagDeviceResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class TagResource(BaseModel):
    id: Optional[Any] = None
    tag: Optional[Any] = None
    supported_product_ids: Optional[Any] = None
    incompatible_product_ids: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    deleted_at: Optional[Any] = None


class TagResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class TagResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class TimelineEventType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_40 = 40
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_9999 = 9999
    VALUE_19999 = 19999
    VALUE_20000 = 20000
    VALUE_20001 = 20001
    VALUE_20002 = 20002
    VALUE_20003 = 20003
    VALUE_20004 = 20004
    VALUE_20005 = 20005
    VALUE_20006 = 20006
    VALUE_20007 = 20007
    VALUE_20008 = 20008
    VALUE_20009 = 20009
    VALUE_20010 = 20010
    VALUE_20011 = 20011
    VALUE_20012 = 20012
    VALUE_20399 = 20399
    VALUE_20400 = 20400
    VALUE_20401 = 20401
    VALUE_20402 = 20402
    VALUE_20403 = 20403
    VALUE_20404 = 20404
    VALUE_20405 = 20405
    VALUE_20406 = 20406
    VALUE_20407 = 20407
    VALUE_20408 = 20408
    VALUE_20409 = 20409
    VALUE_20410 = 20410
    VALUE_20411 = 20411
    VALUE_20999 = 20999
    VALUE_21000 = 21000
    VALUE_21001 = 21001
    VALUE_21002 = 21002
    VALUE_21003 = 21003
    VALUE_21004 = 21004
    VALUE_21005 = 21005
    VALUE_21006 = 21006
    VALUE_21007 = 21007
    VALUE_21008 = 21008
    VALUE_21009 = 21009
    VALUE_21010 = 21010
    VALUE_21011 = 21011
    VALUE_21012 = 21012
    VALUE_21013 = 21013
    VALUE_21014 = 21014
    VALUE_21015 = 21015
    VALUE_21016 = 21016
    VALUE_21017 = 21017
    VALUE_21018 = 21018
    VALUE_21019 = 21019
    VALUE_21020 = 21020
    VALUE_21999 = 21999
    VALUE_23000 = 23000
    VALUE_23001 = 23001
    VALUE_23002 = 23002
    VALUE_23003 = 23003
    VALUE_23004 = 23004
    VALUE_23005 = 23005
    VALUE_23006 = 23006
    VALUE_23999 = 23999
    VALUE_24999 = 24999
    VALUE_26999 = 26999
    VALUE_28999 = 28999
    VALUE_30000 = 30000
    VALUE_30001 = 30001
    VALUE_30002 = 30002


class TimelineResource(BaseModel):
    id: Optional[Any] = None
    type: Optional[Any] = None
    data: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    households: Optional[Any] = None
    devices: Optional[Any] = None
    movements: Optional[Any] = None
    pets: Optional[Any] = None
    tags: Optional[Any] = None
    users: Optional[Any] = None
    weights: Optional[Any] = None


class TimelineResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class TimezoneResource(BaseModel):
    id: Optional[Any] = None
    name: Optional[Any] = None
    timezone: Optional[Any] = None
    utc_offset: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class TimezoneResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class TimezoneResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class UpdateDeviceResource(BaseModel):
    name: Optional[Any] = None


class UpdateDeviceTagResource(BaseModel):
    profile: Optional[Any] = None


class UpdateHouseholdInviteResource(BaseModel):
    owner: Optional[Any] = None
    write: Optional[Any] = None


class UpdateHouseholdResource(BaseModel):
    name: Optional[Any] = None
    timezone_id: Optional[Any] = None


class UpdateHouseholdUserResource(BaseModel):
    owner: Optional[Any] = None
    write: Optional[Any] = None


class UpdateMeResource(BaseModel):
    email_address: Optional[Any] = None
    first_name: Optional[Any] = None
    last_name: Optional[Any] = None
    language_id: Optional[Any] = None
    country_id: Optional[Any] = None
    photo_id: Optional[Any] = None
    marketing_opt_in: Optional[Any] = None
    weight_units: Optional[Any] = None
    time_format: Optional[Any] = None
    notifications: Optional[Any] = None
    password: Optional[Any] = None


class UpdatePetResource(BaseModel):
    name: Optional[Any] = None
    gender: Optional[Any] = None
    date_of_birth: Optional[Any] = None
    weight: Optional[Any] = None
    comments: Optional[Any] = None
    breed_id: Optional[Any] = None
    breed_id2: Optional[Any] = None
    spayed: Optional[Any] = None
    food_type_id: Optional[Any] = None
    photo_id: Optional[Any] = None
    species_id: Optional[Any] = None
    conditions: Optional[Any] = None


class UpdatePhotoResource(BaseModel):
    title: Optional[Any] = None


class UpdateUserSettingsResource(BaseModel):
    value: Optional[Any] = None


class UserClientPlatformAppResource(BaseModel):
    bundle_identifier: Optional[Any] = None
    version: Optional[Any] = None


class UserClientPlatformDeviceModelResource(BaseModel):
    name: Optional[Any] = None
    manufacturer: Optional[Any] = None
    version: Optional[Any] = None


class UserClientPlatformDeviceOsResource(BaseModel):
    platform: Optional[Any] = None
    version: Optional[Any] = None


class UserClientPlatformDeviceResource(BaseModel):
    name: Optional[Any] = None
    model: Optional[Any] = None
    uuid: Optional[Any] = None
    os: Optional[Any] = None


class UserClientPlatformLocaleResource(BaseModel):
    language: Optional[Any] = None
    country: Optional[Any] = None


class UserClientPlatformResource(BaseModel):
    app: Optional[Any] = None
    device: Optional[Any] = None
    locale: Optional[Any] = None


class UserClientResource(BaseModel):
    platform: Optional[Any] = None
    token: Optional[Any] = None


class UserClientResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class UserClientResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class UserResource(BaseModel):
    id: Optional[Any] = None
    email_address: Optional[Any] = None
    first_name: Optional[Any] = None
    last_name: Optional[Any] = None
    country_id: Optional[Any] = None
    language_id: Optional[Any] = None
    photo_id: Optional[Any] = None
    marketing_opt_in: Optional[Any] = None
    terms_accepted: Optional[Any] = None
    weight_units: Optional[Any] = None
    time_format: Optional[Any] = None
    notifications: Optional[Any] = None
    photo: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None
    use_colour: Optional[Any] = None


class UserResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class UserSettingResource(BaseModel):
    id: Optional[Any] = None
    user_id: Optional[Any] = None
    key: Optional[Any] = None
    value: Optional[Any] = None
    version: Optional[Any] = None
    created_at: Optional[Any] = None
    updated_at: Optional[Any] = None


class UserSettingResourceDataResponse(BaseModel):
    data: Optional[Any] = None


class UserSettingResourcePaginatedDataResult(BaseModel):
    data: Optional[Any] = None
    meta: Optional[Any] = None


class UserTimeFormatEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class UserWeightUnitEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


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
