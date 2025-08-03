# === backend/models/campaign.py ===

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from backend.db import Base


class Campaign(Base):
    """
    Campaign model — defines promotional campaigns for products or services.
    """
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    product_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    affiliates = relationship(
        "CampaignAffiliate",
        back_populates="campaign",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Campaign(title='{self.title}', product='{self.product_name}')>"


class CampaignAffiliate(Base):
    """
    CampaignAffiliate model — links users to the campaigns they join.
    """
    __tablename__ = "campaign_affiliates"
    __table_args__ = (
        UniqueConstraint('campaign_id', 'user_id', name='uq_campaign_user'),
    )

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)

    campaign = relationship("Campaign", back_populates="affiliates")
    user = relationship("User", back_populates="joined_campaigns")

    def __repr__(self):
        return f"<CampaignAffiliate(campaign_id={self.campaign_id}, user_id={self.user_id})>"
