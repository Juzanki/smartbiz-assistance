from pydantic import BaseModel
from datetime import datetime

class RechargeCreate(BaseModel):
    amount: float
    method: str
    reference: str

class RechargeOut(BaseModel):
    id: int
    user_id: int
    amount: float
    method: str
    status: str
    reference: str
    created_at: datetime

    class Config:
        from_attributes = True
