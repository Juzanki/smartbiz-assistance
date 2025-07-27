from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.db import Base


class Customer(Base):
    """
    Customer model — end users served by SmartBiz businesses.
    Linked to a business owner (user_id).
    """
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)  # Business owner

    name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False, unique=True)
    email = Column(String(100), nullable=True)
    region = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="customers")

    def __repr__(self):
        return f"<Customer(name='{self["name"]', phone='{self.phone_number}')>"
tags = relationship("Tag", secondary="customer_tags", back_populates="customers")
