import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class DataSource(Base):
    __tablename__ = "data_sources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    name = Column(String, index=True, nullable=False)
    source_type = Column(String, nullable=False) # postgres, sqlite, rest, csv, json, stream
    status = Column(String, default="inactive", nullable=False)
    
    # Encrypted JSON string containing connection details (host, port, username, password)
    encrypted_config = Column(String, nullable=False)
    
    last_successful_sync = Column(DateTime, nullable=True)
    last_failed_sync = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)