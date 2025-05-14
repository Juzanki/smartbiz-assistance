from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, Field, HttpUrl

# --- UserBase ---


class UserBase(BaseModel):
    pass

# --- UserCreate ---


class UserCreate(UserBase):
    password: str

# --- User ---


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- UserUpdate ---


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    business_name: Optional[str] = None
    business_type: Optional[str] = None
    language: Optional[str] = None
    telegram_id: Optional[int] = None
