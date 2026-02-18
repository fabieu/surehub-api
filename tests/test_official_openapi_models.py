import json
from pathlib import Path

import pytest

from surehub_api.entities import official, official_v2


@pytest.mark.parametrize(
    ("module", "spec_path"),
    [
        (official, Path(__file__).resolve().parents[1] / "resources" / "swagger_v1.json"),
        (official_v2, Path(__file__).resolve().parents[1] / "resources" / "swagger_v2.json"),
    ],
)
def test_official_modules_include_all_openapi_schema_definitions(module, spec_path):
    spec = json.loads(spec_path.read_text())
    schema_names = (
        schema_name[:-8] if schema_name.endswith("Resource") else schema_name
        for schema_name in spec["components"]["schemas"].keys()
    )

    missing_schema_models = [schema_name for schema_name in schema_names if not hasattr(module, schema_name)]

    assert missing_schema_models == []


@pytest.mark.parametrize("module", [official, official_v2])
def test_official_modules_do_not_expose_resource_suffixed_models(module):
    class_names = [name for name, value in vars(module).items() if isinstance(value, type)]
    resource_suffixed_class_names = [name for name in class_names if name.endswith("Resource")]

    assert resource_suffixed_class_names == []
