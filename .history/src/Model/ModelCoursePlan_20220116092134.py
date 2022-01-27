"""
# @Time             : 2022-01-13 23:19:45
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/ModelCoursePlan.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-16 00:18:54
# @LastAuthor       : Albert Wang
"""
from pydoc import doc
from turtle import title
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
    __tablename__ = "t_cyplan"
    ID_Curricula = Column(BigInteger, index=True, title="课程ID", doc="这是课程的id序列号")
    ID_Location = Column(BigInteger, index=True, title="地点ID", doc="这是地点的id序列号")
    ID_Speaker = Column(BigInteger, index=True, title="主讲人ID", doc="这是主讲人的id序列号")
    TimeBegin = Column(Integer, index=True,title="开始时间", doc="这是开始时间,单位是秒，每一天0时0分0秒开始的秒数")
    TimeEnd = Column(Integer, index=True,title="结束时间", doc="这是结束时间,单位是秒")
    Attr = Column(SmallInteger, index=True)
    Charge = Column(SmallInteger, index=True)
    PwAccess = Column(SmallInteger, index=True)
    PwContinuous = Column(SmallInteger, index=True)
    PwDirection = Column(SmallInteger, index=True)
    DoorOpen = Column(SmallInteger, index=True)
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
