from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# --- Request schema for creating a campaign ---
class CampaignCreate(BaseModel):
    title: str
    product_id: int
    rate: float                     # Percentage commission e.g., 10.5
    duration: int                   # Duration in days
    platforms: List[str]            # e.g., ["tiktok", "instagram"]
    media_type: Optional[str] = "text"    # Can be "text", "image", "video"
    schedule_time: Optional[datetime] = None

# You can alias the original class if you prefer:
CampaignRequest = CampaignCreate

# --- Response schema for showing saved campaign ---
class CampaignOut(BaseModel):
    id: int
    title: str
    product_id: int
    owner_id: int
    commission_rate: float
    ends_at: datetime
    created_at: datetime
