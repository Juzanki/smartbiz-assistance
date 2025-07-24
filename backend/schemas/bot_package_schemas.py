from pydantic import BaseModel
from typing import List
from datetime import datetime

class BotPackageBase(BaseModel):
    name: str
    description: str
    price_monthly: float
    price_yearly: float
    features: List[str]

class BotPackageOut(BotPackageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
