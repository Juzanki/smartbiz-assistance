from pydantic import BaseModel
from datetime import datetime

class AnnouncementCreate(BaseModel):
    title: str
    content: str

class AnnouncementOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
