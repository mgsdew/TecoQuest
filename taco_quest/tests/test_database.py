import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlmodel import Session
from app.database.models import User, Taco, Location
from app.database.db import engine

def test_create_and_read():
    with Session(engine) as session:
        # Create a user
        user = User(username="crud_user", email="crud_user@example.com")
        session.add(user)
        session.commit()

        # Read the user
        retrieved_user = session.get(User, user.id)
        assert retrieved_user is not None
        assert retrieved_user.username == "crud_user"

def test_update_and_delete():
    with Session(engine) as session:
        # Create a location
        location = Location(name="Test Location", address="123 Test St", lat=0.0, lon=0.0)
        session.add(location)
        session.commit()

        # Create a taco with a valid location_id
        taco = Taco(name="Update Taco", description="To be updated", location_id=location.id)
        session.add(taco)
        session.commit()

        # Update the taco
        taco.description = "Updated description"
        session.add(taco)
        session.commit()

        updated_taco = session.get(Taco, taco.id)
        assert updated_taco.description == "Updated description"

        # Delete the taco
        session.delete(updated_taco)
        session.commit()

        deleted_taco = session.get(Taco, taco.id)
        assert deleted_taco is None