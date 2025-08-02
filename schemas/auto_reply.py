from datetime import datetime
from pydantic import BaseModel

class AutoReplyBase(BaseModel):
    platform: str  # e.g., whatsapp, telegram
    is_enabled: bool
    reply_message: str

class AutoReplyCreate(AutoReplyBase):
    user_id: int

class AutoReplyUpdate(BaseModel):
    is_enabled: bool
    reply_message: str

class AutoReplyOut(AutoReplyBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
