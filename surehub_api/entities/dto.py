from typing import Optional

from pydantic import BaseModel

from surehub_api.entities import official


class PetStateResponse(BaseModel):
    position: Optional[official.PetPosition] = None
    feeding: Optional[official.PetConsumptionStatus] = None
    drinking: Optional[official.PetConsumptionStatus] = None


class UpdatePetStateRequest(BaseModel):
    position: Optional[official.PetPositionWhere] = None
    indoor_only: Optional[bool] = None
