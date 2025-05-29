Personal Finance Tracker CLI
A simple command-line application to manage financial profiles, retirement plans, and life insurance policies.

Features
Create and view financial profiles

Add retirement savings plans

Manage life insurance policies

Preload demo data

Interactive debugging

How to Run
Open terminal in project folder

Set up environment:

bash
python -m venv venv
source venv/bin/activate
pip install sqlalchemy ipdb
Start the application:

bash
python -m finance_tracker.cli.main
Menu Options
1. Create Profile        # Add new financial profile
2. View All Profiles     # Show all profiles with details
3. Add Retirement Plan   # Add savings plan to a profile
4. Add Life Insurance    # Add insurance policy to a profile
5. Seed Database         # Load demo data (3 sample profiles)
6. Debug                # Open interactive debugger
7. Exit                 # Quit application
Run Tests
bash
pytest tests/
Sample Data
After selecting "5. Seed Database", you'll get:

Alice Smith (35, $85k income)

Bob Johnson (42, $110k income)

Charlie Brown (28, $75k income)

Project Structure
finance_tracker/
├── cli/          # Command-line interface
├── helpers/      # Database utilities
├── models/       # Database models
tests/            # Test cases
finance.db        # Database file
Troubleshooting
If you get import errors:

bash
PYTHONPATH=. python -m finance_tracker.cli.main
To reset database:

bash
rm finance.db
python -c "from finance_tracker.models import init_db; init_db()"