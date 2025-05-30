from finance_tracker.models import Profile, Retirement, Life
from finance_tracker.models.base import session

def seed_database():
    
    session.query(Life).delete()
    session.query(Retirement).delete()
    session.query(Profile).delete()
    
    
    alice = Profile(name="Alice Smith", age=35, income=85000)
    bob = Profile(name="Bob Johnson", age=42, income=110000)
    charlie = Profile(name="Charlie Brown", age=28, income=75000)
    
    
    Retirement(savings=125000, contribution=10000, profile=alice)
    Retirement(savings=285000, contribution=15000, profile=bob)
    
    
    Life(coverage=500000, premium=350, policy_type="Term", profile=alice)
    Life(coverage=1000000, premium=800, policy_type="Whole", profile=bob)
    Life(coverage=250000, premium=200, policy_type="Term", profile=charlie)
    
    
    session.add_all([alice, bob, charlie])
    session.commit()
