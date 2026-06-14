from app.models.user_details_model import UserSignIn
from app.schemas.sign_in_user_schema import UserSignInReq
from sqlalchemy.orm import Session
from app.schemas.sign_in_user_resp import SignInUserResponse
from app.utils import hash_password


def sign_in_users(user: UserSignInReq,db: Session):

    existing_user = db.query(UserSignIn).filter(UserSignIn.email==user.email).first()

    if existing_user:
        return  SignInUserResponse(
        status = "Fail",
        status_code=100,
        msg = "User already exist. Please login"
    )
    
    sign_in_user = UserSignIn(name=user.name,email=user.email,password=hash_password(user.password))
    
    db.add(sign_in_user)
    db.commit()
    db.refresh(sign_in_user)

    print("User is added to db for sign in")

    return SignInUserResponse(
        status = "Success",
        status_code= 200,
        msg = "User Signed in successfully"
    )

