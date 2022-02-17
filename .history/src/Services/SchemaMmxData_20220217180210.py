"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:19:36
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaMmxData.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 17:53:10
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelMmxData, ModelUser
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

ModelMmxData_nullable_columns = ["Data"]
ModelMmxData_nullable_columns.extend(nullable)


ModelMmxDataUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmxData, update_exclude)
ModelMmxDataUpdateSingleGetSchema = create_model(
    "ModelMmxDataUpdateSingleGetSchema", __base__=ModelMmxDataUpdateSingleGetSchema
)


class ModelMmxDataUpdateMultipleGetSchema(BaseModel):
    data: List[ModelMmxDataUpdateSingleGetSchema]
    n: int


class ModelMmxDataUpdateSingleTableSchema(ModelMmxDataUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelMmxDataUpdateMultipleTableSchema(ModelMmxDataUpdateSingleTableSchema):
    data: List[ModelMmxDataUpdateSingleTableSchema]
    n: int


ModelMmxDataInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelMmxData, insert_exclude, ModelMmxData_nullable_columns
)
ModelMmxDataInsertSingleGetSchema = create_model(
    "ModelMmxDataInsertSingleGetSchema", __base__=ModelMmxDataInsertSingleGetSchema
)


class ModelMmxDataInsertMultipleGetSchema(BaseModel):
    data: List[ModelMmxDataInsertSingleGetSchema]
    n: int


class ModelMmxDataInsertSingleTableSchema(ModelMmxDataInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxDataInsertMultipleTableSchema(BaseModel):
    data: List[ModelMmxDataInsertSingleTableSchema]
    n: int


ModelMmxDataSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelMmxData, select_out_exclude
)
ModelMmxDataSelectOutSingleTableSchemaBase = create_model(
    "ModelMmxDataSelectOutSingleTableSchemaBase",
    __base__=ModelMmxDataSelectOutSingleTableSchemaBase,
)


class ModelMmxDataSelectOutSingleTableSchema(
    ModelMmxDataSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelMmxDataSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmxData, select_in_exclude, []
)
ModelMmxDataSelectInSingleTableSchema = create_model(
    "ModelMmxDataSelectInSingleTableSchema",
    __base__=ModelMmxDataSelectInSingleTableSchema,
)
ModelMmxData_sub_stmt = (
    select(
        ModelMmxData,
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelUser.ID == ModelMmxData.IdManager, isouter=True)
    .subquery()
)
