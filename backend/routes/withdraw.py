from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import withdraw_schemas
from backend.crud import withdraw_crud
from backend.db import get_db
from backend.dependencies import get_current_user, get_admin_user

router = APIRouter()

@router.post("/withdraw", response_model=withdraw_schemas.WithdrawRequestOut)
def request_withdrawal(data: withdraw_schemas.WithdrawRequestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return withdraw_crud.create_withdraw_request(db, current_user.id, data)

@router.get("/withdrawals/pending", response_model=list[withdraw_schemas.WithdrawRequestOut])
def list_pending_withdrawals(db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    return withdraw_crud.get_pending_withdrawals(db)

@router.post("/withdrawals/{request_id}/approve", response_model=withdraw_schemas.WithdrawRequestOut)
def approve_withdrawal(request_id: int, db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    return withdraw_crud.approve_withdrawal(db, request_id)

@router.post("/withdrawals/{request_id}/reject", response_model=withdraw_schemas.WithdrawRequestOut)
def reject_withdrawal(request_id: int, db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    return withdraw_crud.reject_withdrawal(db, request_id)
