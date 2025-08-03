from datetime import datetime
from pydantic import BaseModel

# --- ScheduledMessageCreate ---


class ScheduledMessageCreate(BaseModel):
    message: str
    platform: str
    recipient: str
    scheduled_time: datetime

# --- ScheduledMessageOut ---


class ScheduledMessageOut(BaseModel):
    id: int
    message: str
    platform: str
    recipient: str
    scheduled_time: datetime
    sent: bool
    created_at: datetime

    class Config:
        from_attributes = True
