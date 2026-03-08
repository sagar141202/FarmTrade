from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base

class Crop(Base):
    __tablename__ = "crops"
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    crop_name = Column(String)
    season = Column(String)
    sowing_date = Column(Date, nullable=True)
    harvest_date = Column(Date, nullable=True)
    area_planted = Column(Float)
    actual_yield = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    farm = relationship("Farm", backref="crops")