from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class SmartCoinTransaction(Base):
    """
    Tracks every coin transaction — earned, spent, transferred, or withdrawn.
    Linked to SmartCoinWallet and user.
    """
    __tablename__ = "smart_coin_transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    wallet_id = Column(Integer, ForeignKey("smart_coin_wallets.id"), nullable=False)

    type = Column(String(50), nullable=False)  # earn, spend, gift, withdraw
    amount = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    # completed, pending, failed
    status = Column(String(20), default="completed")

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="smart_coin_transactions")
    wallet = relationship("SmartCoinWallet", backref="transactions")

    def __repr__(self):
        return (
            f"<SmartCoinTransaction(user_id={self.user_id}, type='{self.type}', amount={self.amount})>"
        )
