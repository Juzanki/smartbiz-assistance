from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class TaskFailureLog(Base):
    __tablename__ = "task_failure_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("scheduled_tasks.id"), nullable=False)
    error_message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    task = relationship("ScheduledTask", back_populates="failure_logs")
