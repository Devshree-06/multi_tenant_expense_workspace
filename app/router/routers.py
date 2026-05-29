from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from app.schemas.sign_in_user_schema import UserSignInReq
from app.db.database import getDb
from app.service.sign_in_user_service import sign_in_users



router = APIRouter()

@router.post("/signIn")
def signUpUsers(user: UserSignInReq,db: Session=Depends(getDb)):
    return sign_in_users(user,db)
