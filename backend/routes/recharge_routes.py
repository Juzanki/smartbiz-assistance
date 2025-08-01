from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.recharge_schemas import *
from backend.crud import recharge_crud
from backend.dependencies import get_current_user, get_admin_user

router = APIRouter()

@router.post("/", response_model=RechargeOut)
def initiate_recharge(data: RechargeCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return recharge_crud.create_recharge(db, current_user.id, data)

@router.post("/complete/{reference}", response_model=RechargeOut)
def confirm_recharge(reference: str, db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    txn = recharge_crud.complete_recharge(db, reference)
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found or already completed")
    return txn
