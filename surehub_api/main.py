import json
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse

from surehub_api import __version__
from surehub_api.config import settings
from surehub_api.entities.openapi import Tags
from surehub_api.routers import devices, households, dashboard, pets

# FastAPI configuration
app = FastAPI(
    title="Unofficial SureHub API",
    version=__version__,
    description="SureHub API is a simple, yet powerful RESTful-API for products from [Sure Petcare](https://www.surepetcare.com).",
    license_info={
        "name": "Apache 2.0",
        "identifier": "Apache-2.0",
    },
    openapi_tags=[
        {
            "name": Tags.DASHBOARD,
            "description": "Endpoints used to retrieve aggregated and real-time data for user dashboards, including summaries, metrics, and status overviews."
        },
        {
            "name": Tags.HOUSEHOLD,
            "description": "Endpoints related to household management, including household configuration, users, pets, and associated devices."
        },
        {
            "name": Tags.DEVICE,
            "description": "Endpoints for managing and interacting with devices, including configuration, status, and telemetry."
        },
        {
            "name": Tags.PET,
            "description": "Endpoints related to pets, including location, pet-specific settings and metadata."
        },
    ],
)
app.include_router(devices.router)
app.include_router(households.router)
app.include_router(dashboard.router)
app.include_router(pets.router)


@app.get('/health', include_in_schema=False)
async def health():
    return JSONResponse({"status": "ok", "version": __version__})


# Redirect default url to docs
@app.get('/', include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


def main():
    # CORS
    if settings.cors:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors.split(","),
            allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
            allow_headers=["Content-Type"],
        )

    # Load logging configuration
    log_config = json.loads((Path(__file__).parent / "logging.json").read_text())

    uvicorn.run(
        "surehub_api.main:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.loglevel,
        log_config=log_config,
        reload=settings.debug
    )


if __name__ == '__main__':
    main()
