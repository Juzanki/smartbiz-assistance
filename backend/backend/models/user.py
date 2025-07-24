from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from backend.db import Base

class User(Base):
    __tablename__ = "users"

    # ========== Core Fields ==========
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default="user", nullable=False)
    full_name = Column(String(100), nullable=True)
    phone_number = Column(String(20), unique=True, index=True, nullable=True)
    language = Column(String(10), nullable=True, default="sw")
    created_at = Column(DateTime, default=datetime.utcnow)

    # ========== Extra Profile Fields ==========
    profile_image = Column(String, nullable=True)  # ✅ Added: for displaying user's avatar
    is_active = Column(Boolean, default=True)      # ✅ Added: to control account status
    is_verified = Column(Boolean, default=False)   # ✅ Optional: for badge or blue-check
    badge_level = Column(String, default='none')   # none, bronze, silver, gold, etc.
    subscription_status = Column(String, default="inactive")  # inactive, active, expired

    # ========== Relationships ==========
    posts = relationship("SocialMediaPost", back_populates="user", cascade="all, delete-orphan", lazy='selectin')
    payments = relationship("Payment", back_populates="user", cascade="all, delete-orphan")
    joined_campaigns = relationship("CampaignAffiliate", back_populates="user", cascade="all, delete-orphan")
    referrals = relationship("ReferralLog", back_populates="referrer", cascade="all, delete-orphan", foreign_keys="[ReferralLog.referrer_id]")
    referrals_received = relationship("ReferralLog", back_populates="referred_user", cascade="all, delete-orphan", foreign_keys="[ReferralLog.referred_user_id]")
    support_tickets = relationship("SupportTicket", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="user", cascade="all, delete-orphan")
    subscriptions = relationship("UserSubscription", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    scheduled_messages = relationship("ScheduledMessage", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("Settings", back_populates="user", uselist=False, cascade="all, delete-orphan")
    platforms = relationship("ConnectedPlatform", back_populates="user", cascade="all, delete-orphan")
    ai_bot_settings = relationship("AIBotSettings", back_populates="user", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    loyalty_points = relationship("LoyaltyPoint", back_populates="user", cascade="all, delete-orphan")
    drone_missions = relationship("DroneMission", back_populates="user", cascade="all, delete-orphan")
    customers = relationship("Customer", back_populates="user", cascade="all, delete-orphan")
    analytics_snapshots = relationship("AnalyticsSnapshot", back_populates="user", cascade="all, delete-orphan")
    billing_logs = relationship("BillingLog", back_populates="user", cascade="all, delete-orphan")
    notification_preferences = relationship("NotificationPreference", back_populates="user", uselist=False, cascade="all, delete-orphan")
    customer_feedbacks = relationship("CustomerFeedback", back_populates="user", cascade="all, delete-orphan")
    activity_score = relationship("ActivityScore", uselist=False, back_populates="user", cascade="all, delete-orphan")
    referral_bonuses = relationship("ReferralBonus", back_populates="referrer", cascade="all, delete-orphan", foreign_keys="[ReferralBonus.referrer_id]")
    tags = relationship("Tag", back_populates="user", cascade="all, delete-orphan")
    search_logs = relationship("SearchLog", back_populates="user", cascade="all, delete-orphan")
    auto_reply_training = relationship("AutoReplyTraining", back_populates="user", cascade="all, delete-orphan")
    post_logs = relationship("PostLog", back_populates="user", cascade="all, delete-orphan")
    platform_statuses = relationship("PlatformStatus", back_populates="user", cascade="all, delete-orphan")
    token_usage_logs = relationship("TokenUsageLog", back_populates="user", cascade="all, delete-orphan")
    error_logs = relationship("ErrorLog", back_populates="user", cascade="all, delete-orphan")
    webhook_delivery_logs = relationship("WebhookDeliveryLog", back_populates="user", cascade="all, delete-orphan")
    user_devices = relationship("UserDevice", back_populates="user", cascade="all, delete-orphan")
    login_history = relationship("LoginHistory", back_populates="user", cascade="all, delete-orphan")
    magic_links = relationship("MagicLink", back_populates="user", cascade="all, delete-orphan")
    smart_coin_wallet = relationship("SmartCoinWallet", back_populates="user", uselist=False, cascade="all, delete-orphan")
    smart_coin_transactions = relationship("SmartCoinTransaction", back_populates="user", cascade="all, delete-orphan")
    products = relationship("Product", back_populates="vendor", cascade="all, delete-orphan")
    live_sessions = relationship("LiveSession", back_populates="user", cascade="all, delete-orphan")
    chat_messages = relationship("ChatMessage", back_populates="sender", cascade="all, delete-orphan")
    messages = relationship("MessageLog", back_populates="user", cascade="all, delete-orphan")
    co_host_entries = relationship("CoHost", back_populates="user", cascade="all, delete-orphan")
    gift_fly_events = relationship("GiftFly", back_populates="user", cascade="all, delete-orphan")
    bots = relationship("UserBot", back_populates="user", cascade="all, delete-orphan")
    video_comments = relationship("VideoComment", back_populates="user", cascade="all, delete-orphan")
    video_views = relationship("VideoViewStat", back_populates="viewer", cascade="all, delete-orphan")
    badge_history = relationship("BadgeHistory", back_populates="user")


    def __repr__(self):
        return f"<User #{self.id} | {self.username} - {self.email}>"

# ✅ Delay heavy model imports to prevent circular references
from .social_media_post import SocialMediaPost
