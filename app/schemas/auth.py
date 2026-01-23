from typing_extensions import Self
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Any, Optional, Union

# User trying to login (seralizer)
class UsersCreationSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_admin: Optional[bool] = False
    createdAt: datetime = datetime.now()
    lastLogin: Optional[datetime] = None

# User details serializer
class UserDetailsSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_admin: Union[bool, None]
    createdAt: datetime
    lastLogin: Optional[datetime] = None

    class Config:
        orm_mode = True

# Update user serializer
class UserUpdateSchema(BaseModel):
    id: int
    username: Union[str, None] = None
    email: Union[str, None] = None
    password: Union[str, None] = None
    is_admin: Union[bool, None] = None

# Login user serializer
class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    lastLogin: datetime = datetime.now()

# Serializer to return after user logs in
class UserTokenSchema(BaseModel):
    refresh_token: str
    access_token: str
    