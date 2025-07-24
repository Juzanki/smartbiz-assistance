from pydantic import BaseModel
from datetime import datetime

class ReplayActivityIn(BaseModel):
    action: str  # share, download
    platform: str | None = None

class ReplayActivityOut(BaseModel):
    id: int
    user_id: int | None
    video_post_id: int
    action: str
    platform: str | None
    created_at: datetime

    class Config:
        orm_mode = True
