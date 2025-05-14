# === backend/models/post.py ===
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from backend.db import Base
from datetime import datetime

# --- Social Media Post Table ---


class SocialMediaPost(Base):
    __tablename__ = "social_posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False)  # ✅ FIXED
    # ✅ limited length
    platform = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    media_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# --- General Blog Post Table ---


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    # ✅ Added max length + nullable
    title = Column(String(200), index=True, nullable=False)
    content = Column(Text, nullable=False)
    is_published = Column(Boolean, default=True)
    created_at = Column(
        DateTime,
        default=datetime.utcnow)             # ✅ Consistency
