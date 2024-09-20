from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import user, movie, comment

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(movie.router)
app.include_router(comment.router)


