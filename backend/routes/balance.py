from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.schemas import balance_schemas
from backend.crud import balance_crud
from backend.db import get_db
from backend.dependencies import get_current_user, get_admin_user

router = APIRouter()

@router.get("/balance/me", response_model=balance_schemas.BalanceOut)
def get_my_balance(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    balance = balance_crud.get_user_balance(db, current_user.id)
    if not balance:
        raise HTTPException(status_code=404, detail="Balance not found")
    return balance

@router.post("/withdraw", response_model=balance_schemas.WithdrawRequestOut)
def request_withdrawal(data: balance_schemas.WithdrawRequestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return balance_crud.create_withdraw_request(db, current_user.id, data)

@router.get("/withdrawals/pending", response_model=list[balance_schemas.WithdrawRequestOut])
def list_pending_withdrawals(db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    return balance_crud.get_pending_withdrawals(db)

@router.post("/withdrawals/{request_id}/approve", response_model=balance_schemas.WithdrawRequestOut)
def approve_withdrawal(request_id: int, db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    return balance_crud.approve_withdrawal(db, request_id)

@router.post("/withdrawals/{request_id}/reject", response_model=balance_schemas.WithdrawRequestOut)
def reject_withdrawal(request_id: int, db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    return balance_crud.reject_withdrawal(db, request_id)
