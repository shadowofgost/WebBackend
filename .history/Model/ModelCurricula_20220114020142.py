"""
# @Time             : 2022-01-13 23:21:08
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/CurriculaModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 02:00:17
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

Base = declarative_base()
class ModelCurricula(ModelPublic):
    __tablename__ = 't_cycurricula'

    ID_Location = Column(Integer, nullable=False)
    ID_Speaker = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Name = Column(Unicode(32))
    TimeBegin = Column(Integer)
    TimeEnd = Column(Integer)
    Attr = Column(Integer)
    Charge = Column(Integer)
    PwAccess = Column(Integer)
    PwContinuous = Column(Integer)
    PwDirection = Column(Integer)
    DoorOpen = Column(Integer)
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
