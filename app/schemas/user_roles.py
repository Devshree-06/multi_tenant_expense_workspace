from enum import Enum


class UserRole(str,Enum):
    WORKSPACE_OWNER = "WORKSPACE_OWNER"
    USER = "USER"
    GUEST = "GUEST"