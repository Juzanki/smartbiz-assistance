from datetime import datetime
from pydantic import BaseModel

# --- PostBase ---


class PostBase(BaseModel):
    title: str
    content: str

# --- PostCreate ---


class PostCreate(PostBase):
    pass

# --- PostOut ---


class PostOut(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    title: str
    content: str
    is_published: bool = True
