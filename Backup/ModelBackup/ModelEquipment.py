"""
# @Time             : 2022-01-13 23:21:52
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/ModelEquipment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 13:08:28
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


class ModelEquipment(ModelPublic):
    __tablename__ = 't_cyequipment'

    ID_Location = Column(BigInteger,index=True)
    ID_User = Column(BigInteger, index=True)
    Name = Column(Unicode(32),index=True)
    ID_Location_SN = Column(BigInteger,index=True)
    ID_IP = Column(Unicode(16),index=True)
    MAC = Column(Unicode(24))
    State = Column(SmallInteger,index=True)
    Login = Column(SmallInteger,index=True)
    Link = Column(SmallInteger,index=True)
    Class_field = Column(SmallInteger,index=True,name="Class")
    Dx = Column(Integer)
    Dy = Column(Integer)
    iTimeBegin = Column(Integer)
    iTimeLogin = Column(Integer)
    WhiteList = Column(Unicode(1024))
    PortListen = Column(Integer)
    Type = Column(Integer)
    TimeDelay = Column(Integer)
    KeyCancel = Column(Integer)
    KeyDel = Column(Integer)
    KeyF1 = Column(Integer)
    OnAll = Column(Integer)
    RangeEqus = Column(Unicode(64))
    ListPlaces = Column(Unicode(64))
    ID_Plan = Column(BigInteger,comment="计划ID",index=True)
    KeyOk = Column(Integer)
