from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from backend.db import Base


class SmartCoinWallet(Base):
    """
    💰 SmartCoinWallet - Manages user's coin balance, theme preferences, and wallet settings.
    """

    __tablename__ = "coin_wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Coin logic
    balance = Column(Float, default=0.0)
    currency = Column(String, default="SBZ")  # SmartBiz Coins
    is_active = Column(Boolean, default=True)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # UI Preferences
    theme = Column(String, default="classic")     # classic, futuristic, etc.
    color_mode = Column(String, default="dark")   # dark or light

    # Relationship
    user = relationship("User", back_populates="smart_coin_wallet")

    # Wallet operations
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def has_enough(self, amount: float) -> bool:
        return self.balance >= amount

    def __repr__(self):
        return f"<SmartCoinWallet #{self.id} User:{self.user_id} Balance:{self.balance} {self.currency}>"
