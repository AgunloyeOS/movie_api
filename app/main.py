from fastapi import FastAPI
from database import engine
from models import Base
from routers import user, movie, comment

#from app.database import engine
#from app.models import Base
#from app.routers import user, movie, comment

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(movie.router)
app.include_router(comment.router)

from dotenv import load_dotenv
import os

load_dotenv() 

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

