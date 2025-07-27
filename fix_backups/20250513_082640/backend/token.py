from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, Field, HttpUrl

# --- Token ---
class Token(BaseModel):
    pass

# --- TokenData ---
class TokenData(BaseModel):
    pass
