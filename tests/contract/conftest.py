from dataclasses import dataclass
from typing import List, Optional

import pytest
from dynaconf.validator import ValidationError

from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.services import api
from surehub_api.utils import response_handler


def credentials_configured() -> bool:
    try:
        return bool(settings.email) and bool(settings.password)
    except ValidationError:
        return False


@dataclass
class ApiContext:
    household_id: Optional[int] = None
    user_id: Optional[int] = None
    pet_id: Optional[int] = None
    device_id: Optional[int] = None
    tag_id: Optional[int] = None


def pytest_addoption(parser):
    parser.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Write current API response shapes to snapshot files instead of comparing against them.",
    )


@pytest.fixture(scope="session")
def update_snapshots(request) -> bool:
    return request.config.getoption("--update-snapshots")


@pytest.fixture(scope="session")
def api_context() -> ApiContext:
    """Discover real ids from the configured account to exercise parameterized endpoints."""

    ctx = ApiContext()

    households = response_handler.parse(
        api.get(f"{settings.endpoint}/api/household"), model=List[official.Household]
    )
    if not households:
        return ctx

    ctx.household_id = households[0].id

    users = response_handler.parse(
        api.get(f"{settings.endpoint}/api/household/{ctx.household_id}/user"),
        model=List[official.HouseholdUser],
    )
    if users:
        ctx.user_id = users[0].id

    pets = response_handler.parse(
        api.get(f"{settings.endpoint}/api/household/{ctx.household_id}/pet"),
        model=List[official.Pet],
    )
    if pets:
        ctx.pet_id = pets[0].id

    devices = response_handler.parse(
        api.get(f"{settings.endpoint}/api/household/{ctx.household_id}/device"),
        model=List[official.Device],
    )
    if devices:
        ctx.device_id = devices[0].id

        tags = response_handler.parse(
            api.get(f"{settings.endpoint}/api/device/{ctx.device_id}/tag"),
            model=List[official.DeviceTag],
        )
        if tags:
            ctx.tag_id = tags[0].id

    return ctx
