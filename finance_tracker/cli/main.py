import sys
from sqlalchemy.exc import SQLAlchemyError
from finance_tracker.models import Profile, Retirement, Life, init_db, session
from finance_tracker.helpers.seed import seed_database
import ipdb

def print_menu():
    print("\nPersonal Finance Tracker")
    print("1. Create Profile")
    print("2. View All Profiles")
    print("3. Add Retirement Plan")
    print("4. Add Life Insurance")
    print("5. Seed Database (Demo Data)")
    print("6. Debug")
    print("7. Exit")

def create_profile():
    print("\nCreate New Profile")
    name = input("Name: ")
    age = int(input("Age: "))
    income = float(input("Annual Income: $"))
    
    profile = Profile(name=name, age=age, income=income)
    session.add(profile)
    session.commit()
    print(f"Created profile for {name} (ID: {profile.id})")

# ... [rest of the CLI functions without emojis] ...

def main():
    init_db()
    while True:
        print_menu()
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            create_profile()
        elif choice == "2":
            view_profiles()
        elif choice == "3":
            add_retirement()
        elif choice == "4":
            add_life_insurance()
        elif choice == "5":
            seed_database()
            print("Database seeded with demo data")
        elif choice == "6":
            print("Entering debug mode...")
            ipdb.set_trace()
        elif choice == "7":
            print("\nExiting application")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
