# === backend/models/post.py ===
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey,Boolean
from backend.db import Base
from datetime import datetime

class SocialMediaPost(Base):
    __tablename__ = "social_posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]))
    platform = Column(String)
    content = Column(Text)
    media_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    is_published = Column(Boolean, default=True)
