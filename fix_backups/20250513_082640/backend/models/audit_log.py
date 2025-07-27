# backend/models/audit_log.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class AuditLog(Base):
    """
    AuditLog model for tracking user activities within the SmartBiz Assistance system.
    Stores metadata like action type, IP address, and optional description.
    """
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)
    action = Column(String(100), nullable=False)  # e.g., "login", "update_profile", "delete_order"
    ip_address = Column(String(45), nullable=True)  # IPv6 compatible
    description = Column(Text, nullable=True)  # Optional details
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")

    def __repr__(self):
        return f"<AuditLog(user_id={self.user_id}, action='{self.action}', ip='{self.ip_address}')>"
