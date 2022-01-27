"""
# @Time             : 2022-01-13 23:23:15
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/ModelRunningAccount.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 13:15:27
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

class ModelRunningAccount(ModelPublic):
    __tablename__ = 't_cyrunningaccount'

    ID_User = Column(BigInteger, index=True)
    Time = Column(SmallInteger,index=True)
    Type_field = Column(SmallInteger,index=True,name="Type")
    Money = Column(Integer)
    Param1 = Column(BigInteger,index=True)
    Param2 = Column(BigInteger, index=True)
