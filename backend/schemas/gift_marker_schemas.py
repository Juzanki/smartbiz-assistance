from pydantic import BaseModel
from datetime import datetime

class GiftMarkerCreate(BaseModel):
    stream_id: int
    gift_name: str
    position: int

class GiftMarkerOut(BaseModel):
    id: int
    stream_id: int
    gift_name: str
    position: int
    timestamp: datetime

    class Config:
        from_attributes = True
