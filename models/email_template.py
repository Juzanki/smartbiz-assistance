from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from backend.db import Base

class EmailTemplate(Base):
    __tablename__ = "email_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)  # e.g., 'payment_success'
    subject = Column(String(200), nullable=False)
    html_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
