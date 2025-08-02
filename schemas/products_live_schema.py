from pydantic import BaseModel
from datetime import datetime

class LiveProductCreate(BaseModel):
    room_id: str
    product_id: int

class LiveProductOut(BaseModel):
    id: int
    room_id: str
    product_id: int
    showcased_at: datetime
