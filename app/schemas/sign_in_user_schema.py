from pydantic import BaseModel


class UserSignInReq(BaseModel):
    name: str
    email: str
    password: str