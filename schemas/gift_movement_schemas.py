from pydantic import BaseModel
from datetime import datetime

class GiftMovementCreate(BaseModel):
    stream_id: int
    sender_id: int
    gift_id: int
    amount: int
    total_value: int

class GiftMovementOut(BaseModel):
    id: int
    stream_id: int
    sender_id: int
    gift_id: int
    amount: int
    total_value: int
    sent_at: datetime
