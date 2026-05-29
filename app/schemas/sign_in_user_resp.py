from pydantic import BaseModel


class SignInUserResponse(BaseModel):
    status: str
    status_code: int
    msg: str
