from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    income = Column(Integer, nullable=False)
    
    retirement = relationship("Retirement", uselist=False, back_populates="profile")
    life = relationship("Life", uselist=False, back_populates="profile")
    
    def __repr__(self):
        return f"Profile(id={self.id}, name='{self.name}')"
