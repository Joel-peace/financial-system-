import sys
from sqlalchemy.exc import SQLAlchemyError
from finance_tracker.models import Profile, Retirement, Life, init_db, session
from finance_tracker.helpers.seed import seed_database
import ipdb

def get_valid_input(prompt, input_type=float, min_value=0):
    """Get validated user input with error handling."""
    while True:
        try:
            value = input_type(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

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
    try:
        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty")
            return
            
        age = get_valid_input("Age: ", int, 1)
        income = get_valid_input("Annual Income: $", float)
        
        profile = Profile(name=name, age=age, income=income)
        session.add(profile)
        session.commit()
        print(f"Created profile for {name} (ID: {profile.id})")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database error: {e}")

def view_profiles():
    print("\nAll Profiles")
    try:
        profiles = session.query(Profile).all()
        
        if not profiles:
            print("No profiles found")
            return
        
        for profile in profiles:
            print(f"\nID: {profile.id} | {profile.name} (Age: {profile.age})")
            print(f"Annual Income: ${profile.income:,.2f}")
            
            if profile.retirement:
                r = profile.retirement
                print(f"  Retirement: ${r.savings:,.2f} saved | ${r.contribution:,.2f}/yr contribution")
            
            if profile.life:
                l = profile.life
                print(f"  Life Insurance: ${l.coverage:,.2f} {l.policy_type} policy | ${l.premium:,.2f}/yr")
    except SQLAlchemyError as e:
        print(f"Database error: {e}")

def add_retirement():
    print("\nAdd Retirement Plan")
    view_profiles()
    try:
        profile_id = get_valid_input("\nEnter Profile ID: ", int, 1)
        profile = session.get(Profile, profile_id)
        
        if not profile:
            print("Profile not found")
            return
        
        savings = get_valid_input("Current Savings: $", float)
        contribution = get_valid_input("Annual Contribution: $", float)
        
        if profile.retirement:
            print("This profile already has a retirement plan")
            return
            
        retirement = Retirement(savings=savings, contribution=contribution, profile=profile)
        session.add(retirement)
        session.commit()
        print("Retirement plan added")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database error: {e}")

def add_life_insurance():
    print("\nAdd Life Insurance")
    view_profiles()
    try:
        profile_id = get_valid_input("\nEnter Profile ID: ", int, 1)
        profile = session.get(Profile, profile_id)
        
        if not profile:
            print("Profile not found")
            return
        
        coverage = get_valid_input("Coverage Amount: $", float)
        premium = get_valid_input("Annual Premium: $", float)
        policy_type = input("Policy Type (Term/Whole): ").strip().capitalize()
        
        if policy_type not in ["Term", "Whole"]:
            print("Policy type must be either 'Term' or 'Whole'")
            return
            
        if profile.life:
            print("This profile already has life insurance")
            return
            
        life = Life(coverage=coverage, premium=premium, policy_type=policy_type, profile=profile)
        session.add(life)
        session.commit()
        print("Life insurance added")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Database error: {e}")

def main():
    init_db()
    print("Database initialized!\n")
    
    while True:
        try:
            print_menu()
            choice = input("\nEnter choice: ").strip()
            
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
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()