from app.database.models import User, Taco, Location, Review, Achievement, UserAchievement, Follow
from app.database.db import engine, Session
from datetime import datetime
import random

def seed_data():
    try:
        with Session(engine) as session:
        # Check if users already exist
            if session.query(User).first():
                print("Data already exists. Skipping seeding.")
                return
            # Create mock users
            users = [
                User(username="taco_lover", email="taco_lover@example.com"),
                User(username="spicy_fan", email="spicy_fan@example.com"),
                User(username="crunchy_taco", email="crunchy_taco@example.com"),
            ]
            session.add_all(users)
            session.commit()
            print("Users seeded successfully!")

            # Create mock locations
            locations = [
                Location(name="Taco Fiesta", address="123 Taco St", lat=40.7128, lon=-74.0060),
                Location(name="Spicy Tacos", address="456 Heat Ave", lat=34.0522, lon=-118.2437),
            ]
            session.add_all(locations)
            session.commit()
            print("Locations seeded successfully!")

            # Create mock tacos
            tacos = [
                Taco(name="Classic Taco", description="A classic beef taco", location_id=locations[0].id),
                Taco(name="Spicy Taco", description="A taco with a spicy kick", location_id=locations[1].id),
            ]
            session.add_all(tacos)
            session.commit()
            print("Tacos seeded successfully!")

            # Create mock reviews
            reviews = [
                Review(user_id=users[0].id, taco_id=tacos[0].id, rating=5, comment="Amazing taco!"),
                Review(user_id=users[1].id, taco_id=tacos[1].id, rating=4, comment="Loved the spice!"),
            ]
            session.add_all(reviews)
            session.commit()
            print("Reviews seeded successfully!")

            # Create mock achievements
            achievements = [
                Achievement(name="First Taco", description="Reviewed your first taco"),
                Achievement(name="Spicy Lover", description="Reviewed a spicy taco"),
            ]
            session.add_all(achievements)
            session.commit()
            print("Achievements seeded successfully!")

            # Assign achievements to users
            user_achievements = [
                UserAchievement(user_id=users[0].id, achievement_id=achievements[0].id, earned_at=datetime.utcnow()),
                UserAchievement(user_id=users[1].id, achievement_id=achievements[1].id, earned_at=datetime.utcnow()),
            ]
            session.add_all(user_achievements)
            session.commit()
            print("User achievements seeded successfully!")

            # Create follow relationships
            follows = [
                Follow(follower_id=users[0].id, following_id=users[1].id),
                Follow(follower_id=users[1].id, following_id=users[2].id),
            ]
            session.add_all(follows)
            session.commit()
            print("Follow relationships seeded successfully!")

            print("Mock data seeded successfully!")

    except Exception as e:
        print(f"Error during seeding: {e}")