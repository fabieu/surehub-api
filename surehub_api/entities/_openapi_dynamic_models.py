from __future__ import annotations

import json
import keyword
import re
from datetime import date, datetime, time
from enum import Enum, IntEnum
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, create_model


def _sanitize_identifier(name: str) -> str:
    identifier = re.sub(r"\W", "_", name)
    if not identifier:
        identifier = "value"
    if identifier[0].isdigit():
        identifier = f"value_{identifier}"
    if keyword.iskeyword(identifier):
        identifier = f"{identifier}_"
    return identifier


def _enum_member_name(value: Any) -> str:
    if isinstance(value, str):
        member = _sanitize_identifier(value).upper()
    else:
        member = f"VALUE_{str(value).replace('-', 'NEGATIVE_')}"
    if not member or member == "_":
        member = "VALUE"
    if member[0].isdigit():
        member = f"VALUE_{member}"
    return member


def _schema_to_type(schema: dict[str, Any], module_globals: dict[str, Any]) -> type[Any] | Any:
    if "$ref" in schema:
        reference_name = schema["$ref"].rsplit("/", maxsplit=1)[-1]
        return module_globals.get(reference_name, Any)

    schema_type = schema.get("type")
    if schema_type == "integer":
        return int
    if schema_type == "number":
        return float
    if schema_type == "boolean":
        return bool
    if schema_type == "string":
        schema_format = schema.get("format")
        if schema_format == "date-time":
            return datetime
        if schema_format == "date":
            return date
        if schema_format == "time":
            return time
        return str
    if schema_type == "array":
        item_type = _schema_to_type(schema.get("items", {}), module_globals)
        return list[item_type]
    if schema_type == "object":
        return dict[str, Any]

    return Any


def populate_missing_openapi_models(module_globals: dict[str, Any], spec_path: Path) -> None:
    spec = json.loads(spec_path.read_text())
    schemas = spec.get("components", {}).get("schemas", {})

    for schema_name, schema in schemas.items():
        if schema_name in module_globals:
            continue

        if "enum" in schema:
            enum_values = schema["enum"]
            base_enum = IntEnum if all(isinstance(v, int) for v in enum_values) else Enum
            members: dict[str, Any] = {}

            for index, value in enumerate(enum_values):
                member_name = _enum_member_name(value)
                if member_name in members:
                    member_name = f"{member_name}_{index}"
                members[member_name] = value

            module_globals[schema_name] = base_enum(schema_name, members)
            continue

        properties = schema.get("properties", {})
        required_fields = set(schema.get("required", []))
        field_definitions: dict[str, tuple[Any, Any]] = {}

        for property_name, property_schema in properties.items():
            field_name = _sanitize_identifier(property_name)
            is_required = property_name in required_fields and not property_schema.get("nullable")
            resolved_type = _schema_to_type(property_schema, module_globals)
            annotation = resolved_type if is_required else Optional[resolved_type]
            default: Any = ... if is_required else None

            if field_name != property_name:
                default = Field(default=default, alias=property_name)

            if field_name in field_definitions:
                field_name = f"{field_name}_field"

            field_definitions[field_name] = (annotation, default)

        module_globals[schema_name] = create_model(schema_name, __base__=BaseModel, **field_definitions)
