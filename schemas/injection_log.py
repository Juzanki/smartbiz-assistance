from datetime import datetime
from pydantic import BaseModel

# --- InjectionLogCreate ---
class InjectionLogCreate(BaseModel):
    tag: str
    content: str
    status: str

# --- InjectionLogOut ---
class InjectionLogOut(BaseModel):
    id: int
    tag: str
    content: str
    status: str
    timestamp: datetime

    class Config:
        from_attributes = True
