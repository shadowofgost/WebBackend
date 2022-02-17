"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:17:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaDepartment.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 17:42:33
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelDepartment, ModelUser
from pydantic import BaseModel, Field, create_model
from sqlalchemy import select

from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

ModelDepartment_nullable_columns = []
ModelDepartment_nullable_columns.extend(nullable)

ModelDepartmentUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelDepartment, update_exclude
)
ModelDepartmentUpdateSingleGetSchema = create_model(
    "ModelDepartmentUpdateSingleGetSchema",
    __base__=ModelDepartmentUpdateSingleGetSchema,
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
ModelDepartmentInsertSingleGetSchema = create_model(
    "ModelDepartmentInsertSingleGetSchema",
    __base__=ModelDepartmentInsertSingleGetSchema,
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
ModelDepartmentSelectOutSingleTableSchemaBase = create_model(
    "ModelDepartmentSelectOutSingleTableSchemaBase",
    __base__=ModelDepartmentSelectOutSingleTableSchemaBase,
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
ModelDepartmentSelectInSingleTableSchema = create_model(
    "ModelDepartmentSelectInSingleTableSchema",
    __base__=ModelDepartmentSelectInSingleTableSchema,
)
ModelDepartment_sub_stmt = (
    select(ModelDepartment, ModelUser.Name.label("ID_Manager_Name"))
    .join(ModelUser, ModelDepartment.IdManager == ModelUser.ID, isouter=True)
    .subquery()
)
