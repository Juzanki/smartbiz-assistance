from pydantic import BaseModel
from datetime import datetime

class DreamLogCreate(BaseModel):
    prompt: str

class DreamLogOut(BaseModel):
    id: int
    prompt: str
    result: str | None = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
