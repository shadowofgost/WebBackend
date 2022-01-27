"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/Public.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 13:01:48
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import (
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    BigInteger,
)
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.ext.declarative import declarative_base
from .Public import ModelPublic

Base= declarative_base()
class ModelPublic(Base):
    __abstract__ = True
    ID = Column(BigInteger, Identity(start=1, increment=1), primary_key=True, unique=True,autoincrement=True, nullable=False,index=True)
    Rem = Column(Unicode(64))
    Introduction = Column(Unicode(254))
    TimeUpdate = Column(BigInteger,index=True)
    IdManager = Column(BigInteger,index=True)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Unicode(254))
    back_up3 = Column(Unicode(254))
    back_up4 = Column(Integer)
    back_up5 = Column(Integer)
    back_up6 = Column(Integer)
