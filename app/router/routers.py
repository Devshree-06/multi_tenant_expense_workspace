from webbrowser import get

from aiosmtplib import send
from fastapi import Depends,APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.schemas.sign_in_user_schema import UserSignInReq
from app.db.database import getDb
from app.service import workspace_accept_invite
from app.service.email_service import send_invite_by_email
from app.service.sign_in_user_service import sign_in_users
from app.schemas.login_user_req import Userlogin
from app.service.user_login_service import loginUserTokenGeneration
from app.schemas.user_role_request import UserRoleReq
from app.auth import verify_token
from app.service.workspace_user_access_service import assign_workspace_user_role
from app.schemas.workspaceCreate import WorkspaceCreateReq
from app.service.workspace_create_service import create_workspace
from app.schemas.user_invite_request import UserInviteRequest
from app.service.user_invite_service import workspace_user_invite
from app.service.workspace_accept_invite import accept_invite



router = APIRouter(
    prefix="/workspace"
)

@router.post("/signIn")
def signUpUsers(user: UserSignInReq,db: Session=Depends(getDb)):
    return sign_in_users(user,db)


@router.post("/login")
def login(login: Userlogin,db: Session=Depends(getDb)):
    return loginUserTokenGeneration(login,db)


@router.post("/workspace_user_role_access")
def user_role_assign(role: UserRoleReq,db:Session=Depends(getDb),token:int=Depends(verify_token)):
    return assign_workspace_user_role(role,db,token)


@router.post("/create_workspace")
def workspace_creation(req: WorkspaceCreateReq,db:Session=Depends(getDb),user_id:int=Depends(verify_token)):
    return create_workspace(req,db,user_id)


@router.post("/{workspace_id}/invite")
async def sent_invite(req: UserInviteRequest, workspace_id: int,db: Session=Depends(getDb),user:int=Depends(verify_token)):

    return await workspace_user_invite(req,workspace_id,db,user)


@router.post("/accept_invite/{invite_token}")
def member_invite(invite_token:str,db:Session=Depends(getDb),user:int=Depends(verify_token)):
    return accept_invite(invite_token,db,user)

# class TestEmail(BaseModel):
#     email: str

# @router.post("/test/email")
# async def test_email(req:TestEmail):
#     await send_invite_by_email(email=req.email,invite_link="https://google.com")

#     return {
#         "status" : "success",
#         "Message" : "Mail sent successfully"
#     }
