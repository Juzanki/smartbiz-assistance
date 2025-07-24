from datetime import datetime
from pydantic import BaseModel

class PushSubscriptionBase(BaseModel):
    endpoint: str
    p256dh: str
    auth: str

class PushSubscriptionCreate(PushSubscriptionBase):
    user_id: int

class PushSubscriptionOut(PushSubscriptionBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
