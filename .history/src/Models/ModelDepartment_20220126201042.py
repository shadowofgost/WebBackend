"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelDepartment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 20:00:41
# @LastAuthor       : Albert Wang
"""
from typing import Container, List, Optional

from pydantic import BaseModel, Field
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    select,
)
from sqlalchemy.orm import Session, sessionmaker

from .ModelPublic import (
    ModelPublic,
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)
from .PublicValues import error_database_execution, error_schema_validation

ModelDepartment_nullable_columns = []
ModelDepartment_nullable_columns.extend(nullable)


class ModelDepartment(ModelPublic):
    __tablename__ = "t_cydept"

    ID_Parent = Column(BigInteger, index=True, comment="父级部门ID", doc="顶级部门值为0")
    Name = Column(Unicode(32), index=True, comment="部门名称", doc="部门的名称")
    Name2=Column(Unicode(32), index=True, comment="部门名称的简写", doc="部门的名称的简写")


ModelDepartmentUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelDepartment, update_exclude
)


class ModelDepartmentUpdateMultipleGetSchema(ModelDepartmentUpdateSingleGetSchema):
    data: List[ModelDepartmentUpdateSingleGetSchema]
    n: int


class ModelDepartmentUpdateSingleTableSchema(ModelDepartmentUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelDepartmentUpdateMultipleTableSchema(ModelDepartmentUpdateSingleTableSchema):
    data: List[ModelDepartmentUpdateSingleTableSchema]
    n: int


ModelDepartmentInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelDepartment, insert_exclude, ModelDepartment_nullable_columns
)


class ModelDepartmentInsertMultipleGetSchema(ModelDepartmentInsertSingleGetSchema):
    data: List[ModelDepartmentInsertSingleGetSchema]
    n: int


class ModelDepartmentInsertSingleTableSchema(ModelDepartmentInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelDepartmentInsertMultipleTableSchema(ModelDepartmentInsertSingleTableSchema):
    data: List[ModelDepartmentInsertSingleTableSchema]
    n: int


ModelDepartmentSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelDepartment, select_out_exclude
)
ModelDepartmentSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelDepartment, select_in_exclude, []
)
