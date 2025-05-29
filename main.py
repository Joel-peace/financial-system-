from database.connection import session, create_tables
from models.author import Author
from models.book import Book
from models.review import Review

def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Author")
        print("2. Add Book")
        print("3. View Authors & Books")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            add_book()
        elif choice == '3':
            view_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def add_author():
    name = input("Enter author name: ").strip()
    if name:
        author = Author(name=name)
        session.add(author)
        session.commit()
        print("Author added.")
    else:
        print("Name cannot be empty.")

def add_book():
    authors = session.query(Author).all()
    if not authors:
        print("No authors found. Add authors first.")
        return
    print("Available authors:")
    for a in authors:
        print(f"{a.id}. {a.name}")
    try:
        author_id = int(input("Enter author ID: "))
        title = input("Enter book title: ").strip()
        if title:
            book = Book(title=title, author_id=author_id)
            session.add(book)
            session.commit()
            print("Book added.")
        else:
            print("Title cannot be empty.")
    except ValueError:
        print("Invalid input.")

def view_authors():
    authors = session.query(Author).all()
    for author in authors:
        print(f"\n{author.name}")
        for book in author.books:
            print(f"  - {book.title}")

if __name__ == "__main__":
    create_tables()
    menu()