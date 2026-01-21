from fastapi import APIRouter, Depends
from app.schemas.auth import UsersCreationSchema, UserDetailsSchema
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth import UserService

authRouter = APIRouter()

@authRouter.post("/signup", status_code=201, response_model=UserDetailsSchema)
def signupRouter(signupDetails: UsersCreationSchema, session: Session= Depends(get_db)):
    try:
        return UserService(session=session).signup(user_data= signupDetails)
    except Exception as e:
        print(e)
        raise e

@authRouter.get("/login", status_code=200)
def loginRouter():
    return {"message": "Signup here"}