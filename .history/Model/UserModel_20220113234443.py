"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/UserModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-13 23:40:52
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
)
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TCyplan(Base):
    __tablename__ = "t_cyplan"
    ID = Column(Integer, primary_key=True)
    ID_Curricula = Column(Integer, nullable=False)
    ID_Location = Column(Integer, nullable=False)
    ID_Speaker = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    TimeBegin = Column(Integer)
    TimeEnd = Column(Integer)
    Attr = Column(Integer)
    Charge = Column(Integer)
    PwAccess = Column(Integer)
    PwContinuous = Column(Integer)
    PwDirection = Column(Integer)
    DoorOpen = Column(Integer)
    TimeBeginCheckBegin = Column(Integer)
    imeBeginCheckEnd = Column(Integer)
    TimeEndCheckBegin = Column(Integer)
    TimeEndCheckEnd = Column(Integer)
    RangeUsers = Column(Unicode(1024))
    ListDepts = Column(Unicode(1024))
    RangeEqus = Column(Unicode(1024))
    ListPlaces = Column(Unicode(1024))
    MapUser2Equ = Column(Unicode(1024))
    AboutSpeaker = Column(Unicode(1024))
    Rem = Column(Unicode(1024))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Unicode(254))
    back_up3 = Column(Integer)
    back_up4 = Column(Integer)
