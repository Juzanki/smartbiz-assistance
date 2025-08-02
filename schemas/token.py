from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# --- Token ---


class Token(BaseModel):
    access_token: str
    token_type: str

# --- TokenData ---


class TokenData(BaseModel):
    email: Optional[str] = None
