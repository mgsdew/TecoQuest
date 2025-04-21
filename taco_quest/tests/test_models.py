import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlmodel import Session
from app.database.models import User, Taco, Location, Review, Achievement, UserAchievement, Follow
from app.database.db import engine
import pytest
from app.database.init_db import reset_db


@pytest.fixture(autouse=True)
def reset_database():
    reset_db()

def test_user_creation():
    with Session(engine) as session:
        user = User(username="test_user", email="test_user@example.com")
        session.add(user)
        session.commit()
        session.refresh(user)
        assert user.id is not None
        assert user.username == "test_user"

def test_relationships():
    with Session(engine) as session:
        # Create a user and a taco
        user = User(username="relationship_user", email="relationship_user@example.com")
        location = Location(name="Test Location", address="123 Test St", lat=0.0, lon=0.0)
        taco = Taco(name="Test Taco", description="A test taco", location=location)
        review = Review(user=user, taco=taco, rating=5, comment="Great taco!")

        session.add_all([user, location, taco, review])
        session.commit()

        # Validate relationships
        assert len(user.reviews) == 1
        assert user.reviews[0].taco.name == "Test Taco"
        assert taco.reviews[0].user.username == "relationship_user"