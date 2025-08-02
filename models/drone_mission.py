from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class DroneMission(Base):
    """
    DroneMission model — manages autonomous or manual product delivery missions.
    """
    __tablename__ = "drone_missions"

    id = Column(Integer, primary_key=True, index=True)
    drone_id = Column(String, nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    destination = Column(String, nullable=False)
    # pending, in-transit, delivered, failed
    status = Column(String, default="pending")

    eta = Column(DateTime, nullable=True)
    initiated_by = Column(String, default="system")  # system/manual/user
    auto_mode = Column(Boolean, default=True)
    emergency = Column(Boolean, default=False)
    retry_attempts = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    # ForeignKey to User model
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # This connects DroneMission to User

    # Relationships
    product = relationship("Product")  # Optional: add back_populates if needed
    user = relationship("User", back_populates="drone_missions")  # Link DroneMission to User model

    def __repr__(self):
        return (
            f"<DroneMission(product_id={self.product_id}, "
            f"destination='{self.destination}', status='{self.status}')>"
        )
