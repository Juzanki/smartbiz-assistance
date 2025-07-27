from datetime import datetime
from pydantic import BaseModel

# --- APIKeyBase ---
class APIKeyBase(BaseModel):
    name: str

# --- APIKeyCreate ---
class APIKeyCreate(APIKeyBase):
    pass

# --- APIKeyOut ---
class APIKeyOut(APIKeyBase):
    id: int
    key: str
    created_at: datetime
    class Config:
        from_attributes = True
