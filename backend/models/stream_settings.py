from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class StreamSettings(Base):
    __tablename__ = "stream_settings"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), unique=True, nullable=False)
    camera_on = Column(Boolean, default=True)
    mic_on = Column(Boolean, default=True)

    stream = relationship("LiveStream", back_populates="settings")
