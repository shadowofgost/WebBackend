"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelDepartment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 16:38:47
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
from .ModelPublic import (
    ModelPublic,
    nullable,
    sqlalchemy_to_pydantic,
    update_exclude,
    insert_exclude,
    select_out_exclude,
    select_in_exclude,
    format_current_time,
)

ModelDepartment_nullable_columns = []
ModelDepartment_nullable_columns.extend(nullable)


class ModelDepartment(ModelPublic):
    __tablename__ = "t_cydept"

    ID_Parent = Column(BigInteger, index=True, comment="父级部门ID", doc="顶级部门值为0")
    Name = Column(Unicode(32), index=True, comment="部门名称", doc="部门的名称")
