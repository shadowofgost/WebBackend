"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/DepartmentModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 01:20:24
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
class TCydept(Base):
    __tablename__ = 't_cydept'

    ID = Column(Integer, primary_key=True)
    ID_Parent = Column(Integer)
    Name = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IdManager = Column(Integer)
    IMark = Column(Integer)
    bakc_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
