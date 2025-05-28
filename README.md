Library Management System
Overview
The Library Management System is a command-line interface (CLI) application built using Python and SQLAlchemy. It enables users to:

Add authors to a database

Add books and associate them with authors

View a list of all authors and the books they have written

This project is designed to demonstrate mastery of Python fundamentals, object-relational mapping (ORM), modular code design, and CLI interaction.

Features
Clean and modular project architecture

SQLite database integration using SQLAlchemy

Create, Read operations for authors and books

User-friendly CLI interface for easy navigation

Persistent data storage

Technologies Used
Python 3.8+

SQLAlchemy (ORM)

SQLite (Database)

Project Structure
bash
Copy
Edit
phase-3finalproject/
├── my_project/
│   ├── cli/
│   │   └── main.py              # Main CLI menu and user interaction
│   ├── database/
│   │   └── connection.py        # Handles database engine and table creation
│   └── models/
│       ├── author.py            # Author model definition
│       ├── book.py              # Book model definition
│       └── review.py            # Review model (optional)
Installation Guide
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
Step 2: Set Up a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
If a requirements.txt file is provided:

bash
Copy
Edit
pip install -r requirements.txt
Or install SQLAlchemy manually:

bash
Copy
Edit
pip install SQLAlchemy
How to Run the Project
Step 1: Navigate to the Main CLI Directory
bash
Copy
Edit
cd my_project
Step 2: Run the Application
bash
Copy
Edit
python -m cli.main
Output:
Once the application runs, you will see a CLI menu like this:

pgsql
Copy
Edit
Library Management System
1. Add Author
2. Add Book
3. View Authors & Books
4. Exit
How to Navigate the CLI
1. Add Author
Select option 1

Input the author's name

The author will be saved to the database

Example:

yaml
Copy
Edit
Enter author name: George Orwell
Author added.
2. Add Book
Select option 2

The system will list all available authors

Enter the corresponding author ID

Input the book title

The book will be saved and linked to the author

Example:

yaml
Copy
Edit
Available authors:
1. George Orwell
Enter author ID: 1
Enter book title: 1984
Book added.
3. View Authors & Books
Select option 3

The system will display all authors and the books they've written

Example Output:

markdown
Copy
Edit
George Orwell
  - 1984
  - Animal Farm
4. Exit
Select option 4 to exit the CLI

