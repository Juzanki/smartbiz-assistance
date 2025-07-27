from typing import Optional
from pydantic import BaseModel

# --- LoginRequest ---
class LoginRequest(BaseModel):
    identifier: str
    password: str
    country_code: Optional[str] = None
