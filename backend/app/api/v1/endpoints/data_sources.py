import json
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.core.encryption import encrypt_credentials
from app.models.user import User
from app.models.data_source import DataSource
from app.schemas.data_source import DataSourceCreate, DataSourceResponse
from app.workers.tasks import ingest_data_task

router = APIRouter()

@router.post("/", response_model=DataSourceResponse)
def create_data_source(
    source_in: DataSourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "engineer"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    config_json = json.dumps(source_in.config)
    encrypted_config = encrypt_credentials(config_json)

    new_source = DataSource(
        organization_id=current_user.organization_id,
        name=source_in.name,
        source_type=source_in.source_type,
        encrypted_config=encrypted_config,
        status="active"
    )
    
    db.add(new_source)
    db.commit()
    db.refresh(new_source)
    return new_source

@router.get("/", response_model=List[DataSourceResponse])
def list_data_sources(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sources = db.query(DataSource).filter(
        DataSource.organization_id == current_user.organization_id,
        DataSource.is_active == True
    ).all()
    return sources

@router.post("/{source_id}/ingest")
def trigger_ingestion(
    source_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    source = db.query(DataSource).filter(
        DataSource.id == source_id,
        DataSource.organization_id == current_user.organization_id
    ).first()

    if not source:
        raise HTTPException(status_code=404, detail="Data Source not found")

    # Send the task to the Celery Worker!
    ingest_data_task.delay(str(source.id))
    
    return {"message": "Ingestion task started in the background", "source_id": str(source.id)}