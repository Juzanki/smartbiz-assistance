from datetime import datetime
from pydantic import BaseModel

class ScheduledTaskBase(BaseModel):
    type: str = "message"
    content: str
    scheduled_time: datetime

class ScheduledTaskCreate(ScheduledTaskBase):
    user_id: int

class ScheduledTaskOut(ScheduledTaskBase):
    id: int
    user_id: int
    status: str
    retry_count: int
    created_at: datetime

    class Config:
        from_attributes = True
