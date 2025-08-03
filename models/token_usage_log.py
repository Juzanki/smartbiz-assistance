from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class TokenUsageLog(Base):
    __tablename__ = "token_usage_logs"
    __table_args__ = {'extend_existing': True}  # Epuka error ya duplicate table definition

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token_type = Column(String(50), nullable=False)  # e.g., "access", "refresh", "magic_link"
    ip_address = Column(String(100), nullable=True)  # optional, for logging security
    device_info = Column(String(255), nullable=True)  # optional: "Chrome on Windows 10"
    used_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to user
    user = relationship("User", back_populates="token_usage_logs")

    def __repr__(self):
        return f"<TokenUsageLog(user_id={self.user_id}, type={self.token_type}, used_at={self.used_at})>"
