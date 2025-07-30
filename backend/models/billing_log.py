from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from backend.db import Base
import enum


class BillingStatus(str, enum.Enum):
    success = "success"
    failed = "failed"
    refunded = "refunded"


class BillingLog(Base):
    """
    🔐 BillingLog Model
    Tracks all user billing and transaction events,
    including top-ups, subscriptions, purchases, gifts, and refunds.
    """

    __tablename__ = "billing_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    type = Column(String(50), nullable=False)  # e.g., subscription, refund, gift
    reference = Column(String(100), unique=True, nullable=True)  # optional external ID
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default="TZS")  # e.g., TZS, USD
    description = Column(String(255), nullable=True)

    status = Column(Enum(BillingStatus), default=BillingStatus.success, nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship to User (backref in User must be: billing_logs = relationship(...))
    user = relationship("User", back_populates="billing_logs")

    def __repr__(self):
        return f"<BillingLog user={self.user_id}, type='{self.type}', amount={self.amount}, status={self.status}>"
