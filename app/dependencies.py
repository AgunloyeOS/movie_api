from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.database import get_db
from app.models import User  
from app.utils import verify_token 

def get_current_user(db: Session = Depends(get_db), token: str = Depends(verify_token)):
    user = db.query(User).filter(User.id == token["sub"]).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
