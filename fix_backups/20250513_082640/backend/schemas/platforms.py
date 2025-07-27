from datetime import datetime
from pydantic import BaseModel

# --- PlatformConnectRequest ---
class PlatformConnectRequest(BaseModel):
    platform: str
    access_token: str

# --- PlatformOut ---
class PlatformOut(BaseModel):
    id: int
    platform: str
    connected_at: datetime

    class Config:
        from_attributes = True

# --- LanguagePreferenceUpdate ---
class LanguagePreferenceUpdate(BaseModel):
    language: str
