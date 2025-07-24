from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.db import get_db
from backend.auth import get_current_user
from backend.models.user import User
from backend.schemas.targeting import TargetingCriteria
from backend.models.customer import Customer
from backend.utils.targeting_engine import filter_customers

router = APIRouter(
    prefix="/campaign",
    tags=["Campaign Targeting"]
)

@router.post("/target-preview", response_model=List[Customer])
def preview_targeted_customers(
    criteria: TargetingCriteria,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return filter_customers(db, criteria)
