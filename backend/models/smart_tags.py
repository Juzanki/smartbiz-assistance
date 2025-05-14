from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from backend.db import Base

# Association table (many-to-many): Customer ↔ Tag
customer_tags = Table(
    "customer_tags",
    Base.metadata,
    Column("customer_id", Integer, ForeignKey("customers.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)


class Tag(Base):
    """
    Tags created by a user to categorize or segment their customers.
    """
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)  # e.g., "VIP", "Hot Lead"
    color = Column(String(10), default="#00A8E8")  # Optional for frontend
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="tags")
    customers = relationship(
        "Customer",
        secondary=customer_tags,
        back_populates="tags"
    )

    def __repr__(self):
        return f"<Tag(name='{self.name}', user_id={self.user_id})>"
