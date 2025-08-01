from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class RechargeTransaction(Base):
    __tablename__ = "recharge_transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    method = Column(String, nullable=False)  # e.g., "mpesa", "paypal", "voucher"
    status = Column(String, default="pending")  # pending, success, failed
    reference = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="recharges")
