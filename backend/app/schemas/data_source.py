from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Dict, Any

class DataSourceCreate(BaseModel):
    name: str
    source_type: str
    config: Dict[str, Any] # E.g., {"host": "localhost", "password": "secret"}

class DataSourceResponse(BaseModel):
    id: UUID
    name: str
    source_type: str
    status: str
    last_successful_sync: datetime | None
    last_failed_sync: datetime | None
    created_at: datetime
    is_active: bool
    # Notice we DO NOT include the config or encrypted_config here!

    class Config:
        from_attributes = True