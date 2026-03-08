from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    location = Column(String)
    area_acres = Column(Float)
    soil_type = Column(String)
    irrigation_type = Column(String)
    lat = Column(Float)
    lng = Column(Float)

    owner = relationship("User", backref="farms")