from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class WebhookDeliveryLog(Base):
    """
    Logs delivery of outbound webhooks for auditing and diagnostics.
    Tracks success/failure, retries, and responses from external systems.
    """
    __tablename__ = "webhook_delivery_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    target_url = Column(String(255), nullable=False)
    # e.g., order.created, payment.success
    event_type = Column(String(100), nullable=False)
    payload = Column(Text, nullable=True)
    response_code = Column(String(10), nullable=True)
    response_body = Column(Text, nullable=True)
    success = Column(Boolean, default=False)
    attempt = Column(Integer, default=1)
    sent_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="webhook_delivery_logs")

    def __repr__(self):
        return (
            f"<WebhookDeliveryLog(user_id={self.user_id}, event='{self.event_type}', success={self.success})>"
        )
