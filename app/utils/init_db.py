from app.core.database import Base, engine
# from models.auth import Users

def create_tables():
    Base.metadata.create_all(bind=engine)