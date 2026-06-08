
from click import DateTime

from app.db.database import Base
from sqlalchemy import Column,BigInteger,String,DateTime, null
from datetime import datetime


class WorkspaceInvite(Base):
    __tablename__ = "workspace_invite"
    invite_id = Column(BigInteger,primary_key=True,index=True)
    workspace_id = Column(BigInteger)
    invite_token = Column(String(100))
    email = Column(String(200))
    invited_by = Column(String(200))
    status = Column(String(200))
    role = Column(String(10))
    expired_at = Column(DateTime,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)
