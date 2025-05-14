from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# --- CampaignRequest ---


class CampaignRequest(BaseModel):
    product_id: int
    platforms: List[str]
    media_type: Optional[str] = "text"
    schedule_time: Optional[datetime]
