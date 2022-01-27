"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelDepartment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 17:20:11
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
from pydantic import BaseModel, Field
from typing import Container, List, Optional
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
