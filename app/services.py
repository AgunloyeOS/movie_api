from sqlalchemy.orm import Session
from app import models, schemas
from app.utils import hash_password, create_access_token

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_movie(db: Session, movie: schemas.MovieCreate, user_id: int):
    db_movie = models.Movie(**movie.dict(), owner_id=user_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def create_comment(db: Session, comment: schemas.CommentCreate, movie_id: int):
    db_comment = models.Comment(**comment.dict(), movie_id=movie_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
