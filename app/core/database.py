from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from .config import settings
import sys

load_dotenv()
# MySQL db engine
DATABASE_URL = settings.database_url
if not DATABASE_URL:
    print("❌ Failed to connect to database")
    sys.exit(1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
print("✅🌐 Successful database connection")

def create_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()