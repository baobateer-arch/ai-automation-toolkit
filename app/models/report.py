from sqlalchemy import Column, Integer, String, DateTime, JSON, func
from app.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    summary = Column(String, nullable=False, default="")
    key_points = Column(JSON, nullable=False, default=list)
    risks = Column(JSON, nullable=False, default=list)
    suggestions = Column(JSON, nullable=False, default=list)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
