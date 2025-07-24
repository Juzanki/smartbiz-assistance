from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.auth import get_current_user
from backend.models.user import User
from backend.schemas.gift_ad import (
    GiftTransactionCreate, GiftTransactionOut,
    AdEarningCreate, AdEarningOut
)
from backend.crud import gift_ad_crud
from backend.models.gift_transaction import GiftTransaction
from backend.models.ad_earning import AdEarning

router = APIRouter(
    prefix="/smartcoin",
    tags=["SmartCoin Earnings"]
)

@router.post("/send-gift", response_model=GiftTransactionOut)
def send_gift(
    gift: GiftTransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.id != gift.sender_id:
        raise HTTPException(status_code=403, detail="Unauthorized sender")

    return gift_ad_crud.send_gift_and_credit(db, gift)

@router.post("/credit-ad", response_model=AdEarningOut)
def credit_ad_earning(
    ad: AdEarningCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "owner"]:
        raise HTTPException(status_code=403, detail="Only admin can credit ads")
    
    return gift_ad_crud.credit_ad_earning(db, ad)

@router.get("/my-gifts", response_model=List[GiftTransactionOut])
def my_gift_earnings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(GiftTransaction).filter(GiftTransaction.recipient_id == current_user.id).order_by(GiftTransaction.created_at.desc()).all()

@router.get("/my-ads", response_model=List[AdEarningOut])
def my_ad_earnings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(AdEarning).filter(AdEarning.user_id == current_user.id).order_by(AdEarning.created_at.desc()).all()
