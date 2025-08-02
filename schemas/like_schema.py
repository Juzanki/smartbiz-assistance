from pydantic import BaseModel
from datetime import datetime

class LikeCreate(BaseModel):
    stream_id: str
    user_id: int

class LikeResponse(BaseModel):
    id: int
    stream_id: str
    user_id: int
    created_at: datetime
