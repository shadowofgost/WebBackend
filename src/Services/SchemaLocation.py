"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:18:46
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaLocation.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-24 10:57:14
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelLocation, ModelUser
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

ModelLocation_nullable_columns = []
ModelLocation_nullable_columns.extend(nullable)

ModelLocationUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocation, update_exclude
)
ModelLocationUpdateSingleGetSchema = create_model(
    "ModelLocationUpdateSingleGetSchema", __base__=ModelLocationUpdateSingleGetSchema
)


class ModelLocationUpdateMultipleGetSchema(BaseModel):
    data: List[ModelLocationUpdateSingleGetSchema]
    n: int


class ModelLocationUpdateSingleTableSchema(ModelLocationUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelLocationUpdateMultipleTableSchema(BaseModel):
    data: List[ModelLocationUpdateSingleTableSchema]
    n: int


ModelLocationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocation, insert_exclude, ModelLocation_nullable_columns
)
ModelLocationInsertSingleGetSchema = create_model(
    "ModelLocationInsertSingleGetSchema", __base__=ModelLocationInsertSingleGetSchema
)


class ModelLocationInsertMultipleGetSchema(BaseModel):
    data: List[ModelLocationInsertSingleGetSchema]
    n: int


class ModelLocationInsertSingleTableSchema(ModelLocationInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelLocationInsertMultipleTableSchema(BaseModel):
    data: List[ModelLocationInsertSingleTableSchema]
    n: int


ModelLocationSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelLocation, select_out_exclude
)
ModelLocationSelectOutSingleTableSchemaBase = create_model(
    "ModelLocationSelectOutSingleTableSchemaBase",
    __base__=ModelLocationSelectOutSingleTableSchemaBase,
)
ModelLocationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelLocation, select_in_exclude, []
)
ModelLocationSelectInSingleTableSchema = create_model(
    "ModelLocationSelectInSingleTableSchema",
    __base__=ModelLocationSelectInSingleTableSchema,
)


class ModelLocationSelectOutSingleTableSchema(
    ModelLocationSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelLocation_sub_stmt = (
    select(ModelLocation, ModelUser.Name.label("ID_Manager_Name"))
    .join(ModelUser, ModelUser.ID == ModelLocation.IdManager, isouter=True)
    .where(ModelLocation.IMark == 0)
    .subquery()
)
