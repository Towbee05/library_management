from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.schemas.auth import TokenPayload, UserTokenSchema
from app.repository.auth import UserRepository
from typing import Annotated
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY=settings.SECRET_KEY
ALGORITHM= settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES= settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS= settings.REFRESH_TOKEN_EXPIRE_DAYS

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Class to generate tokens and verify them
class JWT_TOKEN:
    @staticmethod
    def create_access_token(username: str, expiry_time: timedelta | None= None) -> str:
        if not expiry_time:
            expire= datetime.now(timezone.utc) + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
        else:
            expire= datetime.now(timezone.utc) + expiry_time
        payload = {
            "sub": username,
            "exp": expire,
            "type": "access"
        }
        return jwt.encode(payload, SECRET_KEY, algorithm= ALGORITHM)

    @staticmethod
    def create_refresh_token(username: str, expiry_time: timedelta | None= None) -> str:
        if not expiry_time:
            expire= datetime.now(timezone.utc) + timedelta(days= REFRESH_TOKEN_EXPIRE_DAYS)
        else:
            expire= datetime.now(timezone.utc) + expiry_time
        payload = {
            "sub": username,
            "exp": expire,
            "type": "refresh"
        }
        return jwt.encode(payload, SECRET_KEY, algorithm= ALGORITHM)
    
    # Function to erify token and return the token payload (  )
    @staticmethod
    def verify_current_user(token: str) -> TokenPayload:
        try: 
            payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            # validate thr type of token
            if payload.get("type") != "access":
                raise exception
                
            username: str = payload.get("sub")
            if username is None:
                raise exception
            return TokenPayload(username= username)

        except InvalidTokenError:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Could not validate provided credentials",
                headers= {"WWW-Authenticate":"Bearer"}
        )
