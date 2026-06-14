"""Structural "shape" extraction and diffing for JSON API responses.

Unlike Pydantic validation - which by default ignores unknown fields and treats
missing ``Optional`` fields as ``None`` - this module fingerprints the *actual*
structure of a JSON value (object keys, array item shapes, scalar types) so that
added, removed, or renamed fields can be detected even when they wouldn't cause a
validation error.

A "shape" is one of:
  - ``{"object": {key: shape, ...}}`` for JSON objects
  - ``{"array": shape | None}`` for JSON arrays (``None`` if the array was empty)
  - ``{"mixed": [description, ...]}`` if a single field/position is observed with
    incompatible composite shapes (e.g. an object in one sample, a list in another)
  - a sorted list of scalar type names, e.g. ``["integer", "null"]``, for scalars
"""

from __future__ import annotations

from typing import Any

Shape = Any

_SCALAR_TYPES = {
    type(None): "null",
    bool: "boolean",
    int: "integer",
    float: "number",
    str: "string",
}


def _scalar_type(value: Any) -> str:
    for python_type, name in _SCALAR_TYPES.items():
        if isinstance(value, python_type):
            return name
    raise TypeError(f"Unsupported scalar type: {type(value)!r}")


def _is_object(shape: Shape) -> bool:
    return isinstance(shape, dict) and "object" in shape


def _is_array(shape: Shape) -> bool:
    return isinstance(shape, dict) and "array" in shape


def _is_mixed(shape: Shape) -> bool:
    return isinstance(shape, dict) and "mixed" in shape


def _describe(shape: Shape) -> str:
    if shape is None:
        return "unknown"
    if _is_object(shape):
        return "object"
    if _is_array(shape):
        return "array"
    if _is_mixed(shape):
        return "mixed(" + ",".join(shape["mixed"]) + ")"
    return "|".join(shape)


def compute_shape(value: Any) -> Shape:
    """Recursively compute the shape of a JSON-decoded value."""

    if isinstance(value, dict):
        return {"object": {key: compute_shape(val) for key, val in value.items()}}

    if isinstance(value, list):
        item_shape: Shape | None = None
        for item in value:
            shape = compute_shape(item)
            item_shape = shape if item_shape is None else merge_shapes(item_shape, shape)
        return {"array": item_shape}

    return [_scalar_type(value)]


def merge_shapes(a: Shape, b: Shape) -> Shape:
    """Merge two shapes observed for the same position (e.g. items of one array)."""

    if a is None:
        return b
    if b is None:
        return a

    if _is_object(a) and _is_object(b):
        keys = set(a["object"]) | set(b["object"])
        return {"object": {key: merge_shapes(a["object"].get(key), b["object"].get(key)) for key in keys}}

    if _is_array(a) and _is_array(b):
        return {"array": merge_shapes(a["array"], b["array"])}

    if isinstance(a, list) and isinstance(b, list):
        return sorted(set(a) | set(b))

    if a == b:
        return a

    return {"mixed": sorted({_describe(a), _describe(b)})}


def diff_shapes(old: Shape, new: Shape, path: str = "$") -> list[str]:
    """Diff two shapes, returning human-readable descriptions of every difference."""

    diffs: list[str] = []

    if _is_object(old) and _is_object(new):
        old_fields = old["object"]
        new_fields = new["object"]

        for key in sorted(set(new_fields) - set(old_fields)):
            diffs.append(f"added field: {path}.{key} ({_describe(new_fields[key])})")

        for key in sorted(set(old_fields) - set(new_fields)):
            diffs.append(f"removed field: {path}.{key} ({_describe(old_fields[key])})")

        for key in sorted(set(old_fields) & set(new_fields)):
            diffs.extend(diff_shapes(old_fields[key], new_fields[key], f"{path}.{key}"))

        return diffs

    if _is_array(old) and _is_array(new):
        # An empty array carries no shape information - nothing to compare.
        if old["array"] is None or new["array"] is None:
            return diffs
        return diff_shapes(old["array"], new["array"], f"{path}[]")

    if isinstance(old, list) and isinstance(new, list):
        added = sorted(set(new) - set(old))
        removed = sorted(set(old) - set(new))

        if added:
            diffs.append(f"type added at {path}: {added}")
        if removed:
            diffs.append(f"type removed at {path}: {removed}")

        return diffs

    if old != new:
        diffs.append(f"shape changed at {path}: {_describe(old)} -> {_describe(new)}")

    return diffs
