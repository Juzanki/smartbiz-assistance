# backend/models/subscription.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.db import Base


class SubscriptionPlan(Base):
    """
    Defines available packages such as Free, Pro, Business.
    """
    __tablename__ = "subscription_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    duration_days = Column(Integer, nullable=False)  # e.g., 30, 90, 365
    description = Column(String(255), nullable=True)

    # Optional: Link to all users on this plan (if needed)
    subscriptions = relationship("UserSubscription", back_populates="plan", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<SubscriptionPlan(name='{self["name"]', price={self.price})>"


class UserSubscription(Base):
    """
    Tracks a user's subscription history and active plan status.
    """
    __tablename__ = "user_subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)
    plan_id = Column(Integer, ForeignKey("subscription_plans["id"]), nullable=False)

    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="subscriptions")
    plan = relationship("SubscriptionPlan", back_populates="subscriptions")

    def __repr__(self):
        return f"<UserSubscription(user_id={self.user_id}, plan_id={self.plan_id}, active={self.is_active})>"
