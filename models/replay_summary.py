from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class ReplaySummary(Base):
    __tablename__ = "replay_summaries"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    summary_text = Column(Text, nullable=False)

    stream = relationship("LiveStream", back_populates="summary_ai")
