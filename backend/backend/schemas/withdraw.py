from datetime import datetime
from pydantic import BaseModel

class WithdrawRequestBase(BaseModel):
    amount: float
    method: str = "mpesa"
    destination: str

class WithdrawRequestCreate(WithdrawRequestBase):
    user_id: int

class WithdrawRequestReview(BaseModel):
    status: str  # "approved" or "rejected"
    feedback: str | None = None

class WithdrawRequestOut(WithdrawRequestBase):
    id: int
    user_id: int
    status: str
    feedback: str | None
    created_at: datetime
    reviewed_at: datetime | None = None

    class Config:
        from_attributes = True
