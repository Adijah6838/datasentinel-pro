from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    organization_name: str  # Used during registration to create the org

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: str
    organization_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True