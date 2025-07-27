from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, Field, HttpUrl

# --- LoginRequest ---
class LoginRequest(BaseModel):
    pass
