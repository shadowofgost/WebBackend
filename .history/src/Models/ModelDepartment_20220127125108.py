"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelDepartment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-27 12:08:38
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
from .PublicValuesAndSchemas import error_database_execution, error_schema_validation
from .ModelUser import ModelUser

ModelDepartment_nullable_columns = []
ModelDepartment_nullable_columns.extend(nullable)


class ModelDepartment(ModelPublic):
    __tablename__ = "t_cydept"

    ID_Parent = Column(BigInteger, index=True, comment="父级部门ID", doc="顶级部门值为0")
    Name = Column(Unicode(32), index=True, comment="部门名称", doc="部门的名称")
    Name2 = Column(Unicode(32), index=True, comment="部门名称的简写", doc="部门的名称的简写")


ModelDepartmentUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelDepartment, update_exclude
)


class ModelDepartmentUpdateMultipleGetSchema(BaseModel):
    data: List[ModelDepartmentUpdateSingleGetSchema]
    n: int


class ModelDepartmentUpdateSingleTableSchema(ModelDepartmentUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelDepartmentUpdateMultipleTableSchema(BaseModel):
    data: List[ModelDepartmentUpdateSingleTableSchema]
    n: int


ModelDepartmentInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelDepartment, insert_exclude, ModelDepartment_nullable_columns
)


class ModelDepartmentInsertMultipleGetSchema(BaseModel):
    data: List[ModelDepartmentInsertSingleGetSchema]
    n: int


class ModelDepartmentInsertSingleTableSchema(ModelDepartmentInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelDepartmentInsertMultipleTableSchema(BaseModel):
    data: List[ModelDepartmentInsertSingleTableSchema]
    n: int


ModelDepartmentSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelDepartment, select_out_exclude
)


class ModelDepartmentSelectOutSingleTableSchema(
    ModelDepartmentSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelDepartmentSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelDepartment, select_in_exclude, []
)
ModelDepartment_sub_stmt = (
    select(ModelDepartment, ModelUser.Name.label("ID_Manager_Name")).join(
        ModelUser, ModelDepartment.IdManager == ModelUser.ID, isouter=True
    )
).subquery()
