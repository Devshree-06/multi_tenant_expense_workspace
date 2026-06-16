from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from sqlalchemy import select

from app.auth import verify_token
from app.db.database import getDb
from app.models.workspace_member import WorkspaceMember
from app.schemas.workspace_members_list import MembersData,WorkspaceMemberResponse
from app.models.user_details_model import UserSignIn
from app.models.workspace import Workspace
from app.schemas.workspace_members_list import MembersData,WorkspaceMemberResponse



def get_workspace_members(workspace_id: int,db:Session=Depends(getDb)):

    workspace_exist = db.execute(
        select(Workspace).where(
            Workspace.workspace_id  == workspace_id
        )
    ).scalar_one_or_none()

    if not workspace_exist:
        raise HTTPException(
            status_code=404,
            detail="Workspace does not exist"
        )
    
    result = db.execute(
        select(
            UserSignIn.id,
            UserSignIn.name,
            WorkspaceMember.role
        )
        .join(UserSignIn,WorkspaceMember.user_id == UserSignIn.id
        ).where(WorkspaceMember.workspace_id == workspace_id)
    ).all()

    membersData = [
        MembersData(
            user_id=row.id,
            name=row.name,
            role=row.role
        )

        for row in result
    ]

    return WorkspaceMemberResponse(
        workspace_id=workspace_id,
        workspace_name = workspace_exist.workspace_name,
        members = membersData

    )

     

