from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .profile import Profile

class Retirement(Base):
    __tablename__ = 'retirements'
    
    id = Column(Integer, primary_key=True)
    savings = Column(Float)
    contribution = Column(Float)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    
    profile = relationship("Profile", back_populates="retirement")
    
    def __repr__(self):
        return f"Retirement(id={self.id}, savings={self.savings})"
