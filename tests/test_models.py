import pytest
from finance_tracker.models import Profile, Retirement, Life
from finance_tracker.models.base import Base, session, engine

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(engine)
    yield
    session.rollback()
    Base.metadata.drop_all(engine)

def test_profile_creation():
    profile = Profile(name="Test User", age=30, income=60000)
    session.add(profile)
    session.commit()
    assert profile.id is not None

def test_retirement_relationship():
    profile = Profile(name="Test User", age=30, income=60000)
    retirement = Retirement(savings=50000, contribution=6000)
    profile.retirement = retirement
    session.add(profile)
    session.commit()
    assert retirement.profile_id == profile.id

def test_life_relationship():
    profile = Profile(name="Test User", age=30, income=60000)
    life = Life(coverage=300000, premium=250, policy_type="Term")
    profile.life = life
    session.add(profile)
    session.commit()
    assert life.profile_id == profile.id

def test_profile_deletion_cascades():
    profile = Profile(name="Test User", age=30, income=60000)
    retirement = Retirement(savings=50000, contribution=6000)
    life = Life(coverage=300000, premium=250, policy_type="Term")
    profile.retirement = retirement
    profile.life = life
    session.add(profile)
    session.commit()
    
    session.delete(profile)
    session.commit()
    
    assert session.query(Profile).count() == 0
    assert session.query(Retirement).count() == 0
    assert session.query(Life).count() == 0
