from sqlalchemy import Column, String
from .database import Base

class User(Base):
    __tablename__ = 'self_user'
    id = Column(String(255), primary_key=True, nullable=False, comment='用户名')
    password = Column(String(255), nullable=False, comment='密码')
