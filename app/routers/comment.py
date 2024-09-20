from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, services
from app.dependencies import get_db

router = APIRouter()

@router.post("/movies/{movie_id}/comments", response_model=schemas.Comment)
def add_comment(movie_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return services.create_comment(db=db, comment=comment, movie_id=movie_id)

