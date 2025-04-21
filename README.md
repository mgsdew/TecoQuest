# Taco Quest

Taco Quest is a community-driven taco discovery platform where users can explore tacos by location, share reviews and ratings, follow other taco lovers, and earn achievements through their activity.

The backend is implemented with SQLModel and Python, the frontend with Next.js and Prisma, and both are connected to Supabase as a cloud database.

---

## Project Setup

### Phase 1: Set Up Project and Dependencies
1. **Create Project Directory and Virtual Environment**
   ```bash
   mkdir -p taco_quest/app/{database,config,seeds,utils}
   mkdir -p taco_quest/tests

   py -m venv .venv  # Create a Virtual Environment
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  # Grant PowerShell Permission
   .venv\Scripts\activate  # Activate Virtual Environment

   pip install uv  # Install uv for managing dependencies
   uv init  # Create initial files inside the main folder
   ```

2. **Install Dependencies**
   ```bash
   uv add sqlmodel pydantic python-dotenv typer
   ```

3. **Set Up `.gitignore`**
   A `.gitignore` file was created to exclude unnecessary files like `__pycache__`, `.venv/`, and others.

---

### Phase 2: Configuration and Database Setup
1. **Configuration Module**
   - A `settings.py` file was created to manage environment variables using `python-dotenv`.

2. **Database Connection**
   - A `db.py` file was created to manage the database connection using SQLModel.

3. **Database Initialization**
   - An `init_db.py` script was created to initialize the database and create tables.

4. **Environment Variables**
   - A `.env` file was added to store configuration values like `DATABASE_URL` and `DEBUG`.

---

### Phase 3: Database Modeling
The database schema is implemented using SQLModel. Below are the key entities and their relationships:

#### Key Entities
- **User**: Represents a registered taco lover.
- **Taco**: A taco instance tied to a specific location.
- **Location**: A physical place where tacos are served.
- **Review**: A user's feedback on a taco.
- **Follow**: Tracks user follow relationships.
- **Achievement**: Represents badges earned by users.
- **UserAchievement**: Tracks which achievements a user has earned.

#### Relationships
- Users can write reviews for tacos.
- Tacos are associated with specific locations.
- Users can follow other users.
- Users can earn achievements based on activity.

#### Database Initialization
Run the following command to create the database tables:

```bash
python main.py
```

---

### Phase 4: Mock Data Generation
Mock data was created to populate the database with sample users, tacos, locations, reviews, achievements, and follow relationships.

#### Seeding the Database
Run the following command to seed the database with mock data:

```bash
python main.py
```

This will:
- Add sample users, locations, and tacos.
- Create reviews and assign achievements.
- Establish follow relationships between users.

---

## Next Steps
- **Phase 5**: Testing and Validation
- **Phase 6**: Documentation
- **Phase 7**: Supabase Integration