# backend/schemas/host_schemas.py
from pydantic import BaseModel
from datetime import datetime

class CoHostInviteCreate(BaseModel):
    stream_id: int
    receiver_id: int

class CoHostInviteUpdate(BaseModel):
    status: str  # accepted, rejected

class CoHostInviteOut(BaseModel):
    id: int
    stream_id: int
    sender_id: int
    receiver_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True  # ✅ Pydantic v2 replacement for orm_mode
