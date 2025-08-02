from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LiveStreamExploreOut(BaseModel):
    id: int
    room_id: str
    host_id: int
    title: Optional[str]
    topic: Optional[str]
    is_live: bool
    is_featured: bool
    viewers_count: int
    gifts_count: int
    started_at: datetime
