from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class TokenUsageLog(Base):
    """
    Tracks how tokens or API keys are used per user.
    Useful for monitoring limits, billing, and abuse prevention.
    """
    __tablename__ = "token_usage_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    token_type = Column(String(50), default="openai")  # openai, sms, smartbiz, custom
    action = Column(String(100), nullable=False)  # e.g., chat_completion, image_gen, sms_send
    token_count = Column(Float, default=0.0)
    cost_estimate = Column(Float, default=0.0)  # estimated cost in TZS/USD

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="token_usage_logs")

    def __repr__(self):
        return f"<TokenUsageLog(user_id={self.user_id}, action='{self.action}', tokens={self.token_count})>"
