from datetime import datetime
from pydantic import BaseModel

# --- Wallet ---
class WalletOut(BaseModel):
    id: int
    user_id: int
    balance: float
    smartcoin: float
    updated_at: datetime

    class Config:
        from_attributes = True

# --- WalletTransaction ---
class WalletTransactionBase(BaseModel):
    type: str  # deposit, withdraw, convert, transfer
    amount: float
    currency: str = "TZS"
    description: str | None = None

class WalletTransactionCreate(WalletTransactionBase):
    wallet_id: int

class WalletTransactionOut(WalletTransactionBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
