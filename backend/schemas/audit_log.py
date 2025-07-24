from datetime import datetime
from pydantic import BaseModel

class AuditLogBase(BaseModel):
    action: str
    ip_address: str | None = None
    description: str | None = None

class AuditLogCreate(AuditLogBase):
    user_id: int

class AuditLogOut(AuditLogBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
