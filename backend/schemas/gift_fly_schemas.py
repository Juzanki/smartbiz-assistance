from pydantic import BaseModel
from datetime import datetime

class GiftFlyCreate(BaseModel):
    stream_id: int
    user_id: int
    gift_name: str

class GiftFlyOut(BaseModel):
    id: int
    stream_id: int
    user_id: int
    gift_name: str
    position: int
    sent_at: datetime

    class Config:
        from_attributes = True
