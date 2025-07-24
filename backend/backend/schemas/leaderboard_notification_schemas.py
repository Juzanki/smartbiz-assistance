from pydantic import BaseModel
from datetime import datetime

class LeaderboardNotificationOut(BaseModel):
    id: int
    stream_id: int
    user_id: int
    position: int
    previous_position: int | None
    type: str
    seen: bool
    created_at: datetime

    class Config:
        orm_mode = True
