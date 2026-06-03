
from ssl import VerifyMode
from webbrowser import get

from sqlalchemy.orm import Session

from app.schemas.workspaceCreate import WorkspaceCreateReq
from app.auth import verify_token
from fastapi import Depends
from app.db.database import getDb
from app.models.user_details_model import UserSignIn
from app.schemas.user_roles import UserRole
from app.models.workspace import Workspace


def create_workspace(create_req: WorkspaceCreateReq,db:Session=Depends(getDb),user_id: int=Depends(verify_token)):
    user_role_check = db.query(UserSignIn).filter(UserSignIn.id == user_id).first()

    if not user_role_check.role==UserRole.WORKSPACE_OWNER.value:
        return "User does not havr proper permissions"
    
    workspace_create = Workspace(workspace_name=create_req.workspace_name,
                                 workspace_description=create_req.workspace_description,
                                 created_by=user_id)
    
    db.add(workspace_create)
    db.commit()
    db.refresh(workspace_create)

    return "Workspace Created Successfully"