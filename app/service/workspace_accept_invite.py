import stat

from fastapi import Depends
from numpy import invert

from app.auth import verify_token
from app.db.database import getDb
from app.models import workspace_member
from app.models.user_invite_model import WorkspaceInvite
from sqlalchemy.orm import Session
from app.models.user_details_model import UserSignIn
from app.schemas.user_roles import UserRole
from app.models.workspace_member import WorkspaceMember

def accept_invite(invite:str,db:Session=Depends(getDb),user_id:int=Depends(verify_token)):

    user_role_check = db.query(UserSignIn).filter(UserSignIn.id==user_id).first()

    if not user_role_check:
        return "User does not exist"
    
    print("User role is : ",user_role_check.role)

    if  user_role_check.role != UserRole.USER.value:
        return "User does not have proper access rights"
    
    invite_check = db.query(WorkspaceInvite).filter(WorkspaceInvite.invite_token==invite).first()

    if not invite_check:
        return "Invalid invite.Please try again"
    
    if invite_check.status=="ACCEPTED":
        return "Invite is already accepted."
    
    if user_role_check.email.lower()!=invite_check.email.lower():
        "Invalid user email.Please try again."

    invite_check.status = "ACCEPTED";
    db.commit()

    member = WorkspaceMember(workspace_id=invite_check.workspace_id,user_id= user_id,
                              role=invite_check.role)
    
    db.add(member)
    db.commit()
    db.refresh(member)

    return "Invitation accepted successfully!"

