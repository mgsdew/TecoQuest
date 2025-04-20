from sqlmodel import create_engine, Session
from app.config.settings import settings

# Create the database engine
engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

# Dependency to get a database session
def get_session():
    with Session(engine) as session:
        yield session