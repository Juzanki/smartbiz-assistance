"""
Pydantic schemas for SmartBiz Assistant.
Includes user registration, login, tokens, subscriptions, posts, payments, API key management, and broadcasting.
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr, Field, HttpUrl

# ==================== USER SCHEMAS ====================

class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: Optional[str] = None
    full_name: Optional[str] = "N/A"
    telegram_id: Optional[int] = None
    business_name: Optional[str] = "N/A"
    business_type: Optional[str] = None
    language: Optional[str] = "sw"
    user_token: Optional[str] = None
    subscription_status: Optional[str] = "free"
    subscription_expiry: Optional[datetime] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    business_name: Optional[str] = None
    business_type: Optional[str] = None
    language: Optional[str] = None
    telegram_id: Optional[int] = None

# ==================== TOKEN SCHEMAS ====================

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# ==================== LOGIN SCHEMA ====================

class LoginRequest(BaseModel):
    identifier: str
    password: str
    country_code: Optional[str] = None

    @classmethod
    def validate_country_code(cls, values):
        identifier = values.get("identifier")
        code = values.get("country_code")
        if identifier and (identifier.startswith("0") or identifier.isdigit()):
            if not code:
                raise ValueError("Country code is required for phone login.")
            if not code.startswith("+") or len(code) < 2:
                raise ValueError("Invalid country code format (e.g., +255).")
        return values

# ==================== API KEY SCHEMAS ====================

class APIKeyBase(BaseModel):
    name: str

class APIKeyCreate(APIKeyBase):
    pass

class APIKeyOut(APIKeyBase):
    id: int
    key: str
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== SOCIAL MEDIA POST SCHEMAS ====================

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== SETTINGS SCHEMAS ====================

class SettingBase(BaseModel):
    name: str
    value: str

class SettingCreate(SettingBase):
    pass

class SettingOut(SettingBase):
    id: int

    class Config:
        from_attributes = True

# ==================== FORGOT PASSWORD FLOW ====================

class ForgotPasswordRequest(BaseModel):
    identifier: str = Field(..., example="juza@example.com or +255712345678")

class VerifyResetCode(BaseModel):
    identifier: str
    code: str

class ResetPassword(BaseModel):
    identifier: str
    code: str
    new_password: constr(min_length=6)

# ==================== SUBSCRIPTION PLAN SCHEMAS ====================

class PlanCreate(BaseModel):
    name: str
    price: float
    duration_days: int
    description: Optional[str] = None

class PlanOut(PlanCreate):
    id: int

    class Config:
        from_attributes = True

class SubscribeRequest(BaseModel):
    plan_id: int

class SubscriptionOut(BaseModel):
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime
    is_active: bool

    class Config:
        from_attributes = True

# ==================== PAYMENT SCHEMAS ====================

class PaymentRequest(BaseModel):
    amount: float
    phone_number: str
    reference: Optional[str] = None

class PaymentResponse(BaseModel):
    id: str
    reference: str
    amount: float
    status: str
    phone_number: str
    method: str
    created_at: datetime
    instructions: str

class ConfirmMpesaRequest(BaseModel):
    reference: str

# ==================== BROADCAST SCHEMA ====================

class BroadcastMessage(BaseModel):
    message: str
    channels: List[str]

# ==================== PRODUCT SCHEMA ====================

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== NEGOTIATION SCHEMA ====================

class NegotiationRequest(BaseModel):
    product_id: int
    user_message: str

class NegotiationResponse(BaseModel):
    product_name: str
    original_price: float
    proposed_reply: str
    suggested_discount: Optional[float] = None

# ==================== ADMIN / OWNER SCHEMAS ====================

class RoleUpdateRequest(BaseModel):
    user_id: int
    new_role: str

class AdminCreate(BaseModel):
    email: str
    password: str
    name: str

class OwnerLoginRequest(BaseModel):
    email: EmailStr

class OwnerLoginVerify(BaseModel):
    token: str

# ==================== SMART ORDER SCHEMAS ====================

class SmartOrderOut(BaseModel):
    id: int
    customer_name: str
    product_id: int
    method: str
    created_at: datetime
    status: str

    class Config:
        from_attributes = True

# ==================== PLATFORM CONNECTION SCHEMAS ====================

class PlatformConnectRequest(BaseModel):
    platform: str
    access_token: str

class PlatformOut(BaseModel):
    id: int
    platform: str
    connected_at: datetime

    class Config:
        from_attributes = True

class LanguagePreferenceUpdate(BaseModel):
    language: str

# ==================== CAMPAIGN SCHEDULE SCHEMA ====================

class CampaignRequest(BaseModel):
    product_id: int
    platforms: List[str]
    media_type: Optional[str] = "text"
    schedule_time: Optional[datetime]

# ==================== SCHEDULED MESSAGES SCHEMA ====================

class ScheduledMessageCreate(BaseModel):
    message: str
    platform: str
    recipient: str
    scheduled_time: datetime

class ScheduledMessageOut(BaseModel):
    id: int
    message: str
    platform: str
    recipient: str
    scheduled_time: datetime
    sent: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ==================== ADVANCED SETTINGS ====================

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

class SettingsCreate(SettingsBase):
    pass

class SettingsOut(SettingsBase):
    user_id: str

    class Config:
        from_attributes = True

class AIBotSettingsSchema(BaseModel):
    active: bool = True
    language: str = "en"
    default_greeting: str = "Hello! How can I assist you today?"
    platforms: List[str] = ["whatsapp", "telegram"]

    class Config:
        from_attributes = True

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

class AuditLogOut(BaseModel):
    id: int
    user_id: int
    action: str
    target: str
    timestamp: datetime

    class Config:
        from_attributes = True

class SchedulePostSchema(BaseModel):
    platform: str
    content: str
    media_url: Optional[str]
    scheduled_time: datetime

class InjectionLogCreate(BaseModel):
    tag: str
    content: str
    status: str

class InjectionLogOut(BaseModel):
    id: int
    tag: str
    content: str
    status: str
    timestamp: datetime

    class Config:
        orm_mode = True
