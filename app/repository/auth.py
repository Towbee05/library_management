from .base import BaseRepository
from app.schemas.auth import UsersCreationSchema, UserDetailsSchema
from app.models.auth import Users
from pydantic import EmailStr

class UserRepository(BaseRepository):
    def create_user(self, user_data: UsersCreationSchema):
        # Create user instance
        user = Users(**user_data.model_dump(exclude_none=True))
        self.session.add(instance=user)
        self.session.commit()
        self.session.refresh(instance=user)

        return user
    
    def user_email_exist(self, email: EmailStr) -> bool:
        user =  self.session.query(Users).filter_by(email=email).first()
        return bool(user)
    
    def user_username_exist(self, username: str) -> bool:
        user = self.session.query(Users).filter_by(username= username).first()
        return bool(user)
    
    def get_user_by_username(self, username: str) -> UserDetailsSchema | None:
        user= self.session.query(Users).filter_by(username=username).first()
        if user:
            return user
        return None

    def get_user_by_id(self, user_id: int) -> UserDetailsSchema | None:
        user= self.session.query(Users).filter_by(id=user_id).first()
        if user:
            return user
        return None
    
    def is_user_admin(self, admin: bool) -> bool:
        is_admin= self.session.query(Users).filter_by(is_admin=admin).first()
        return is_admin