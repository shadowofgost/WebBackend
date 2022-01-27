"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/ModelDepartment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-16 12:31:32
# @LastAuthor       : Albert Wang
"""
from turtle import title
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
from .Public import ModelPublic,exclude,nullable


class ModelDepartment(ModelPublic):
    __tablename__ = 't_cydept'


    ID_Parent = Column(BigInteger, index=True,title="父级部门ID",doc="顶级部门值为0，必须有值")
    Name = Column(Unicode(32),index=True,title="部门名称",doc="部门的名称")
