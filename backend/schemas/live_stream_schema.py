from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LiveStreamCreate(BaseModel):
    host_id: int
    room_id: str
    title: Optional[str] = None
    topic: Optional[str] = None
    goal: Optional[str] = None

class LiveStreamUpdate(BaseModel):
    title: Optional[str]
    topic: Optional[str]
    goal: Optional[str]
    is_live: Optional[bool] = None
    ended_at: Optional[datetime] = None

class LiveStreamOut(BaseModel):
    id: int
    host_id: int
    room_id: str
    title: Optional[str]
    topic: Optional[str]
    goal: Optional[str]
    is_live: bool
    started_at: datetime
    ended_at: Optional[datetime]
