from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.auth import get_current_user
from backend.dependencies import check_admin
from backend.models.user import User
from backend.schemas.audit_log import AuditLogOut
from backend.crud import audit_log_crud

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)

@router.get("/", response_model=List[AuditLogOut])
def get_all_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only admin or owner can view all logs
    if current_user.role not in ["admin", "owner"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return audit_log_crud.get_all_logs(db)

@router.get("/me", response_model=List[AuditLogOut])
def get_my_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return audit_log_crud.get_logs_by_user(db, user_id=current_user.id)
