from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# --- PlanCreate ---


class PlanCreate(BaseModel):
    name: str
    price: float
    duration_days: int
    description: Optional[str] = None

# --- PlanOut ---


class PlanOut(PlanCreate):
    id: int

    class Config:
        from_attributes = True

# --- SubscribeRequest ---


class SubscribeRequest(BaseModel):
    plan_id: int

# --- SubscriptionOut ---


class SubscriptionOut(BaseModel):
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime
    is_active: bool

    class Config:
        from_attributes = True
