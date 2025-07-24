from sqlalchemy import Column, Integer, String, DateTime, Boolean
from backend.db import Base


class PasswordResetCode(Base):
    __tablename__ = "password_reset_codes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    code = Column(String, index=True)
    is_used = Column(Boolean, default=False)
    expires_at = Column(DateTime)
