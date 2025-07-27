from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class SearchLog(Base):
    """
    Records every search query made by users in SmartBiz dashboard or AI bots.
    Useful for insights, AI improvement, and trending analysis.
    """
    __tablename__ = "search_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    query = Column(String(255), nullable=False)
    source = Column(String(50), default="dashboard")  # dashboard, assistant, mobile, etc.
    results_count = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="search_logs")

    def __repr__(self):
        return f"<SearchLog(user_id={self.user_id}, query='{self.query}', results={self.results_count})>"
