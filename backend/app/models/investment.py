from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base

class Investment(Base):
    __tablename__ = "investments"
    id = Column(Integer, primary_key=True, index=True)
    investor_id = Column(Integer, ForeignKey("users.id"))
    proposal_id = Column(Integer, ForeignKey("proposals.id"))
    amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    investor = relationship("User", backref="investments")
    proposal = relationship("Proposal", backref="investments")