import email

from pydantic import BaseModel

class UserInviteRequest(BaseModel):
    email:str
    user_role:str