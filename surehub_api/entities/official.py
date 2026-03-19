from __future__ import annotations

from datetime import datetime, time, date
from typing import Optional, List, Any

from pydantic import BaseModel, Field

from surehub_api.entities.enums import (
    ConsumptionHabitModelState,
    ConsumptionHabitOutcome,
    DeviceType,
    DoorDirection,
    DoorSide,
    DoorStatus,
    HouseholdInviteStatus,
    LockMode,
    PetGender,
    PetPositionWhere,
    RequestChangeStateResponseStatus,
    Spayed,
    SpecialProfiles,
    SubstanceTypes,
    TimelineEventType,
    UserTimeFormat,
    UserWeightUnit,
)


class AnimoPet(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    gender: Optional[PetGender] = None
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
    weight_units: Optional[UserWeightUnit] = None
    time_format: Optional[UserTimeFormat] = None
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
    outcome: ConsumptionHabitOutcome
    calendar_day: date
    amount: int
    lower_limit: Optional[int] = None
    upper_limit: Optional[int] = None
    created_at: datetime


class ConsumptionHabitModelState(BaseModel):
    pet_id: Optional[int] = None
    tag_id: Optional[int] = None
    state: Optional[ConsumptionHabitModelState] = None


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
    gender: Optional[PetGender] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[float] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id2: Optional[int] = None
    spayed: Optional[Spayed] = None
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


# TODO: Add descriptive names to numeric special profiles


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
    direction: Optional[DoorDirection] = None
    side: Optional[DoorSide] = None
    type: Optional[DoorStatus] = None
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
    gender: Optional[PetGender] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[str] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id2: Optional[int] = None
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


class PetConsumptionOverview(BaseModel):
    date: Optional[datetime] = None
    last_consumption: Optional[datetime] = None
    substance_type: Optional[SubstanceTypes] = None
    total_consumption: Optional[float] = None
    number_of_visits: Optional[int] = None
    consumption_time: Optional[int] = None
    activity: Optional[List[PetConsumption]] = None
    device_ids: Optional[List[int]] = None


class PetConsumptionStatus(BaseModel):
    id: int
    tag_id: Optional[int] = None
    device_id: Optional[int] = None
    change: Optional[List[float]] = None
    at: Optional[datetime] = None


class PetDashboard(BaseModel):
    pet_id: Optional[int] = None
    movement: Optional[PetMovementOverview] = None
    drinking: Optional[PetConsumptionOverview] = None
    feeding: Optional[PetConsumptionOverview] = None
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


class PetMovementOverview(BaseModel):
    date: Optional[datetime] = None
    where: Optional[DoorDirection] = None
    time_outside: Optional[str] = None
    since: Optional[datetime] = None
    last_entry: Optional[datetime] = None
    trips_outside: Optional[int] = None
    entries: Optional[int] = None
    time_outside_in_seconds: Optional[int] = None
    activity: Optional[List[PetMovement]] = None
    device_ids: Optional[List[int]] = None


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
    weight_units: Optional[UserWeightUnit] = None
    time_format: Optional[UserTimeFormat] = None
    notifications: Optional[dict] = None
    password: Optional[str] = None


class UpdatePet(BaseModel):
    name: str
    gender: Optional[PetGender] = None
    date_of_birth: Optional[datetime] = None
    weight: Optional[float] = None
    comments: Optional[str] = None
    breed_id: Optional[int] = None
    breed_id2: Optional[int] = None
    spayed: Optional[Spayed] = None
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
