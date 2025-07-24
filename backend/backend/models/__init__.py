# === backend/models/__init__.py ===

# ✅ Base metadata (required for Alembic)
from backend.db import Base

# ✅ User model first (other models depend on it)
from .user import User

# 🔧 Core Activity & Settings
from .activity_score import ActivityScore
from .ai_bot_settings import AIBotSettings
from .api_key import APIKey
from .audit_log import AuditLog
from .auto_reply_training import AutoReplyTraining

# 💳 Billing & Transactions
from .billing_log import BillingLog
from .smart_coin_wallet import SmartCoinWallet
from .smart_coin_transaction import SmartCoinTransaction
from .gift_model import Gift
from .gift_movement import GiftMovement
from .gift_fly import GiftFly
from .gift_transaction import GiftTransaction  # ✅ Newly added

# 🛒 Commerce & Orders
from .order import Order
from .payment import Payment
from .product import Product

# 📣 Campaigns & Referrals
from .campaign import Campaign, CampaignAffiliate
from .referral_bonus import ReferralBonus
from .referral_log import ReferralLog

# 📊 Analytics & Logs
from .analytics import AnalyticsSnapshot
from .error_log import ErrorLog
from .token_usage_log import TokenUsageLog
from .injection_log import InjectionLog
from .search_log import SearchLog
from .post_log import PostLog
from .feedback import CustomerFeedback
from .login_history import LoginHistory
from .message import MessageLog, ScheduledMessage
from .notification import Notification
from .notification_preferences import NotificationPreference
from .webhook_delivery_log import WebhookDeliveryLog

# 🤖 Bots & AI
from .user_bot import UserBot
from .bot_package import BotPackage

# 👥 Users & Devices
from .user_device import UserDevice
from .customer import Customer
from .guests import Guest

# 📺 Streaming & Video
from .live_stream import LiveStream
from .live_session import LiveSession
from .recorded_stream import RecordedStream
from .replay_events import ReplayEvent
from .video_post import VideoPost

# 🪄 Magic, Loyalty & Subscriptions
from .magic_link import MagicLink
from .loyalty import LoyaltyPoint
from .subscription import SubscriptionPlan, UserSubscription

# 🔧 Support & Tickets
from .support import SupportTicket

# 🔐 Security & Access
from .password_reset import PasswordResetCode
from .platform_status import PlatformStatus

# 📌 Tags & Social Media
from .smart_tags import Tag
from .social_media_post import SocialMediaPost

# 👥 Co-hosting Features
from .co_host import CoHost
from .co_host_invite import CoHostInvite

# 📡 Connected Platforms
from .connected_platform import ConnectedPlatform

# ✈️ Drone/IoT Missions
from .drone_mission import DroneMission

# 🏅 Badges
from .badge_history import BadgeHistory  # ✅ For tracking badge assignments

# ✅ Settings
from .setting import Setting, Settings
