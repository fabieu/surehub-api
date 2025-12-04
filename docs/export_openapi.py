import json
from pathlib import Path

from surehub_api.main import app

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "public" / "openapi.json"

with open(OPENAPI_PATH, "w") as f:
    f.write(json.dumps(app.openapi()))
