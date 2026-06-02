import email
import stat

from fastapi.types import DependencyCacheKey
from rsa import verify
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import getDb
from app.models.user_details_model import UserSignIn
from app.schemas.sign_in_user_resp import SignInUserResponse
from app.auth import create_token
from app.utils import verify_password

from app.db.database import getDb
from app.schemas.login_user_req import Userlogin


def loginUserTokenGeneration(user: Userlogin,db:Session=Depends(getDb)):

    existing_user = db.query(UserSignIn).filter(UserSignIn.email==user.email).first()

    if not existing_user:
        return SignInUserResponse(
            status="Fail",
            status_code=100,
            msg="User not signed in. Please sign in and try again."
        )
    
    password_check = verify_password(user.password,existing_user.password)

    if not password_check:
        return SignInUserResponse(
            status="Fail",
            status_code=100,
            msg="Incorrect Password. Please try again."
        )

    token = create_token(
        data = {"sub" : str(existing_user.id)}
    )

    return {"msg": "Token created successfully","access_token" : token}