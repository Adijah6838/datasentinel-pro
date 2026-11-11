from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class OrganizationCreate(BaseModel):
    name: str
    subscription_plan: str = "free"

class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    subscription_plan: str
    created_at: datetime

    class Config:
        from_attributes = True