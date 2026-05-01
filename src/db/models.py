from sqlalchemy import Column, Integer, String
from .database import Base

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)