from sqlalchemy import Column, Integer, String, Date, Float, Boolean, DateTime
from datetime import datetime
from app.database import Base

class PriceReport(Base):
    __tablename__ = "price_reports"
    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String)
    market_name = Column(String)
    state = Column(String)
    date = Column(Date)
    modal_price = Column(Float)
    min_price = Column(Float)
    max_price = Column(Float)
    is_anomaly = Column(Boolean, default=False)
    anomaly_score = Column(Float, nullable=True)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)