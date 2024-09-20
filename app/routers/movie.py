from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, services
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/movies", response_model=schemas.Movie)
def add_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return services.create_movie(db=db, movie=movie, user_id=user_id)
