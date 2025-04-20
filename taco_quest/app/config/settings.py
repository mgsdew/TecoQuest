import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./taco_quest.db")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()