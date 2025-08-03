from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime

class SocialMediaPost(Base):
    __tablename__ = 'social_posts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    platform = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    media_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<SocialMediaPost(id={self.id}, user_id={self.user_id}, platform={self.platform}, created_at={self.created_at})>"
