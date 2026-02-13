from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from surehub_api.entities import official
from surehub_api.utils import http_utils


class FakeResponse:
    def __init__(self, status_code: int, payload: dict, text: str = ""):
        self.status_code = status_code
        self.ok = 200 <= status_code < 300
        self._payload = payload
        self.text = text
        self.request = SimpleNamespace(method="GET", url="https://example.test/resource")

    def json(self):
        return self._payload


def test_extract_response_data_validates_pydantic_model():
    response = FakeResponse(200, {"data": {"id": 1, "version": 1}})

    result = http_utils.extract_response_data(response, model=official.Pet)

    assert isinstance(result, official.Pet)
    assert result.id == 1


def test_raise_for_status_logs_with_expected_levels(caplog):
    ok_response = FakeResponse(200, {"data": {}})
    error_response = FakeResponse(404, {"error": "missing"}, text="missing")

    with caplog.at_level("INFO"):
        http_utils.raise_for_status(ok_response)

    with pytest.raises(HTTPException):
        with caplog.at_level("ERROR"):
            http_utils.raise_for_status(error_response)

    assert "returned 200" in caplog.text
    assert "returned 404" in caplog.text
