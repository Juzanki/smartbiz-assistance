from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WithdrawRequestCreate(BaseModel):
    amount: float

class WithdrawRequestOut(BaseModel):
    id: int
    user_id: int
    amount: float
    status: str
    requested_at: datetime
    approved_at: Optional[datetime] = None
    is_paid: bool

    class Config:
        from_attributes = True
