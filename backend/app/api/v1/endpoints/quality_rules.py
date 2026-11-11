from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.quality_rule import QualityRule
from app.schemas.quality_rule import QualityRuleCreate, QualityRuleResponse

router = APIRouter()

@router.post("/", response_model=QualityRuleResponse)
def create_rule(
    rule_in: QualityRuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "engineer"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    new_rule = QualityRule(
        organization_id=current_user.organization_id,
        data_source_id=rule_in.data_source_id,
        name=rule_in.name,
        rule_type=rule_in.rule_type,
        column_name=rule_in.column_name,
        config=rule_in.config
    )
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)
    return new_rule

@router.get("/", response_model=List[QualityRuleResponse])
def list_rules(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(QualityRule).filter(QualityRule.organization_id == current_user.organization_id).all()