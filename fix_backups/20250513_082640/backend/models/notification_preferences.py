from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class NotificationPreference(Base):
    """
    Stores each user's notification preferences — which channel(s) they want alerts from.
    """
    __tablename__ = "notification_preferences"

    user_id = Column(Integer, ForeignKey("users["id"]), primary_key=True)

    enable_email = Column(Boolean, default=True)
    enable_sms = Column(Boolean, default=False)
    enable_push = Column(Boolean, default=True)
    enable_critical_only = Column(Boolean, default=False)  # only receive urgent alerts

    user = relationship("User", back_populates="notification_preferences")

    def __repr__(self):
        return f"<NotificationPreference(user_id={self.user_id}, email={self.enable_email}, sms={self.enable_sms})>"
