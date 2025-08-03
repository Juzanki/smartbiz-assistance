from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, HttpUrl

# ==================== 🔹 Base User Schema ====================
class UserBase(BaseModel):
    """
    Msingi wa schema ya mtumiaji unaotumika katika Create, Update na Response.
    """
    username: str = Field(..., min_length=3, example="johndoe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    full_name: Optional[str] = Field(None, example="John Doe")
    phone_number: Optional[str] = Field(None, example="+255712345678")
    language: Optional[str] = Field(default="sw", example="sw")
    profile_image: Optional[HttpUrl] = Field(None, example="https://cdn.smartbiz.com/profiles/avatar123.png")
    is_verified: Optional[bool] = Field(default=False, example=False)

# ==================== 🟢 User Creation Schema ====================
class UserCreate(UserBase):
    """
    Schema ya kusajili mtumiaji mpya.
    """
    password: str = Field(..., min_length=6, example="StrongPass123!")

# ==================== ✏️ User Update Schema ====================
class UserUpdate(BaseModel):
    """
    Schema ya kusasisha taarifa za mtumiaji.
    """
    full_name: Optional[str] = Field(None, example="Updated Name")
    phone_number: Optional[str] = Field(None, example="+255789654321")
    language: Optional[str] = Field(None, example="en")
    profile_image: Optional[HttpUrl] = Field(None, example="https://cdn.smartbiz.com/profiles/updated_avatar.png")
    is_verified: Optional[bool] = Field(None, example=True)
    badge_level: Optional[str] = Field(None, example="gold")
    subscription_status: Optional[str] = Field(None, example="active")  # inactive, active, expired
    role: Optional[str] = Field(None, example="admin")  # user, admin, owner

# ==================== 📤 User Response Schema ====================
class UserOut(UserBase):
    """
    Schema ya kurejesha taarifa za mtumiaji kwa client (response).
    """
    id: int
    role: str = Field(..., example="user")
    badge_level: str = Field(..., example="bronze")
    subscription_status: str = Field(..., example="inactive")
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True
