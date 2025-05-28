from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    from models.author import Author
    from models.book import Book
    from models.review import Review
    Base.metadata.create_all(engine)
