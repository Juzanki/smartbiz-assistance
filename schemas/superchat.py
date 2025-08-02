from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SuperchatCreate(BaseModel):
    sender_id: int
    stream_id: str
    amount: float
    message: Optional[str] = ""
    emoji: Optional[str] = None
    animation_id: Optional[str] = None
    voice_clip_url: Optional[str] = None
    highlight_color: Optional[str] = "#FFD700"

class SuperchatOut(BaseModel):
    id: int
    sender_id: int
    stream_id: str
    amount: float
    message: Optional[str]
    emoji: Optional[str]
    animation_id: Optional[str]
    voice_clip_url: Optional[str]
    highlight_color: Optional[str]
    timestamp: datetime
