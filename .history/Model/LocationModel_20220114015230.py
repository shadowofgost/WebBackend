"""
# @Time             : 2022-01-13 23:22:21
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/LocationModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 01:42:30
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

class TCylocation(Base):
    __tablename__ = 't_cylocation'

    ID = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    ID_Parent = Column(Integer)
    Name = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    Rem = Column(Unicode(1024))


class TCylocationex(Base):
    __tablename__ = 't_cylocationex'

    ID_Location = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    Attr = Column(Integer)
    DateBegin = Column(Integer)
    DateEnd = Column(Integer)
    ModeRun = Column(Integer)
    ModeShangJi = Column(Integer)
    EnableDelayCharged = Column(Integer)
    DelayCharged = Column(Integer)
    EnableLimitYuE_SJ = Column(Integer)
    LimitYuE_SJ = Column(Integer)
    EnableLimitYuE_XJ = Column(Integer)
    LimitYuE_XJ = Column(Integer)
    EnableLimitTime_XJ = Column(Integer)
    LimitTime_XJ = Column(Integer)
    EnableWarnYuE = Column(Integer)
    WarnYuE = Column(Integer)
    EnableWarnTime = Column(Integer)
    WarnTime = Column(Integer)
    EnableMinCost = Column(Integer)
    MinCost = Column(Integer)
    Price = Column(Integer)
    PriceMinute = Column(Integer)
    GetEquName = Column(Integer)
    GetEquIp = Column(Integer)
    GetEquMac = Column(Integer)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
