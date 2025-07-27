from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl

# --- SettingBase ---
class SettingBase(BaseModel):
    name: str
    value: str

# --- SettingCreate ---
class SettingCreate(SettingBase):
    pass

# --- SettingOut ---
class SettingOut(SettingBase):
    id: int
    class Config:
        from_attributes = True

# --- SettingsBase ---
class SettingsBase(BaseModel):
    business_name: str
    tagline: Optional[str] = None
    language: Optional[str] = "en"
    logo_url: Optional[HttpUrl] = None
    primary_color: Optional[str] = "#0d6efd"
    secondary_color: Optional[str] = "#6c757d"
    timezone: Optional[str] = "Africa/Dar_es_Salaam"
    currency: Optional[str] = "TZS"
    enable_custom_domain: Optional[bool] = False

# --- SettingsCreate ---
class SettingsCreate(SettingsBase):
    pass

# --- SettingsOut ---
class SettingsOut(SettingsBase):
    user_id: str
    class Config:
        from_attributes = True

# --- AIBotSettingsSchema ---
class AIBotSettingsSchema(BaseModel):
    active: bool = True
    language: str = "en"
    default_greeting: str = "Hello! How can I assist you today?"
    platforms: List[str] = ["whatsapp", "telegram"]
    class Config:
        from_attributes = True

# --- SupportTicketOut ---
class SupportTicketOut(BaseModel):
    id: int
    user_id: int
    subject: str
    type: str
    description: str
    attachment: Optional[str] = None
    status: str
    created_at: datetime
    class Config:
        from_attributes = True

# --- AuditLogOut ---
class AuditLogOut(BaseModel):
    id: int
    user_id: int
    action: str
    target: str
    timestamp: datetime
    class Config:
        from_attributes = True

# --- SchedulePostSchema ---
class SchedulePostSchema(BaseModel):
    platform: str
    content: str
    media_url: Optional[str]
    scheduled_time: datetime
