from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class ErrorLog(Base):
    """
    Stores user-facing or system errors for diagnosis, debugging, and analytics.
    Can be triggered from frontend, backend, or integrations.
    """
    __tablename__ = "error_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # nullable in case it's system-level

    # frontend, backend, integration
    source = Column(String(50), default="backend")
    error_type = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    trace = Column(Text, nullable=True)  # optional: traceback or extra context

    occurred_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="error_logs")

    def __repr__(self):
        return f"<ErrorLog(source='{self.source}', type='{self.error_type}')>"
