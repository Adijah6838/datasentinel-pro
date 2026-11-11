import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class QualityRule(Base):
    __tablename__ = "quality_rules"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    data_source_id = Column(UUID(as_uuid=True), ForeignKey("data_sources.id"), nullable=False)
    
    name = Column(String, nullable=False)
    rule_type = Column(String, nullable=False) # completeness, uniqueness, validity, etc.
    column_name = Column(String, nullable=False)
    config = Column(JSON, nullable=False) # e.g., {"expected_type": "email"} or {"min_length": 5}
    
    is_active = Column(String, default="active", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)