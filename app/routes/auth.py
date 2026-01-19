from fastapi import APIRouter, Depends

authRouter = APIRouter()

@authRouter.get("/signup", status_code=201)
def signupRouter():
    return {"message": "Signup here"}

@authRouter.get("/login", status_code=200)
def loginRouter():
    return {"message": "Signup here"}