from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os
import sys

load_dotenv()

class Settings(BaseSettings):
    database_url: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # JWT config
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
settings = Settings()