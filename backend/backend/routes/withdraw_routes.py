from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.db import get_db
from backend.auth import get_current_user
from backend.dependencies import check_admin
from backend.models.user import User
from backend.schemas.withdraw import (
    WithdrawRequestCreate, WithdrawRequestOut, WithdrawRequestReview
)
from backend.crud import withdraw_crud

router = APIRouter(
    prefix="/withdraw",
    tags=["Withdraw Requests"]
)

# User: request withdraw
@router.post("/", response_model=WithdrawRequestOut)
def request_withdraw(
    request_data: WithdrawRequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.id != request_data.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return withdraw_crud.create_withdraw_request(db, request_data)

# User: view my requests
@router.get("/mine", response_model=List[WithdrawRequestOut])
def view_my_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return withdraw_crud.get_requests_by_user(db, current_user.id)

# Admin: view all requests
@router.get("/admin", response_model=List[WithdrawRequestOut])
def admin_view_all_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "owner"]:
        raise HTTPException(status_code=403, detail="Admin only")
    return withdraw_crud.get_all_requests(db)

# Admin: review (approve/reject)
@router.put("/{request_id}/review", response_model=WithdrawRequestOut)
def review_request(
    request_id: int,
    review: WithdrawRequestReview,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "owner"]:
        raise HTTPException(status_code=403, detail="Admin only")
    return withdraw_crud.review_withdraw_request(db, request_id, review)
