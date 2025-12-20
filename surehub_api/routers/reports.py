from datetime import datetime

from fastapi import APIRouter

from surehub_api.entities import official
from surehub_api.entities.openapi import Tags
from surehub_api.services import reports

router = APIRouter(
    prefix="/reports",
    tags=[Tags.REPORT],
)


@router.get("/pet",
            response_model_exclude_none=True)
async def get_pet_report(household_id: int,
                         pet_id: int,
                         from_datetime: datetime,
                         to_datetime: datetime
                         ) -> official.PetReport:
    return reports.get_pet_report(household_id, pet_id, from_datetime, to_datetime)
