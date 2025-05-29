from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .profile import Profile

class Life(Base):
    __tablename__ = 'life_insurances'
    
    id = Column(Integer, primary_key=True)
    coverage = Column(Float)
    premium = Column(Float)
    policy_type = Column(String)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    
    profile = relationship("Profile", back_populates="life")
    
    def __repr__(self):
        return f"Life(id={self.id}, coverage={self.coverage})"
