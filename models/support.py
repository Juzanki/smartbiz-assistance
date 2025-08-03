# backend/models/support.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class SupportTicket(Base):
    """
    SupportTicket model — represents user-submitted support or help requests.
    """
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    subject = Column(String(150), nullable=False)
    type = Column(String(50), nullable=False)  # e.g., bug, payment, feedback
    description = Column(Text, nullable=False)
    attachment = Column(String, nullable=True)  # file path or URL
    status = Column(String(20), default="open")  # open, resolved, closed
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="support_tickets")

    def __repr__(self):
        return f"<SupportTicket(subject='{self.subject}', status='{self.status}')>"
