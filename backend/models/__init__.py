# === 📦 backend/models/__init__.py ===
# Central model registry for SQLAlchemy + Alembic

# ✅ Base metadata (required by Alembic)
from backend.db import Base

# 👤 Users & Identity
from .user import User
from .user_device import UserDevice
from .customer import Customer
from .guests import Guest

# 🛍️ Products & Orders
from .product import Product
from .order import Order
from .payment import Payment

# 💳 Coins & Wallets
from .smart_coin_wallet import SmartCoinWallet
from .smart_coin_transaction import SmartCoinTransaction

# 🎁 Gifts & Transactions
from .gift_model import Gift
from .gift_transaction import GiftTransaction
from .gift_movement import GiftMovement
from .gift_fly import GiftFly

# 📺 Streaming & Videos
from .live_stream import LiveStream
from .live_session import LiveSession
from .recorded_stream import RecordedStream
from .replay_events import ReplayEvent
from .video_post import VideoPost

# 🤖 Bots & AI
from .user_bot import UserBot
from .bot_package import BotPackage
from .ai_bot_settings import AIBotSettings
from .auto_reply_training import AutoReplyTraining

# 📣 Campaigns & Referrals
from .campaign import Campaign, CampaignAffiliate
from .referral_bonus import ReferralBonus
from .referral_log import ReferralLog

# 🔔 Notifications & Messaging
from .notification import Notification
from .notification_preferences import NotificationPreference
from .message import MessageLog, ScheduledMessage

# 📊 Analytics & Logs
from .analytics import AnalyticsSnapshot
from .error_log import ErrorLog
from .token_usage_log import TokenUsageLog
from .injection_log import InjectionLog
from .search_log import SearchLog
from .post_log import PostLog
from .feedback import CustomerFeedback
from .login_history import LoginHistory
from .webhook_delivery_log import WebhookDeliveryLog

# ⚙️ Core Utilities & Admin
from .setting import Setting, Settings
from .api_key import APIKey
from .audit_log import AuditLog
from .platform_status import PlatformStatus

# 🪄 Magic, Loyalty & Subscription
from .magic_link import MagicLink
from .loyalty import LoyaltyPoint
from .subscription import SubscriptionPlan, UserSubscription

# 🧰 Support & Tickets
from .support import SupportTicket

# 🏷️ Tags & Social Media
from .smart_tags import Tag
from .social_media_post import SocialMediaPost

# 👥 Co-hosting
from .co_host import CoHost
from .co_host_invite import CoHostInvite

# 🌐 Connected Platforms
from .connected_platform import ConnectedPlatform

# ✈️ Drone & IoT
from .drone_mission import DroneMission

# 🏅 Badges & History
from .badge_history import BadgeHistory

# 🧠 Activity Scores
from .activity_score import ActivityScore

# 🔐 Security
from .password_reset import PasswordResetCode
