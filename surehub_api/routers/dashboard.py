from fastapi import APIRouter

from surehub_api.entities import official
from surehub_api.entities.openapi import Tags
from surehub_api.services import dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=[Tags.DASHBOARD],
)


@router.get("/",
            response_model_exclude_none=True)
async def get_dashboard() -> official.MeStart:
    return dashboard.get_dashboard()
