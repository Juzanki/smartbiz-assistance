from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class RecordedStream(Base):
    __tablename__ = "recorded_streams"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    file_path = Column(String, nullable=False)
    duration = Column(Float, default=0.0)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # ? One-to-One or One-to-Many to VideoPost
    video_post = relationship("VideoPost", back_populates="recorded_stream", uselist=False)

    # ? Link to LiveStream
    stream = relationship("LiveStream", back_populates="recorded_streams")
