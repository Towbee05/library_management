from sqlalchemy.orm import Session
from app.repository.auth import UserRepository
from app.schemas.auth import UsersCreationSchema, UserDetailsSchema
from app.utils.hash_password import HashHelper
from fastapi import HTTPException
from http import HTTPStatus

class UserService:
    def __init__(self, session: Session):
        self._user_repository = UserRepository(session=session)

    def signup(self, user_data: UsersCreationSchema) -> UserDetailsSchema:
        # print("++++++++++ USER IS TRYING TO SIGNUP ++++++++++")
        if self._user_repository.user_email_exist(email= user_data.email):
            raise HTTPException(status_code= HTTPStatus.BAD_REQUEST, detail="User with provided email exists in databse") 
        
        if self._user_repository.user_username_exist(username= user_data.username):
            raise HTTPException(status_code= HTTPStatus.BAD_REQUEST, detail="User with provided username exists in database")

        hashed_password = HashHelper.hash_password(user_data.password)
        user_data.password = hashed_password
        return self._user_repository.create_user(user_data= user_data)
