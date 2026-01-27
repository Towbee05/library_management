from fastapi import APIRouter, Depends, status
from app.schemas.auth import UsersCreationSchema, UserDetailsSchema, UserLoginSchema
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth import UserService
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

authRouter = APIRouter()

@authRouter.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserDetailsSchema)
def signupRouter(signupDetails: UsersCreationSchema, session: Session= Depends(get_db)):
    try:
        return UserService(session=session).signup(user_data= signupDetails)
    except Exception as error:
        print(error)
        raise error

@authRouter.post("/token", status_code=status.HTTP_200_OK)
def loginRouter(form_data: OAuth2PasswordRequestForm= Depends(), session: Session= Depends(get_db)):
    try:
        return UserService(session=session).login(username= form_data.username, password= form_data.password)
    except Exception as error:
        print(error)
        raise error