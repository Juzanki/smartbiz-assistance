# 📦 routes/coin_wallet.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend import models
from backend.schemas import coin_wallet

router = APIRouter(prefix="/wallets", tags=["Coin Wallet"])

@router.post("/", response_model=coin_wallet.CoinWalletResponse)
def create_wallet(wallet_data: coin_wallet.CoinWalletCreate, db: Session = Depends(get_db)):
    existing = db.query(models.CoinWallet).filter(models.CoinWallet.user_id == wallet_data.user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Wallet already exists")
    wallet = models.CoinWallet(user_id=wallet_data.user_id, balance=wallet_data.balance)
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet

@router.get("/{user_id}", response_model=coin_wallet.CoinWalletResponse)
def get_wallet(user_id: int, db: Session = Depends(get_db)):
    wallet = db.query(models.CoinWallet).filter(models.CoinWallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.put("/{user_id}", response_model=coin_wallet.CoinWalletResponse)
def update_wallet(user_id: int, wallet_data: coin_wallet.CoinWalletUpdate, db: Session = Depends(get_db)):
    wallet = db.query(models.CoinWallet).filter(models.CoinWallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    wallet.balance = wallet_data.balance
    db.commit()
    db.refresh(wallet)
    return wallet
