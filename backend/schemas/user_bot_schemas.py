from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBotCreate(BaseModel):
    name: str
    purpose: Optional[str]
    bot_package_id: int

class UserBotOut(BaseModel):
    id: int
    name: str
    purpose: Optional[str]
    is_active: bool
    expiry_date: Optional[datetime]
    created_at: datetime
    bot_package_id: int

    class Config:
        from_attributes = True
