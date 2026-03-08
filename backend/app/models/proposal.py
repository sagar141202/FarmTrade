from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base

class Proposal(Base):
    __tablename__ = "proposals"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("users.id"))
    crop_id = Column(Integer, ForeignKey("crops.id"))
    title = Column(String)
    description = Column(String)
    amount_requested = Column(Float)
    expected_yield = Column(Float)
    roi_percent = Column(Float)
    status = Column(String, default="draft")
    language = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    farmer = relationship("User", backref="proposals")
    crop = relationship("Crop", backref="proposals")