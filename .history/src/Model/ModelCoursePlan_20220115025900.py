"""
# @Time             : 2022-01-13 23:19:45
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/ModelCoursePlan.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-15 02:49:00
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

class ModelCoursePlan(ModelPublic):
    __tablename__ = 't_cyplan'
    ID_Curricula = Column(BigInteger, index=True)
    ID_Location = Column(BigInteger, index=True)
    ID_Speaker = Column(BigInteger, index=True)
    TimeBegin = Column(Integer,index=True)
    TimeEnd = Column(Integer,index=True)
    Attr = Column(SmallInteger,index=True)
    Charge = Column(SmallInteger,index=True)
    PwAccess = Column(SmallInteger,index=True)
    PwContinuous = Column(SmallInteger,index=True)
    PwDirection = Column(SmallInteger,index=True)
    DoorOpen = Column(SmallInteger,index=True)
    TimeBeginCheckBegin = Column(Integer)
    TimeBeginCheckEnd = Column(Integer)
    TimeEndCheckBegin = Column(Integer)
    TimeEndCheckEnd = Column(Integer)
    RangeUsers = Column(Unicode(1024))
    ListDepts = Column(Unicode(1024))
    RangeEqus = Column(Unicode(1024))
    ListPlaces = Column(Unicode(1024))
    MapUser2Equ = Column(Unicode(1024))
    AboutSpeaker = Column(Unicode(1024))
