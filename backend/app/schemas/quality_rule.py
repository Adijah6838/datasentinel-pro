from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Dict, Any

class QualityRuleCreate(BaseModel):
    data_source_id: UUID
    name: str
    rule_type: str
    column_name: str
    config: Dict[str, Any]

class QualityRuleResponse(BaseModel):
    id: UUID
    data_source_id: UUID
    name: str
    rule_type: str
    column_name: str
    config: Dict[str, Any]
    is_active: str
    created_at: datetime

    class Config:
        from_attributes = True