from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30) ,index=True, unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    is_admin: Mapped[bool] = mapped_column(default=False)
    createdAt: Mapped[datetime] = mapped_column()
    lastLogin: Mapped[datetime] = mapped_column()

    def __repr__(self):
        return f"{self.id} {self.username}"