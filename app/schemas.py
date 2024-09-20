from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class MovieCreate(BaseModel):
    title: str
    description: str

class Movie(MovieCreate):
    id: int
    owner: User

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    content: str

class Comment(CommentCreate):
    id: int
    movie: Movie

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: str | None = None