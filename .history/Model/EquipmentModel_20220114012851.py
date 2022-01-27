"""
# @Time             : 2022-01-13 23:21:52
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/EquipmentModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 01:23:01
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

Base = declarative_base()
class TCyequipment(Base):
    __tablename__ = 't_cyequipment'

    ID = Column(Integer, primary_key=True)
    ID_Location = Column(Integer, nullable=False)
    ID_User = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Name = Column(Unicode(32))
    ID_Location_SN = Column(Integer)
    ID_IP = Column(Unicode(16))
    MAC = Column(Unicode(24))
    State = Column(Integer)
    Login = Column(Integer)
    Link = Column(Integer)
    Class = Column(Integer)
    Dx = Column(Integer)
    Dy = Column(Integer)
    iTimeBegin = Column(Integer)
    iTimeLogin = Column(Integer)
    WhiteList = Column(Unicode(1024))
    Rem = Column(Unicode(1024))
    TimeUpdate = Column(Integer)
    PortListen = Column(Integer)
    Type = Column(Integer)
    TimeDelay = Column(Integer)
    KeyCancel = Column(Integer)
    KeyDel = Column(Integer)
    KeyF1 = Column(Integer)
    OnAll = Column(Integer)
    RangeEqus = Column(Unicode(64))
    ListPlaces = Column(Unicode(64))
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    ID_Plan = Column(Integer,comment="计划ID")
    KeyOk = Column(Integer)


