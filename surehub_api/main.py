import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
        {"name": Tags.DASHBOARD, "description": ""},
        {"name": Tags.HOUSEHOLD, "description": ""},
        {"name": Tags.DEVICE, "description": ""},
        {"name": Tags.PET, "description": ""},
    ]
)
app.include_router(devices.router)
app.include_router(households.router)
app.include_router(dashboard.router)
app.include_router(pets.router)


# Redirect default url to docs
@app.get("/",
         include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


def main():
    # CORS
    if settings.cors:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors.split(","),
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    uvicorn.run("main:app", port=settings.port, host="0.0.0.0", log_level=settings.loglevel, reload=settings.debug)


if __name__ == '__main__':
    main()
