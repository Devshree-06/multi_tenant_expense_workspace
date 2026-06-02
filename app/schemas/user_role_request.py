from os import access

from pydantic import BaseModel


class UserRoleReq(BaseModel):
    access_type:str
    