from pydantic import BaseModel
from datetime import datetime

class ViewStatOut(BaseModel):
    id: int
    user_id: int | None
    video_post_id: int
    viewed_at: datetime

    class Config:
        from_attributes = True
