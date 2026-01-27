from sqlalchemy.orm import Session
from app.repository.auth import UserRepository

class BaseService:
    def __init__(self, session: Session):
        self._user_repository = UserRepository(session= session)