from pydantic import BaseModel
from datetime import datetime

class ShareActivityCreate(BaseModel):
    user_id: int
    room_id: str
    platform: str
    content_type: str = "stream"  # default: stream

class ShareActivityOut(BaseModel):
    id: int
    user_id: int
    room_id: str
    platform: str
    content_type: str
    shared_at: datetime
