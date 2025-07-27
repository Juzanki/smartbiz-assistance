from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class APIKeyCreate(BaseModel):
    key: str
    plan: Optional[str] = "free"
    owner_id: Optional[int] = None

class APIKeyRead(BaseModel):
    id: int
    key: str
    plan: str
    owner_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True  # ✅ Updated for Pydantic v2
