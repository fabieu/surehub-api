from tests.contract.shape import compute_shape, diff_shapes


def test_compute_shape_scalars():
    assert compute_shape("foo") == ["string"]
    assert compute_shape(42) == ["integer"]
    assert compute_shape(4.2) == ["number"]
    assert compute_shape(True) == ["boolean"]
    assert compute_shape(None) == ["null"]


def test_compute_shape_object():
    assert compute_shape({"id": 1, "name": "Bob"}) == {
        "object": {"id": ["integer"], "name": ["string"]}
    }


def test_compute_shape_array_merges_item_shapes():
    shape = compute_shape([{"id": 1, "name": "Bob"}, {"id": 2, "name": None}])

    assert shape == {
        "array": {"object": {"id": ["integer"], "name": ["null", "string"]}}
    }


def test_compute_shape_empty_array():
    assert compute_shape([]) == {"array": None}


def test_diff_shapes_no_changes():
    shape = compute_shape({"id": 1, "name": "Bob"})
    assert diff_shapes(shape, shape) == []


def test_diff_shapes_detects_added_field():
    old = compute_shape({"id": 1})
    new = compute_shape({"id": 1, "name": "Bob"})

    diffs = diff_shapes(old, new)

    assert diffs == ["added field: $.name (string)"]


def test_diff_shapes_detects_removed_field():
    old = compute_shape({"id": 1, "name": "Bob"})
    new = compute_shape({"id": 1})

    diffs = diff_shapes(old, new)

    assert diffs == ["removed field: $.name (string)"]


def test_diff_shapes_detects_renamed_field_as_add_and_remove():
    old = compute_shape({"pet_name": "Bob"})
    new = compute_shape({"name": "Bob"})

    diffs = diff_shapes(old, new)

    assert sorted(diffs) == [
        "added field: $.name (string)",
        "removed field: $.pet_name (string)",
    ]


def test_diff_shapes_detects_type_change():
    old = compute_shape({"weight": "12.3"})
    new = compute_shape({"weight": 12.3})

    diffs = diff_shapes(old, new)

    assert sorted(diffs) == [
        "type added at $.weight: ['number']",
        "type removed at $.weight: ['string']",
    ]


def test_diff_shapes_detects_object_vs_array_change():
    old = compute_shape({"control": {"locking": 1}})
    new = compute_shape({"control": [{"locking": 1}]})

    diffs = diff_shapes(old, new)

    assert diffs == ["shape changed at $.control: object -> array"]


def test_diff_shapes_detects_nested_changes_inside_arrays():
    old = compute_shape({"pets": [{"id": 1, "name": "Bob"}]})
    new = compute_shape({"pets": [{"id": 1}]})

    diffs = diff_shapes(old, new)

    assert diffs == ["removed field: $.pets[].name (string)"]


def test_diff_shapes_ignores_empty_arrays():
    old = compute_shape({"pets": []})
    new = compute_shape({"pets": [{"id": 1}]})

    assert diff_shapes(old, new) == []
    assert diff_shapes(new, old) == []
