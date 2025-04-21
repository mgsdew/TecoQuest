from app.database.init_db import init_db, reset_db
from app.seeds.seed_data  import seed_data

if __name__ == "__main__":
    # print("Initializing the database...")
    # init_db()
    # print("Database initialized successfully!")

    ## Uncomment the below lines to reset the database and insert mock data
    print("Resetting the database...")
    reset_db()
    print("Database reset successfully!")

    print("Seeding mock data...")
    seed_data()
    print("Mock data seeded successfully!")