"""
# @Time             : 2022-01-13 23:22:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/MmxModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 01:42:42
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

class TCymmx(Base):
    __tablename__ = 't_cymmx'

    ID = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    ID_Data = Column(Integer)
    ID_Type = Column(Integer)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)


class TCymmxdata(Base):
    __tablename__ = 't_cymmxdata'

    ID = Column(Integer, primary_key=True)
    Data = Column(Unicode, nullable=False)
    IdManager = Column(Integer, nullable=False)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
