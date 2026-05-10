from sqlalchemy import Column, Integer, String, DateTime, JSON, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base


class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    scans = relationship(
        "Scan",
        back_populates="site",
        cascade="all, delete-orphan",
        order_by="Scan.timestamp.desc()"
    )

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    raw_data = Column(JSON, nullable=True)
    ai_report = Column(Text, nullable=True)

    site = relationship("Site", back_populates="scans")
