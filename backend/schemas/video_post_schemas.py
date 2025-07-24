from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VideoPostBase(BaseModel):
    caption: Optional[str] = None
    hashtags: Optional[str] = None
    is_draft: bool = True
    video_url: str

class VideoPostCreate(VideoPostBase):
    recorded_stream_id: int

class VideoPostUpdate(VideoPostBase):
    pass

class VideoPostOut(VideoPostBase):
    id: int
    recorded_stream_id: int
    created_at: datetime

    class Config:
        orm_mode = True
