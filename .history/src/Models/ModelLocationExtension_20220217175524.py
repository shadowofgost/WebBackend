"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-27 14:15:12
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelLocationExtension.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 17:51:30
# @Software         : Vscode
"""
from sqlalchemy import BigInteger, Column, Integer, SmallInteger
from .PublicModel import ModelPublic


class ModelLocationExtension(ModelPublic):
    __tablename__ = "t_cylocationex"

    ID_Location = Column(
        BigInteger,
        index=True,
        comment="外键，位置的唯一标识",
        doc="这是外键，链接Location关键字，每个位置的唯一标识，一旦添加不能更改",
    )
    Attr = Column(SmallInteger, index=True)
    DateBegin = Column(Integer, index=True)
    DateEnd = Column(Integer, index=True)
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
