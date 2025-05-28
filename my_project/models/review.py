from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="reviews")

    def __repr__(self):
        return f"Review({self.id}, {self.content})"
