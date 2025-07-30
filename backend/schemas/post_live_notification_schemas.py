from pydantic import BaseModel
from datetime import datetime

class PostLiveNotificationOut(BaseModel):
    id: int
    user_id: int
    stream_id: int
    message: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
