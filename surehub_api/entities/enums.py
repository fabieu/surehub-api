from __future__ import annotations

from enum import IntEnum
from typing import Any

from pydantic import GetJsonSchemaHandler
from pydantic_core import CoreSchema


class ConsumptionHabitModelState(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class ConsumptionHabitOutcome(IntEnum):
    OK = 0
    BELOW_LIMIT = 1
    ABOVE_LIMIT = 2

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Consumption Habit Outcome"
        schema["description"] = (
            "Outcome of a consumption habit evaluation:\n"
            "- `0` (OK): Within normal range\n"
            "- `1` (BELOW_LIMIT): Below the expected limit\n"
            "- `2` (ABOVE_LIMIT): Above the expected limit"
        )
        return schema


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

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Device Type"
        schema["description"] = (
            "Type of Sure Petcare device:\n"
            "- `0` (UNKNOWN_DEVICE_0): Unknown device\n"
            "- `1` (HUB): Hub\n"
            "- `2` (REPEATER): Repeater\n"
            "- `3` (PET_DOOR_CONNECT): Pet Door Connect\n"
            "- `4` (PET_FEEDER_CONNECT): Pet Feeder Connect\n"
            "- `5` (PROGRAMMER): Programmer\n"
            "- `6` (DUALSCAN_CAT_FLAP_CONNECT): DualScan Cat Flap Connect\n"
            "- `7` (MICROCHIP_FEEDER): Microchip Feeder\n"
            "- `8` (FELAQUA_CONNECT): Felaqua Connect (Poseidon)\n"
            "- `9` (CAT_FLAP_CONNECT): Cat Flap Connect\n"
            "- `10` (DUALSCAN_PET_DOOR_CONNECT): DualScan Pet Door Connect\n"
            "- `32` (DOG_BOWL_CONNECT): Dog Bowl Connect (Cerberus)\n"
            "- `255` (UNKNOWN_DEVICE_255): Unknown device"
        )
        return schema


class DoorDirection(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class DoorSide(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DoorStatus(IntEnum):
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_8 = 8
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13


class HouseholdInviteStatus(IntEnum):
    PENDING = 0
    ACCEPTED = 1
    EXPIRED = 2

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Household Invite Status"
        schema["description"] = (
            "Status of a household invitation:\n"
            "- `0` (PENDING): Invitation is pending\n"
            "- `1` (ACCEPTED): Invitation has been accepted\n"
            "- `2` (EXPIRED): Invitation has expired"
        )
        return schema


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


class PetGender(IntEnum):
    FEMALE = 0
    MALE = 1

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Pet Gender"
        schema["description"] = (
            "Gender of the pet:\n"
            "- `0` (FEMALE): Female\n"
            "- `1` (MALE): Male"
        )
        return schema


class PetPositionWhere(IntEnum):
    UNKNOWN = 0
    INSIDE = 1
    OUTSIDE = 2

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Pet Position"
        schema["description"] = (
            "Where the pet is located:\n"
            "- `0` (UNKNOWN): Unknown position\n"
            "- `1` (INSIDE): Inside the house\n"
            "- `2` (OUTSIDE): Outside the house"
        )
        return schema


class RequestChangeStateResponseStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class Spayed(IntEnum):
    UNKNOWN = 0
    YES = 1
    NO = 2

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Spayed/Neutered Status"
        schema["description"] = (
            "Whether the pet has been spayed or neutered:\n"
            "- `0` (UNKNOWN): Unknown\n"
            "- `1` (YES): Spayed/neutered\n"
            "- `2` (NO): Not spayed/neutered"
        )
        return schema


class SpecialProfiles(IntEnum):
    SPECIAL_PROFILE_0 = 0
    SPECIAL_PROFILE_1 = 1
    SPECIAL_PROFILE_2 = 2
    SPECIAL_PROFILE_3 = 3
    SPECIAL_PROFILE_4 = 4
    SPECIAL_PROFILE_5 = 5
    SPECIAL_PROFILE_6 = 6


class SubstanceTypes(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


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


class UserTimeFormat(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class UserWeightUnit(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class ChangeProfileAction(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DeviceTagProfiles(IntEnum):
    DISABLED = 2
    ENABLED = 3

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        schema = handler(core_schema)
        schema["title"] = "Device Tag Profile"
        schema["description"] = (
            "Profile setting for a device tag:\n"
            "- `2` (DISABLED): Tag profile disabled\n"
            "- `3` (ENABLED): Tag profile enabled"
        )
        return schema


class DualScanLockingMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class FailSafeOptions(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1


class FeederBowlType(IntEnum):
    VALUE_1 = 1
    VALUE_4 = 4
    VALUE_5 = 5


class FoodTypes(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class LedMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_128 = 128


class PairingMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_128 = 128


class PetDoorLockingMode(IntEnum):
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


class ReportHouseholdEvent(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


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


class ZeroAction(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
