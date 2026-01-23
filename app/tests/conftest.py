import pytest 
from app.tests.database import TestingSessionLocal, engine
from app.main import app
from app.core.database import Base, get_db

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def overide_get_db():
    db= TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = overide_get_db