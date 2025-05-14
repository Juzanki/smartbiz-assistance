from backend.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    posts = relationship("SocialMediaPost", back_populates="user", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="user", cascade="all, delete-orphan")
    joined_campaigns = relationship("CampaignAffiliate", back_populates="user", cascade="all, delete-orphan")
    referrals = relationship("ReferralLog", back_populates="promoter", cascade="all, delete-orphan")
    support_tickets = relationship("SupportTicket", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="user", cascade="all, delete-orphan")
    subscriptions = relationship("UserSubscription", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    scheduled_messages = relationship("ScheduledMessage", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("Settings", back_populates="user", uselist=False)
    platforms = relationship("ConnectedPlatform", back_populates="user", cascade="all, delete-orphan")
    ai_bot_settings = relationship("AIBotSettings", back_populates="user", uselist=False)
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    loyalty_points = relationship("LoyaltyPoint", back_populates="user", cascade="all, delete-orphan")
    drone_missions = relationship("DroneMission", back_populates="user", cascade="all, delete-orphan")
    customers = relationship("Customer", back_populates="user", cascade="all, delete-orphan")
    analytics_snapshots = relationship("AnalyticsSnapshot", back_populates="user", cascade="all, delete-orphan")
    billing_logs = relationship("BillingLog", back_populates="user", cascade="all, delete-orphan")
    notification_preferences = relationship("NotificationPreference", back_populates="user", uselist=False, cascade="all, delete-orphan")
    customer_feedbacks = relationship("CustomerFeedback", back_populates="user", cascade="all, delete-orphan")
    activity_score = relationship("ActivityScore", back_populates="user", uselist=False, cascade="all, delete-orphan")
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

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
