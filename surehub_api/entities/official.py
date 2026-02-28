from __future__ import annotations

from datetime import datetime, time, date
from enum import IntEnum
from typing import Optional, List, Any

from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic_core import CoreSchema


class AnimoPet(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    gender: Optional[PetGenderEnum] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[str] = None
    breed_id: Optional[int] = None
    household_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class AnimoPetPaginatedDataResult(BaseModel):
    data: Optional[List[AnimoPet]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class AuthChangePassword(BaseModel):
    user_id: Optional[int] = None
    password: str
    new_password: Optional[str] = None


class AuthLogin(BaseModel):
    client_uid: Optional[str] = None
    device_id: Optional[str] = None
    email_address: str
    password: str


class AuthLogout(BaseModel):
    client_uid: Optional[str] = None
    device_id: Optional[str] = None


class AuthRegister(BaseModel):
    email_address: str
    first_name: str
    last_name: str
    password: str
    language_id: int
    country_id: int
    photo_id: Optional[int] = None
    marketing_opt_in: bool
    weight_units: Optional[UserWeightUnitEnum] = None
    time_format: Optional[UserTimeFormatEnum] = None
    device_id: str


class AuthResetPassword(BaseModel):
    email_address: str
    password: str
    token: str
    client_uid: Optional[str] = None
    device_id: Optional[str] = None


class AuthResetPasswordRequest(BaseModel):
    email_address: str


class AuthToken(BaseModel):
    token: str


class DeviceTag(BaseModel):
    id: int
    device_id: int
    index: int
    profile: Optional[int] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Breed(BaseModel):
    id: Optional[int] = None
    species_id: Optional[int] = None
    name: Optional[str] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class BreedDataResponse(BaseModel):
    data: Optional[Breed] = None


class BreedPaginatedDataResult(BaseModel):
    data: Optional[List[Breed]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class BreedQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    species_id: Optional[int] = None
    lang: Optional[str] = None


class Condition(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ConditionDataResponse(BaseModel):
    data: Optional[Condition] = None


class ConditionPaginatedDataResult(BaseModel):
    data: Optional[List[Condition]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class ConditionQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    lang: Optional[str] = None


class ConsumptionAlert(BaseModel):
    pet_id: int
    tag_id: int
    pet_weight: int
    amount: int
    time_noticed_utc: datetime
    created_at: datetime


class ConsumptionHabit(BaseModel):
    outcome: ConsumptionHabitOutcomeEnum
    calendar_day: date
    amount: int
    lower_limit: Optional[int] = None
    upper_limit: Optional[int] = None
    created_at: datetime


class ConsumptionHabitModelState(BaseModel):
    pet_id: Optional[int] = None
    tag_id: Optional[int] = None
    state: Optional[ConsumptionHabitModelStateEnum] = None


class ConsumptionHabitModelStateEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ConsumptionHabitOutcomeEnum(IntEnum):
    OK = 0
    BELOW_LIMIT = 1
    ABOVE_LIMIT = 2


class Country(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    native_name: Optional[str] = None
    code: Optional[str] = None
    default_language_id: Optional[int] = None
    default_timezone_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CountryDataResponse(BaseModel):
    data: Optional[Country] = None


class CountryPaginatedDataResult(BaseModel):
    data: Optional[List[Country]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class CountryQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    iso_code2: Optional[str] = None
    lang: Optional[str] = None


class CreateHousehold(BaseModel):
    name: str
    timezone_id: int


class CreateHouseholdInvite(BaseModel):
    code: Optional[str] = None
    email_address: str
    owner: bool
    write: bool


class CreatePet(BaseModel):
    name: str
    gender: Optional[PetGenderEnum] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[float] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id2: Optional[int] = None
    spayed: Optional[SpayedEnum] = None
    food_type_id: Optional[int] = None
    photo_id: Optional[int] = None
    species_id: Optional[int] = None
    conditions: Optional[List[Condition]] = None
    household_id: int


class CreatePetPosition(BaseModel):
    where: Optional[PetPositionWhere] = None
    since: Optional[datetime] = None


class CreateUserSettings(BaseModel):
    key: str
    value: str


class Curfew(BaseModel):
    enabled: Optional[bool] = None
    lock_time: Optional[time] = None
    unlock_time: Optional[time] = None


class DeleteAccount(BaseModel):
    password: str
    households: Optional[List[int]] = None


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
    status: Optional[DeviceStatus] = None
    tags: Optional[List[DeviceTag]] = None


class LockMode(IntEnum):
    NONE = 0
    IN = 1
    OUT = 2
    BOTH = 3

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Lock Mode"
        schema["description"] = (
            "Controls the direction of locking:\n"
            "- `0` (NONE): No locking\n"
            "- `1` (IN): Lock inbound only\n"
            "- `2` (OUT): Lock outbound only\n"
            "- `3` (BOTH): Lock both directions"
        )
        return schema


class DeviceControl(BaseModel):
    curfew: Curfew | List[Curfew] | None = None
    fast_polling: Optional[bool] = None
    locking: Optional[LockMode] = None
    led_mode: Optional[int] = None
    pairing_mode: Optional[int] = None


class DeviceControlSchema(BaseModel):
    data: Optional[Any] = None
    pending: Optional[List[DeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceControlPending(BaseModel):
    state: Optional[Any] = None
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


class DeviceControlStateChange(BaseModel):
    request_id: Optional[str] = None
    response_id: Optional[str] = None
    status: Optional[RequestChangeStateResponseStatus] = None
    status_id: Optional[RequestChangeStateResponseStatus] = None
    requested_at: Optional[datetime] = None
    committed_at: Optional[datetime] = None
    device_id: Optional[int] = None
    state: Optional[Any] = None
    requested_by: Optional[int] = None
    child_state_changes: Optional[List[DeviceControlStateChange]] = None
    parent_request_id: Optional[str] = None


class DeviceControlStateChangeDataResponse(BaseModel):
    data: Optional[DeviceControlStateChange] = None


class DeviceControlStateChangeListDataResponse(BaseModel):
    data: Optional[List[DeviceControlStateChange]] = None


class DeviceDataResponse(BaseModel):
    data: Optional[Device] = None


class DeviceIEnumerableDataResponse(BaseModel):
    data: Optional[List[Device]] = None


class DeviceNeedsUpdate(BaseModel):
    needs_manual_update: Optional[bool] = None


class DeviceNeedsUpdateDataResponse(BaseModel):
    data: Optional[DeviceNeedsUpdate] = None


class DevicePaginatedDataResult(BaseModel):
    data: Optional[List[Device]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class DevicePairByCode(BaseModel):
    pairing_code: str


class DeviceReadiness(BaseModel):
    device_ready: Optional[bool] = None
    profiles_available: Optional[int] = None
    profiles_updated_at: Optional[datetime] = None


class DeviceReadinessDataResponse(BaseModel):
    data: Optional[DeviceReadiness] = None


class DeviceStatus(BaseModel):
    led_mode: Optional[int] = None
    pairing_mode: Optional[int] = None
    status: Optional[bool] = None


class DeviceTagData(BaseModel):
    data: Optional[DeviceTag] = None
    pending: Optional[List[DeviceControlPending]] = None
    results: Optional[List[DeviceControlResult]] = None


class DeviceTagDataResponse(BaseModel):
    data: Optional[DeviceTag] = None


class DeviceTagPaginatedDataResult(BaseModel):
    data: Optional[List[DeviceTag]] = None
    meta: Optional[PaginatedMetaDataResult] = None


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


class DrinkingReport(BaseModel):
    datapoints: Optional[List[DrinkingReportDataPoint]] = None


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


class Error(BaseModel):
    success: Optional[bool] = None
    error: Optional[dict] = None


class FeedingReport(BaseModel):
    datapoints: Optional[List[FeedingReportDataPoint]] = None


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


class FoodType(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class FoodTypeDataResponse(BaseModel):
    data: Optional[FoodType] = None


class FoodTypePaginatedDataResult(BaseModel):
    data: Optional[List[FoodType]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class FoodTypeQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    lang: Optional[str] = None


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


class HouseholdDataResponse(BaseModel):
    data: Optional[Household] = None


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


class HouseholdInviteDataResponse(BaseModel):
    data: Optional[HouseholdInvite] = None


class HouseholdInvitePaginatedDataResult(BaseModel):
    data: Optional[List[HouseholdInvite]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class HouseholdInviteStatus(IntEnum):
    PENDING = 0
    ACCEPTED = 1
    EXPIRED = 2


class HouseholdInviteUser(BaseModel):
    creator: Optional[PublicUser] = None
    acceptor: Optional[PublicUser] = None


class HouseholdPaginatedDataResult(BaseModel):
    data: Optional[List[Household]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class HouseholdUser(BaseModel):
    id: int
    owner: Optional[bool] = None
    write: Optional[bool] = None
    user: Optional[PublicUser] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class HouseholdUserDataResponse(BaseModel):
    data: Optional[HouseholdUser] = None


class HouseholdUserPaginatedDataResult(BaseModel):
    data: Optional[List[HouseholdUser]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class Info(BaseModel):
    language: Optional[str] = None
    country: Optional[str] = None


class InfoDataResponse(BaseModel):
    data: Optional[Info] = None


class Invite(BaseModel):
    id: Optional[int] = None
    code: Optional[str] = None
    email_address: Optional[str] = None
    owner: Optional[bool] = None
    write: Optional[bool] = None
    status: Optional[HouseholdInviteStatus] = None
    user: Optional[HouseholdInviteUser] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    used_at: Optional[datetime] = None


class InviteDataResponse(BaseModel):
    data: Optional[Invite] = None


class InvitePaginatedDataResult(BaseModel):
    data: Optional[List[Invite]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class Language(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    native_name: Optional[str] = None
    code: Optional[str] = None
    enabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class LanguageDataResponse(BaseModel):
    data: Optional[Language] = None


class LanguagePaginatedDataResult(BaseModel):
    data: Optional[List[Language]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class MeStart(BaseModel):
    devices: Optional[List[Device]] = None
    households: Optional[List[Household]] = None
    pets: Optional[List[Pet]] = None
    photos: Optional[List[Photo]] = None
    tags: Optional[List[Tag]] = None
    user: Optional[User] = None
    segments: Optional[List[str]] = None


class MeStartDataResponse(BaseModel):
    data: Optional[MeStart] = None


class Movement(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None
    user_id: Optional[int] = None
    direction: Optional[DoorDirectionEnum] = None
    side: Optional[DoorSide] = None
    type: Optional[DoorStatusEnum] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class MovementReport(BaseModel):
    datapoints: Optional[List[MovementReportDataPoint]] = None


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


class Notification(BaseModel):
    id: Optional[int] = None
    type: Optional[TimelineEventType] = None
    text: Optional[str] = None
    created_at: Optional[datetime] = None


class NotificationPaginatedDataResult(BaseModel):
    data: Optional[List[Notification]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class ObjectDataResponse(BaseModel):
    data: Optional[Any] = None


class PaginatedMetaDataResult(BaseModel):
    page: Optional[int] = None
    page_size: Optional[int] = None
    count: Optional[int] = None
    total_pages: Optional[int] = None


class Pet(BaseModel):
    id: int
    name: Optional[str] = None
    gender: Optional[PetGenderEnum] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[str] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id2: Optional[int] = None
    food_type_id: Optional[int] = None
    household_id: Optional[int] = None
    photo_id: Optional[int] = None
    species_id: Optional[int] = None
    spayed: Optional[SpayedEnum] = None
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


class PetCondition(BaseModel):
    id: int
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PetConditionDataResponse(BaseModel):
    data: Optional[PetCondition] = None


class PetConditionPaginatedDataResult(BaseModel):
    data: Optional[List[PetCondition]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class PetConsumption(BaseModel):
    total_consumption: Optional[float] = None
    date: Optional[datetime] = None


class PetConsumptionStatus(BaseModel):
    id: int
    tag_id: Optional[int] = None
    device_id: Optional[int] = None
    change: Optional[List[float]] = None
    at: Optional[datetime] = None


class PetDashboard(BaseModel):
    pet_id: Optional[int] = None
    movement: Optional[PetMovement] = None
    drinking: Optional[PetConsumption] = None
    feeding: Optional[PetConsumption] = None
    drinking_habit: Optional[ConsumptionHabit] = None
    drinking_alert: Optional[ConsumptionAlert] = None
    habit_model_state: Optional[ConsumptionHabitModelState] = None


class PetDashboardListDataResponse(BaseModel):
    data: Optional[List[PetDashboard]] = None


class PetDashboardQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    pet_id: List[int]
    from_: datetime = Field(alias='from')
    days_history: Optional[int] = None


class PetDataResponse(BaseModel):
    data: Optional[Pet] = None


class PetGenderEnum(IntEnum):
    FEMALE = 0
    MALE = 1


class PetInsight(BaseModel):
    pet_id: Optional[int] = None
    drinking_habit: Optional[ConsumptionHabit] = None
    drinking_alert: Optional[ConsumptionAlert] = None
    habit_model_state: Optional[ConsumptionHabitModelState] = None


class PetInsightDataResponse(BaseModel):
    data: Optional[PetInsight] = None


class PetInsightQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None


class PetMovement(BaseModel):
    date: Optional[datetime] = None
    time_outside: Optional[str] = None


class PetPaginatedDataResult(BaseModel):
    data: Optional[List[Pet]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class PetPosition(BaseModel):
    id: int
    pet_id: Optional[int] = None
    tag_id: Optional[int] = None
    device_id: Optional[int] = None
    user_id: Optional[int] = None
    where: Optional[PetPositionWhere] = None
    since: Optional[datetime] = None


class PetPositionDataResponse(BaseModel):
    data: Optional[PetPosition] = None


class PetPositionPaginatedDataResult(BaseModel):
    data: Optional[List[PetPosition]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class PetPositionWhere(IntEnum):
    UNKNOWN = 0
    INSIDE = 1
    OUTSIDE = 2


class PetReport(BaseModel):
    movement: MovementReport
    feeding: FeedingReport
    drinking: DrinkingReport

    consumption_habit: Optional[List[ConsumptionHabit]] = None
    consumption_alert: Optional[List[ConsumptionAlert]] = None


class PetStatus(BaseModel):
    pet_id: Optional[int] = None
    activity: Optional[PetPosition] = None
    feeding: Optional[PetConsumptionStatus] = None
    drinking: Optional[PetConsumptionStatus] = None


class PetStatusDataResponse(BaseModel):
    data: Optional[PetStatus] = None


class PetStatusPaginatedDataResult(BaseModel):
    data: Optional[List[PetStatus]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class Photo(BaseModel):
    id: int
    title: Optional[str] = None
    location: Optional[str] = None
    hash: Optional[str] = None
    uploading_user_id: Optional[int] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PhotoDataResponse(BaseModel):
    data: Optional[Photo] = None


class PhotoPaginatedDataResult(BaseModel):
    data: Optional[List[Photo]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class ProblemDetails(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    status: Optional[int] = None
    detail: Optional[str] = None
    instance: Optional[str] = None


class Product(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProductDataResponse(BaseModel):
    data: Optional[Product] = None


class ProductPaginatedDataResult(BaseModel):
    data: Optional[List[Product]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class ProductQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    lang: Optional[str] = None


class PublicUser(BaseModel):
    id: int
    name: Optional[str] = None
    photo_id: Optional[int] = None
    photo: Optional[Photo] = None


class PublicUserDataResponse(BaseModel):
    data: Optional[PublicUser] = None


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


class ReportHouseholdListDataResponse(BaseModel):
    data: Optional[List[ReportHousehold]] = None


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


class ReportHouseholdQuery(BaseModel):
    from_: Optional[datetime] = Field(default=None, alias='from')
    to: Optional[datetime] = None


class ReportWeightFrame(BaseModel):
    index: Optional[int] = None
    weight: float
    change: float
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


class SpayedEnum(IntEnum):
    UNKNOWN = 0
    YES = 1
    NO = 2


class SpecialProfiles(IntEnum):
    SPECIAL_PROFILE_0 = 0
    SPECIAL_PROFILE_1 = 1
    SPECIAL_PROFILE_2 = 2
    SPECIAL_PROFILE_3 = 3
    SPECIAL_PROFILE_4 = 4
    SPECIAL_PROFILE_5 = 5
    SPECIAL_PROFILE_6 = 6


class Species(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class SpeciesDataResponse(BaseModel):
    data: Optional[Species] = None


class SpeciesPaginatedDataResult(BaseModel):
    data: Optional[List[Species]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class SpeciesQuery(BaseModel):
    page: Optional[int] = None
    items_per_page: Optional[int] = None
    page_size: Optional[int] = None
    lang: Optional[str] = None


class Start(BaseModel):
    breed: Optional[List[Breed]] = None
    condition: Optional[List[Condition]] = None
    country: Optional[List[Country]] = None
    language: Optional[List[Language]] = None
    product: Optional[List[Product]] = None
    timezone: Optional[List[Timezone]] = None


class StartDataResponse(BaseModel):
    data: Optional[Start] = None


class StartQuery(BaseModel):
    lang: Optional[str] = None


class SubstanceTypesEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class Tag(BaseModel):
    id: int
    tag: Optional[str] = None
    supported_product_ids: Optional[List[DeviceType]] = None
    incompatible_product_ids: Optional[List[DeviceType]] = None
    version: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class TagDataResponse(BaseModel):
    data: Optional[Tag] = None


class TagDevice(BaseModel):
    id: Optional[int] = None
    index: Optional[int] = None
    profile: Optional[int] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TagDeviceDataResponse(BaseModel):
    data: Optional[TagDevice] = None


class TagDevicePaginatedDataResult(BaseModel):
    data: Optional[List[TagDevice]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class TagPaginatedDataResult(BaseModel):
    data: Optional[List[Tag]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class Timeline(BaseModel):
    id: Optional[int] = None
    type: Optional[int] = None
    data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    households: Optional[List[Household]] = None
    devices: Optional[List[Device]] = None
    movements: Optional[List[Movement]] = None
    pets: Optional[List[Pet]] = None
    tags: Optional[List[Tag]] = None
    users: Optional[List[PublicUser]] = None
    weights: Optional[List[Weight]] = None


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


class TimelinePaginatedDataResult(BaseModel):
    data: Optional[List[Timeline]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class Timezone(BaseModel):
    id: int
    name: Optional[str] = None
    timezone: Optional[str] = None
    utc_offset: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TimezoneDataResponse(BaseModel):
    data: Optional[Timezone] = None


class TimezonePaginatedDataResult(BaseModel):
    data: Optional[List[Timezone]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class UpdateDevice(BaseModel):
    name: str


class UpdateDeviceTag(BaseModel):
    profile: Optional[SpecialProfiles] = None


class UpdateHousehold(BaseModel):
    name: Optional[str] = None
    timezone_id: Optional[int] = None


class UpdateHouseholdInvite(BaseModel):
    owner: Optional[bool] = None
    write: Optional[bool] = None


class UpdateHouseholdUser(BaseModel):
    owner: Optional[bool] = None
    write: Optional[bool] = None


class UpdateMe(BaseModel):
    email_address: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    language_id: Optional[int] = None
    country_id: Optional[int] = None
    photo_id: Optional[int] = None
    marketing_opt_in: Optional[bool] = None
    weight_units: Optional[UserWeightUnitEnum] = None
    time_format: Optional[UserTimeFormatEnum] = None
    notifications: Optional[dict] = None
    password: Optional[str] = None


class UpdatePet(BaseModel):
    name: str
    gender: Optional[PetGenderEnum] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[float] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id2: Optional[int] = None
    spayed: Optional[SpayedEnum] = None
    food_type_id: Optional[int] = None
    photo_id: Optional[int] = None
    species_id: Optional[int] = None
    conditions: Optional[List[Condition]] = None


class UpdatePhoto(BaseModel):
    title: Optional[str] = None


class UpdateUserSettings(BaseModel):
    value: str


class User(BaseModel):
    id: Optional[int] = None
    email_address: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    country_id: Optional[int] = None
    language_id: Optional[int] = None
    photo_id: Optional[int] = None
    marketing_opt_in: Optional[bool] = None
    terms_accepted: Optional[datetime] = None
    weight_units: Optional[int] = None
    time_format: Optional[int] = None
    notifications: Optional[dict] = None
    photo: Optional[Photo] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    use_colour: Optional[str] = None
    segments: Optional[List[str]] = None


class UserClient(BaseModel):
    platform: Optional[UserClientPlatform] = None
    token: Optional[str] = None


class UserClientDataResponse(BaseModel):
    data: Optional[UserClient] = None


class UserClientPaginatedDataResult(BaseModel):
    data: Optional[List[UserClient]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class UserClientPlatform(BaseModel):
    app: Optional[UserClientPlatformApp] = None
    device: Optional[UserClientPlatformDevice] = None
    locale: Optional[UserClientPlatformLocale] = None


class UserClientPlatformApp(BaseModel):
    bundle_identifier: Optional[str] = None
    version: Optional[str] = None


class UserClientPlatformDevice(BaseModel):
    name: Optional[str] = None
    model: Optional[UserClientPlatformDeviceModel] = None
    uuid: Optional[str] = None
    os: Optional[UserClientPlatformDeviceOs] = None


class UserClientPlatformDeviceModel(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    version: Optional[str] = None


class UserClientPlatformDeviceOs(BaseModel):
    platform: Optional[str] = None
    version: Optional[str] = None


class UserClientPlatformLocale(BaseModel):
    language: Optional[str] = None
    country: Optional[str] = None


class UserDataResponse(BaseModel):
    data: Optional[User] = None


class UserSetting(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    key: Optional[str] = None
    value: Optional[str] = None
    version: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserSettingDataResponse(BaseModel):
    data: Optional[UserSetting] = None


class UserSettingPaginatedDataResult(BaseModel):
    data: Optional[List[UserSetting]] = None
    meta: Optional[PaginatedMetaDataResult] = None


class UserTimeFormatEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class UserWeightUnitEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


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
