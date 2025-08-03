from datetime import datetime
from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    slug: str
    domain: str | None = None

class TenantCreate(TenantBase):
    pass

class TenantOut(TenantBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
