from pydantic import BaseModel
from datetime import datetime

class LiveViewerIn(BaseModel):
    user_id: int
    stream_id: int

class LiveViewerOut(BaseModel):
    id: int
    user_id: int
    stream_id: int
    joined_at: datetime
    left_at: datetime | None
    is_active: bool

    class Config:
        from_attributes = True
