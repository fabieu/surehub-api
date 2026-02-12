from typing import Optional

from pydantic import BaseModel

from surehub_api.entities import official


class PetStatusResponse(BaseModel):
    position: Optional[official.PetPosition] = None
    feeding: Optional[official.PetConsumptionStatus] = None
    drinking: Optional[official.PetConsumptionStatus] = None
    indoor_only: Optional[bool] = None


class UpdatePetStatusRequest(BaseModel):
    household_ids: Optional[list[int]] = None
    position: Optional[official.PetPositionWhere] = None
    indoor_only: Optional[bool] = None
