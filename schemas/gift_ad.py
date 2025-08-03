from datetime import datetime
from pydantic import BaseModel

# === GiftTransaction ===
class GiftTransactionBase(BaseModel):
    sender_id: int
    recipient_id: int
    gift_name: str
    gift_value: float  # in SmartCoins

class GiftTransactionCreate(GiftTransactionBase):
    pass

class GiftTransactionOut(GiftTransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# === AdEarning ===
class AdEarningBase(BaseModel):
    ad_type: str = "video"
    smartcoins_earned: float
    details: str | None = None

class AdEarningCreate(AdEarningBase):
    user_id: int

class AdEarningOut(AdEarningBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
