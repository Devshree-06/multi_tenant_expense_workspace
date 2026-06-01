from pydantic import BaseModel

class WorkspaceCreateReq(BaseModel):
    workspace_name: str
    workspace_description: str
    