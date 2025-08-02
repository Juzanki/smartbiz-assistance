from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class Wallet(Base):
    __tablename__ = "wallets"
    # Auto-added back_populates
    transactions = relationship("System.Collections.Hashtable.from", back_populates="Wallet", cascade="all, delete-orphan")

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    balance = Column(Float, default=0.0)  # Real money
    smartcoin = Column(Float, default=0.0)  # Internal credits
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="wallet")

class WalletTransaction(Base):
    __tablename__ = "wallet_transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    type = Column(String(50))  # deposit, withdraw, convert, transfer
    amount = Column(Float)
    currency = Column(String(10), default="TZS")  # Or "SmartCoin"
    status = Column(String(20), default="success")  # success, failed, pending
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    wallet = relationship("Wallet", back_populates="transactions")
