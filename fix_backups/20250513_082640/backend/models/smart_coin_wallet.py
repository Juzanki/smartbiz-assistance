from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class SmartCoinWallet(Base):
    """
    Stores wallet balance and coin type for each user.
    Can support multiple internal currencies like SmartCoin or JuzankiCoin.
    """
    __tablename__ = "smart_coin_wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    coin_type = Column(String(50), default="SmartCoin")  # SmartCoin, JuzankiCoin, etc.
    balance = Column(Float, default=0.0)
    total_earned = Column(Float, default=0.0)
    total_spent = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="smart_coin_wallet")

    def __repr__(self):
        return f"<SmartCoinWallet(user_id={self.user_id}, coin='{self.coin_type}', balance={self.balance})>"
