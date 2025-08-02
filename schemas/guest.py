from pydantic import BaseModel
from datetime import datetime

class GuestCreate(BaseModel):
    room_id: str
    user_id: int

class GuestOut(BaseModel):
    id: int
    room_id: str
    user_id: int
    is_approved: bool
    is_host: bool
    joined_at: datetime
