# 📦 schemas/coin_wallet.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CoinWalletBase(BaseModel):
    balance: float

class CoinWalletCreate(BaseModel):
    user_id: int
    balance: Optional[float] = 0.0

class CoinWalletUpdate(BaseModel):
    balance: float

class CoinWalletResponse(CoinWalletBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
