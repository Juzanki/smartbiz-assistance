# backend/models/order.py

from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class Order(Base):
    """
    Order model — tracks customer orders for specific products.
    """
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)
    product_id = Column(Integer, ForeignKey("products["id"]), nullable=False)

    quantity = Column(Integer, nullable=False, default=1)
    total = Column(Float, nullable=False)
    status = Column(String(20), default="pending")  # pending, paid, cancelled, delivered
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="orders")
    product = relationship("Product")

    def __repr__(self):
        return f"<Order(user_id={self.user_id}, product_id={self.product_id}, total={self.total})>"
