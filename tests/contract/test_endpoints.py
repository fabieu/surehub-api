"""Live contract tests against the real Sure Petcare API.

For every read-only endpoint of the upstream API used by this project, these tests:

1. Call the upstream endpoint with the configured account's credentials.
2. Validate the response against the corresponding Pydantic model (catches breaking
   type/required-field changes - the same check performed at request time by
   ``response_handler.parse``).
3. Compare the *structural shape* of the raw response against a committed snapshot
   in ``tests/contract/snapshots/`` to detect added, removed, or renamed fields -
   changes that Pydantic alone would silently ignore.

Run with ``--update-snapshots`` to (re)write the snapshot files after a reviewed and
accepted upstream change. Requires ``SUREHUB_EMAIL``/``SUREHUB_PASSWORD`` to be set;
otherwise all tests in this module are skipped.
"""

import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, List, Optional

import pytest
from pydantic import TypeAdapter

from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.services import api
from surehub_api.utils import response_handler
from tests.contract.conftest import ApiContext, credentials_configured
from tests.contract.shape import compute_shape, diff_shapes

pytestmark = [
    pytest.mark.contract,
    pytest.mark.skipif(
        not credentials_configured(),
        reason="SUREHUB_EMAIL/SUREHUB_PASSWORD not configured; skipping live contract tests",
    ),
]

SNAPSHOTS_DIR = Path(__file__).parent / "snapshots"


@dataclass
class EndpointSpec:
    name: str
    path: Callable[[ApiContext], str]
    model: Any
    requires: tuple = ()
    params: Optional[Callable[[ApiContext], dict]] = None


def _report_params(_ctx: ApiContext) -> dict:
    now = datetime.now(timezone.utc)
    return {"From": (now - timedelta(days=7)).isoformat(), "To": now.isoformat()}


ENDPOINT_SPECS = [
    EndpointSpec("dashboard_me_start", lambda ctx: "/api/me/start", official.MeStart),
    EndpointSpec("pets_list", lambda ctx: "/api/pet", List[official.Pet]),
    EndpointSpec("pet_by_id", lambda ctx: f"/api/pet/{ctx.pet_id}", official.Pet, requires=("pet_id",)),
    EndpointSpec("devices_list", lambda ctx: "/api/device", List[official.Device]),
    EndpointSpec(
        "device_by_id", lambda ctx: f"/api/device/{ctx.device_id}", official.Device, requires=("device_id",)
    ),
    EndpointSpec(
        "device_control",
        lambda ctx: f"/api/device/{ctx.device_id}/control",
        official.DeviceControl,
        requires=("device_id",),
    ),
    EndpointSpec(
        "device_tags",
        lambda ctx: f"/api/device/{ctx.device_id}/tag",
        List[official.DeviceTag],
        requires=("device_id",),
    ),
    EndpointSpec(
        "device_tag_by_id",
        lambda ctx: f"/api/device/{ctx.device_id}/tag/{ctx.tag_id}",
        official.DeviceTag,
        requires=("device_id", "tag_id"),
    ),
    EndpointSpec("households_list", lambda ctx: "/api/household", List[official.Household]),
    EndpointSpec(
        "household_by_id",
        lambda ctx: f"/api/household/{ctx.household_id}",
        official.Household,
        requires=("household_id",),
    ),
    EndpointSpec(
        "household_users",
        lambda ctx: f"/api/household/{ctx.household_id}/user",
        List[official.HouseholdUser],
        requires=("household_id",),
    ),
    EndpointSpec(
        "household_user_by_id",
        lambda ctx: f"/api/household/{ctx.household_id}/user/{ctx.user_id}",
        official.HouseholdUser,
        requires=("household_id", "user_id"),
    ),
    EndpointSpec(
        "household_pets",
        lambda ctx: f"/api/household/{ctx.household_id}/pet",
        List[official.Pet],
        requires=("household_id",),
    ),
    EndpointSpec(
        "household_pet_by_id",
        lambda ctx: f"/api/household/{ctx.household_id}/pet/{ctx.pet_id}",
        official.Pet,
        requires=("household_id", "pet_id"),
    ),
    EndpointSpec(
        "household_devices",
        lambda ctx: f"/api/household/{ctx.household_id}/device",
        List[official.Device],
        requires=("household_id",),
    ),
    EndpointSpec(
        "household_device_by_id",
        lambda ctx: f"/api/household/{ctx.household_id}/device/{ctx.device_id}",
        official.Device,
        requires=("household_id", "device_id"),
    ),
    EndpointSpec(
        "household_pet_report",
        lambda ctx: f"/api/v2/report/household/{ctx.household_id}/pet/{ctx.pet_id}/aggregate",
        official.PetReport,
        requires=("household_id", "pet_id"),
        params=_report_params,
    ),
]


@pytest.mark.parametrize("spec", ENDPOINT_SPECS, ids=lambda spec: spec.name)
def test_endpoint_contract(spec: EndpointSpec, api_context: ApiContext, update_snapshots: bool):
    for field in spec.requires:
        if getattr(api_context, field) is None:
            pytest.skip(f"No {field} discovered in this account; cannot test '{spec.name}'")

    uri = f"{settings.endpoint}{spec.path(api_context)}"
    params = spec.params(api_context) if spec.params else None

    response = api.get(uri, params=params)
    response_handler.raise_for_status(response)
    payload = response.json()

    assert "data" in payload, f"Response for '{spec.name}' is missing the 'data' key"
    data = payload["data"]

    # Catches breaking type/required-field changes (mirrors response_handler.parse)
    TypeAdapter(spec.model).validate_python(data)

    current_shape = compute_shape(data)
    snapshot_path = SNAPSHOTS_DIR / f"{spec.name}.json"

    if update_snapshots or not snapshot_path.exists():
        snapshot_path.write_text(json.dumps(current_shape, indent=2, sort_keys=True) + "\n")
        if not update_snapshots:
            pytest.fail(
                f"No snapshot found for '{spec.name}'. A baseline was written to "
                f"{snapshot_path} - review it, commit it, then re-run."
            )
        return

    baseline_shape = json.loads(snapshot_path.read_text())
    diffs = diff_shapes(baseline_shape, current_shape)

    assert not diffs, "Detected upstream API schema changes for '{}':\n{}".format(
        spec.name, "\n".join(f"  - {d}" for d in diffs)
    )
