from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.db import Base
from datetime import datetime

class LiveStream(Base):
    __tablename__ = "live_streams"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=True)
    title = Column(String, nullable=True)
    goal = Column(String, nullable=True)
    is_featured = Column(Boolean, default=False)
    is_recorded = Column(Boolean, default=False)
    viewers_count = Column(Integer, default=0)
    likes_count = Column(Integer, default=0)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    ended_at = Column(DateTime(timezone=True), nullable=True)
    last_active_at = Column(DateTime, default=datetime.utcnow, nullable=True)

    # === Relationships ===
    cohost_invites = relationship("CoHostInvite", back_populates="stream", cascade="all, delete-orphan")
    cohosts = relationship("CoHost", back_populates="stream", cascade="all, delete-orphan")
    gift_fly_events = relationship("GiftFly", back_populates="stream", cascade="all, delete-orphan")
    viewers = relationship("LiveViewer", back_populates="stream", cascade="all, delete-orphan")
    summary_ai = relationship("ReplaySummary", back_populates="stream", cascade="all, delete-orphan", uselist=False)
    captions = relationship("ReplayCaption", back_populates="stream", cascade="all, delete-orphan")
    auto_title = relationship("ReplayTitle", back_populates="stream", cascade="all, delete-orphan", uselist=False)
    analytics_entries = relationship("ReplayAnalytics", back_populates="stream", cascade="all, delete-orphan")
    gift_markers = relationship("GiftMarker", back_populates="stream", cascade="all, delete-orphan")
    recorded_streams = relationship("RecordedStream", back_populates="stream", cascade="all, delete-orphan")

    # ⛔️ Removed the faulty relationship:
    # settings = relationship("System.Collections.Hashtable.from", ...) ❌

