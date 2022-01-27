"""
# @Time             : 2022-01-13 23:23:28
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/TableInformationModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 01:43:09
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
class TCytableinfo(Base):
    __tablename__ = 't_cytableinfo'

    ID = Column(Integer, primary_key=True)
    Name = Column(Unicode(50))
    NameTable = Column(Unicode(50))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    IdManager = Column(Integer)
