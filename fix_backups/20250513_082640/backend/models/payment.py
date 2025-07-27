# backend/models/payment.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class Payment(Base):
    """
    Payment model — records of user payments for subscriptions or services.
    """
    __tablename__ = "payments"

    id = Column(String, primary_key=True, index=True)  # UUID string
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    method = Column(String(30), default="mpesa")  # e.g., mpesa, paypal, stripe
    amount = Column(Float, nullable=False)
    status = Column(String(20), default="pending")  # pending, success, failed
    phone_number = Column(String(20), nullable=False)
    reference = Column(String(100), unique=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="payments")

    def __repr__(self):
        return f"<Payment(user_id={self.user_id}, amount={self.amount}, status='{self["status"]')>"
