from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from backend.db import Base

class ShareActivity(Base):
    __tablename__ = "share_activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)          # Aliyeshiriki
    room_id = Column(String, index=True)           # Stream iliyoshirikiwa
    platform = Column(String)                      # Mfano: whatsapp, facebook, link
    content_type = Column(String, default="stream")  # stream / product / goal / post
    shared_at = Column(DateTime(timezone=True), server_default=func.now())
