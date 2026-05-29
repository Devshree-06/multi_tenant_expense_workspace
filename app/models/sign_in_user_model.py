from app.db.database import Base

from sqlalchemy import Column,Integer,String,BigInteger


class UserSignIn(Base):
    __tablename__ = "user_details"

    id = Column(BigInteger,primary_key=True,index=True)
    name = Column(String(200))
    email = Column(String(200),index=True)
    password = Column(String(200))

