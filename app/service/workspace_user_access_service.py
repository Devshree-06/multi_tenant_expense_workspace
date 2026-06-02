import logging

from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.user_role_request import UserRoleReq
from app.db.database import getDb
from app.models.user_details_model import UserSignIn
from app.auth import verify_token
from app.schemas.user_roles import UserRole



def assign_workspace_user_role(user: UserRoleReq,db:Session=Depends(getDb),user_id:int=Depends(verify_token)):

    check_user_exists = db.query(UserSignIn).filter(UserSignIn.id == user_id).first()

    if not check_user_exists:
        return "User does not exists"
    
    if(user.access_type.upper() == UserRole.WORKSPACE_OWNER.value):
        logging.info("User has Owner access")

        check_user_exists.role = user.access_type

        db.commit()

        return "User has Owner Access. Please proceed with workspace creation"
    
    else:
        return "Only Owners can create workspace. Please try again"

