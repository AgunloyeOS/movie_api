import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres123@localhost/movie_db")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "2236fc2aeee4ea0d68bd32e9193b1e492ebacba1fd4072f6edc243479e3ed22c")

    class Config:
        env_file = ".env"

# Initialize settings object
settings = Settings()
