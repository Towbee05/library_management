from sqlalchemy.orm import Session
from app.repository.auth import UserRepository
from app.schemas.auth import UsersCreationSchema, UserDetailsSchema, TokenPayload, UserTokenSchema
from app.utils.hash_password import HashHelper
from fastapi import HTTPException, status
from app.utils.jwt_auth import JWT_TOKEN
from typing import Annotated
from .base import BaseService

 
class UserService(BaseService):
    def authenticate_user(self, username: str, password: str) -> UserDetailsSchema:
        user = self._user_repository.get_user_by_username(username=username)
        if user is None:
            return None
        
        # verify password
        is_password_correct = HashHelper.verify_password(plain_password= password, hashed_password=user.password)
        if not is_password_correct:
            return None
        return user

    def signup(self, user_data: UsersCreationSchema) -> UserDetailsSchema:
        # print("++++++++++ USER IS TRYING TO SIGNUP ++++++++++")
        if self._user_repository.user_email_exist(email= user_data.email):
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="User with provided email exists in databse") 
        
        if self._user_repository.user_username_exist(username= user_data.username):
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="User with provided username exists in database")

        hashed_password = HashHelper.hash_password(user_data.password)
        user_data.password = hashed_password
        return self._user_repository.create_user(user_data= user_data)

    # Authenticate users
    def login(self, username: str, password: str) -> UserTokenSchema:
        #  Authenticate user
        user = self.authenticate_user(username= username, password= password)
        if not user:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
       
        # Generate JWT tokens
        # token= create_access_token(data= {"username": user.username})
        data= TokenPayload(username= user.username)
        access_token= JWT_TOKEN(data = data).create_access_token()
        refresh_token= JWT_TOKEN(data = data).create_refresh_token()

        token = UserTokenSchema(token_type="Bearer", access_token= access_token, refresh_token= refresh_token)
        print(token)
        return token