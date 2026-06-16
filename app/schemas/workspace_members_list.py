from typing import List

from pydantic import BaseModel

class MembersData(BaseModel):
    user_id: int
    name: str
    role: str


class WorkspaceMemberResponse(BaseModel):
    workspace_id : int
    workspace_name: str
    members: List[MembersData]