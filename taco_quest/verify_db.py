from sqlmodel import Session, select
from app.database.models import User, Taco, Review, Location, Achievement
from app.database.db import engine

def verify_data():
    with Session(engine) as session:
        print("Users:")
        users = session.exec(select(User)).all()
        for user in users:
            print(user)

        print("\nLocations:")
        locations = session.exec(select(Location)).all()
        for location in locations:
            print(location)

        print("\nTacos:")
        tacos = session.exec(select(Taco)).all()
        for taco in tacos:
            print(taco)

        print("\nReviews:")
        reviews = session.exec(select(Review)).all()
        for review in reviews:
            print(review)

        print("\nAchievements:")
        achievements = session.exec(select(Achievement)).all()
        for achievement in achievements:
            print(achievement)

if __name__ == "__main__":
    verify_data()