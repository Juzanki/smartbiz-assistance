from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.db import Base

class LiveProduct(Base):
    __tablename__ = "live_products"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(String, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))  # Unganisha na bidhaa halisi
    showcased_at = Column(DateTime(timezone=True), server_default=func.now())
