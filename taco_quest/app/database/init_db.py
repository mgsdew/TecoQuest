from sqlmodel import SQLModel
from app.database.db import engine

def init_db():
    # Create all tables in the database
    SQLModel.metadata.create_all(engine)

def reset_db():
    # Drop all tables and recreate them
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)