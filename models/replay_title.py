from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class ReplayTitle(Base):
    __tablename__ = "replay_titles"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    generated_title = Column(String, nullable=False)

    stream = relationship("LiveStream", back_populates="auto_title")
