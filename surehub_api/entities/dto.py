from typing import Optional

from pydantic import BaseModel

from surehub_api.entities import official


class PetStatusResponse(BaseModel):
    position: Optional[official.PetPosition] = None
    feeding: Optional[official.PetConsumptionStatus] = None
    drinking: Optional[official.PetConsumptionStatus] = None


class UpdatePetStatusRequest(BaseModel):
    position: Optional[official.PetPositionWhere] = None
    indoor_only: Optional[bool] = None
