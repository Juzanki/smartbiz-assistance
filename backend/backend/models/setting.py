# backend/models/setting.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class Setting(Base):
    """
    Setting model — stores global app-wide configurations as key-value pairs.
    """
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Setting(key='{self.key}', value='{self.value}')>"


class Settings(Base):
    """
    Settings model — user-specific configuration settings (branding, language, etc.).
    """
    __tablename__ = "user_settings"
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    business_name = Column(String, nullable=False)
    tagline = Column(String, nullable=True)
    language = Column(String, nullable=False, default="en")
    logo_url = Column(String, nullable=True)
    primary_color = Column(String, default="#0d6efd")
    secondary_color = Column(String, default="#6c757d")
    timezone = Column(String, default="Africa/Dar_es_Salaam")
    currency = Column(String, default="TZS")
    enable_custom_domain = Column(Boolean, default=False)

    user = relationship("User", back_populates="settings")

    def __repr__(self):
        return f"<Settings(user_id={self.user_id}, language='{self.language}')>"
