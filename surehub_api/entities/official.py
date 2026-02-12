from datetime import datetime, time, date
from enum import IntEnum
from typing import Optional, List

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
    FELAQUA_CONNECT = 8 # Poseidon
    CAT_FLAP_CONNECT = 9
    DUALSCAN_PET_DOOR_CONNECT = 10
    DOG_BOWL_CONNECT = 32 # Cerberus
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
