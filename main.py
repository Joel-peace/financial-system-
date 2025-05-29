# Replace the CLI main file with complete implementation
cat > finance_tracker/cli/main.py << 'EOL'
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

def view_profiles():
    print("\nAll Profiles")
    profiles = session.query(Profile).all()
    
    if not profiles:
        print("No profiles found")
        return
    
    for profile in profiles:
        print(f"\nID: {profile.id} | {profile.name} (Age: {profile.age})")
        print(f"Annual Income: ${profile.income}")
        
        if profile.retirement:
            r = profile.retirement
            print(f"  Retirement: ${r.savings} saved | ${r.contribution}/yr contribution")
        
        if profile.life:
            l = profile.life
            print(f"  Life Insurance: ${l.coverage} {l.policy_type} policy | ${l.premium}/yr")

def add_retirement():
    print("\nAdd Retirement Plan")
    view_profiles()
    profile_id = int(input("\nEnter Profile ID: "))
    
    profile = session.get(Profile, profile_id)
    if not profile:
        print("Profile not found")
        return
    
    savings = float(input("Current Savings: $"))
    contribution = float(input("Annual Contribution: $"))
    
    retirement = Retirement(savings=savings, contribution=contribution, profile=profile)
    session.add(retirement)
    session.commit()
    print("Retirement plan added")

def add_life_insurance():
    print("\nAdd Life Insurance")
    view_profiles()
    profile_id = int(input("\nEnter Profile ID: "))
    
    profile = session.get(Profile, profile_id)
    if not profile:
        print("Profile not found")
        return
    
    coverage = float(input("Coverage Amount: $"))
    premium = float(input("Annual Premium: $"))
    policy_type = input("Policy Type (Term/Whole): ")
    
    life = Life(coverage=coverage, premium=premium, policy_type=policy_type, profile=profile)
    session.add(life)
    session.commit()
    print("Life insurance added")

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
EOL