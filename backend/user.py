from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, Field, HttpUrl

# --- UserBase ---


class UserBase(BaseModel):
    pass

# --- UserCreate ---


class UserCreate(BaseModel):
    pass

# --- User ---


class User(BaseModel):
    pass

# --- UserUpdate ---


class UserUpdate(BaseModel):
    pass
