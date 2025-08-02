from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.auth import get_current_user
from backend.dependencies import check_admin
from backend.models.user import User
from backend.schemas.tenant import TenantCreate, TenantOut
from backend.crud import tenant_crud

router = APIRouter(
    prefix="/tenants",
    tags=["Tenants"]
)

@router.post("/", response_model=TenantOut)
def create_tenant(
    tenant: TenantCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only the system owner can create tenants.")
    return tenant_crud.create_tenant(db, tenant)

@router.get("/", response_model=List[TenantOut])
def list_tenants(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only the system owner can view all tenants.")
    return tenant_crud.get_all_tenants(db)
