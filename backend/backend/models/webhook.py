from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class WebhookEndpoint(Base):
    __tablename__ = "webhook_endpoints"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    url = Column(String, nullable=False)
    secret = Column(String, nullable=True)  # for signing payload
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="webhooks")
    deliveries = relationship("WebhookDeliveryLog", back_populates="endpoint", cascade="all, delete-orphan")

class WebhookDeliveryLog(Base):
    __tablename__ = "webhook_delivery_logs"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("webhook_endpoints.id"))
    payload = Column(String, nullable=False)
    response_code = Column(Integer, nullable=True)
    success = Column(Boolean, default=False)
    attempts = Column(Integer, default=1)
    error_message = Column(String, nullable=True)
    delivered_at = Column(DateTime, default=datetime.utcnow)

    endpoint = relationship("WebhookEndpoint", back_populates="deliveries")
