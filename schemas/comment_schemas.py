from pydantic import BaseModel
from datetime import datetime

class VideoCommentCreate(BaseModel):
    video_post_id: int
    message: str

class VideoCommentOut(BaseModel):
    id: int
    user_id: int
    video_post_id: int
    message: str
    timestamp: datetime

    class Config:
        from_attributes = True
