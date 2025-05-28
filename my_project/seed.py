from database.connection import session, create_tables
from models.author import Author
from models.book import Book

create_tables()

author1 = Author(name="J.K. Rowling")
author2 = Author(name="George R.R. Martin")

book1 = Book(title="Harry Potter", author=author1)
book2 = Book(title="Game of Thrones", author=author2)

session.add_all([author1, author2, book1, book2])
session.commit()

print("Seed data inserted.")
