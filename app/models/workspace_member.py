from app.db.database import Base
from sqlalchemy import Column,BigInteger, ForeignKey, DateTime,String
from datetime import datetime

class WorkspaceMember(Base):
    __tablename__="workspace_member"
    member_id=Column(BigInteger,primary_key=True,index=True)
    workspace_id = Column(BigInteger,ForeignKey("workspace_details.workspace_id"))
    user_id=Column(BigInteger,ForeignKey("user_details.id"))
    role=Column(String(50))
    joined_at=(DateTime,datetime.utcnow)