from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TargetingCriteria(BaseModel):
    regions: Optional[List[str]] = None         # e.g., ["Dar es Salaam", "Arusha"]
    tags: Optional[List[str]] = None            # e.g., ["VIP", "Debtor"]
    last_purchase_after: Optional[date] = None  # date filter
    has_replied: Optional[bool] = None
