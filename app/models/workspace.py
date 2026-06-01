from pymysql import Timestamp

from app.db.database import Base
from sqlalchemy import Column,BigInteger, ForeignKey,Integer,String

class Workspace:

    __tablename__ = "workspace_details"
    workspace_id = Column(BigInteger,primary_key=True,index=True)
    workspace_name = Column(String)
    workspace_discription = Column(String)
    created_at = Column(Timestamp)
    modified_at = Column(Timestamp)
    created_by = Column(BigInteger,ForeignKey("user_details.id"))