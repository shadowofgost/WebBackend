"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/UserModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 00:50:48
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


class TCyuser(Base):
    __tablename__ = 't_cyuser'

    ID = Column(Integer, primary_key=True)
    Deptid = Column(Integer, nullable=False)
    Nocard = Column(Unicode(32))
    NoUser = Column(Unicode(32))
    Name = Column(Unicode(32))
    Psw = Column(Unicode(32))
    Sex = Column(Integer)
    Attr = Column(Integer)
    AttrJf = Column(Integer)
    Yue = Column(Integer)
    Yue2 = Column(Integer)
    TimeUpdate = Column(Integer)
    IdManager = Column(Integer)
    LocalID = Column(Unicode(1024))
    IMark = Column(Integer)
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    back_up1 = Column(Unicode(254))


class TCyuserex(Base):
    __tablename__ = 't_cyuserex'

    ID = Column(Integer, primary_key=True)
    Photo = Column(LargeBinary, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Rem = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    Photo_dataF = Column(Unicode)
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    back_up1 = Column(Unicode(254))
