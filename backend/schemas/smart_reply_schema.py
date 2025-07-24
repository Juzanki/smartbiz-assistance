from pydantic import BaseModel
from typing import List

class SmartReplyCreate(BaseModel):
    room_id: str
    replies: List[str]

class SmartReplyOut(BaseModel):
    id: int
    room_id: str
    message: str
