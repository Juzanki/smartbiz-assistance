from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db import Base

class Product(Base):
    """
    Product model — defines business products or services for sale/display.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)  # Name cannot be null
    description = Column(Text, nullable=True)  # Description is optional
    price = Column(Float, nullable=False)  # Price cannot be null
    is_available = Column(Boolean, default=True)  # Default to available
    vendor_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Ensure vendor_id is not null
    created_at = Column(DateTime, default=datetime.utcnow)  # Automatically set the current time on creation

    # Define the relationship between Product and User (vendor)
    vendor = relationship("User", back_populates="products")

    # Relationship with Order (reverse side of the order-product relationship)
    orders = relationship("Order", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, vendor_id={self.vendor_id})>"
