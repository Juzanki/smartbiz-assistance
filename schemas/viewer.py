# backend/schemas/viewer.py

from pydantic import BaseModel
from datetime import datetime

class ViewerCreate(BaseModel):
    user_id: int
    stream_id: str

class ViewerOut(BaseModel):
    id: int
    user_id: int
    stream_id: str
    joined_at: datetime
