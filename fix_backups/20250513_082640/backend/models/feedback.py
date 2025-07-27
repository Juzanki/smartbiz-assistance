from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class CustomerFeedback(Base):
    """
    Captures feedback submitted by customers for a given business user.
    Useful for quality improvement, analytics, and support.
    """
    __tablename__ = "customer_feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)  # Business owner

    customer_name = Column(String(100), nullable=True)
    contact = Column(String(100), nullable=True)
    feedback_type = Column(String(50), default="general")  # e.g., complaint, praise, suggestion
    message = Column(Text, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="customer_feedbacks")

    def __repr__(self):
        return f"<CustomerFeedback(user_id={self.user_id}, type='{self.feedback_type}')>"
