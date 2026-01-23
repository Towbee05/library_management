from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
import os

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine= create_engine(TEST_DATABASE_URL)
TestingSessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)