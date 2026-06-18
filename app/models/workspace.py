from sqlalchemy import DateTime
from datetime import datetime

from app.db.database import Base
from sqlalchemy import Column,BigInteger, ForeignKey,Integer,String

class Workspace(Base):

    __tablename__ = "workspace_details"
    workspace_id = Column(BigInteger,primary_key=True,index=True)
    workspace_name = Column(String(200))
    workspace_description = Column(String(200))
    created_at = Column(DateTime,default=datetime.utcnow)
    modified_at = Column(DateTime,default=datetime.utcnow)
    created_by = Column(BigInteger,ForeignKey("user_details.id"))