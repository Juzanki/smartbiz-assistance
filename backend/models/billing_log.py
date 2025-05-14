from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class BillingLog(Base):
    """
    Records all billing and transaction activities for users,
    including manual charges, plan upgrades, gift redemptions, etc.
    """
    __tablename__ = "billing_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # e.g., subscription, gift, refund
    type = Column(String(50), nullable=False)
    reference = Column(String(100), unique=True, nullable=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default="TZS")
    description = Column(String(255), nullable=True)
    status = Column(String(20), default="success")  # success, failed, refunded
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="billing_logs")

    def __repr__(self):
        return f"<BillingLog(user_id={self.user_id}, type='{self.type}', amount={self.amount})>"
