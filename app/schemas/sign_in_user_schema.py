from pydantic import BaseModel


class UserSignInReq(BaseModel):
    name: str
    email: str
    password: str


class Userloginreq(BaseModel):
    email: str
    password: str