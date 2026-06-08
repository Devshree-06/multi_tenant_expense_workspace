import email

from fastapi import Depends
from sqlalchemy.orm import Session
from app.auth import verify_token
from app.db.database import getDb
from app.schemas.user_invite_request import UserInviteRequest
import uuid

from app.models.user_invite_model import WorkspaceInvite
from app.schemas.user_roles import UserRole
from  datetime import datetime,timedelta


def workspace_user_invite(invite:UserInviteRequest,workspace_id:int,db:Session=Depends(getDb),user_id: int=Depends(verify_token)):
    if user_id != UserRole.WORKSPACE_OWNER.value:
        return "User does not have proper access rights."
    
    invite_token = str(uuid.uuid4())
    invite_token_expire = datetime.utcnow() + timedelta(days=7)

    

    invite_created = WorkspaceInvite(email=invite.email,role=invite.role,invite_token=invite_token,expired_at=invite_token_expire,
                                     invited_by=user_id,status="PENDING",workspace_id=workspace_id)
    
    db.add(invite_created)
    db.commit()
    db.refresh(invite_created)