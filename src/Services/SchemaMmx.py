# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:19:25
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaMmx.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-13 18:08:30
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelMmxData, ModelMmx, ModelUser
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

ModelMmx_nullable_columns = []
ModelMmx_nullable_columns.extend(nullable)

ModelMmxUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmx, update_exclude)
ModelMmxUpdateSingleGetSchema = create_model(
    "ModelMmxUpdateSingleGetSchema", __base__=ModelMmxUpdateSingleGetSchema
)


class ModelMmxUpdateMultipleGetSchema(BaseModel):
    data: List[ModelMmxUpdateSingleGetSchema]
    n: int


class ModelMmxUpdateSingleTableSchema(ModelMmxUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelMmxUpdateMultipleTableSchema(BaseModel):
    data: List[ModelMmxUpdateSingleTableSchema]
    n: int


ModelMmxInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelMmx, insert_exclude, ModelMmx_nullable_columns
)
ModelMmxInsertSingleGetSchema = create_model(
    "ModelMmxInsertSingleGetSchema", __base__=ModelMmxInsertSingleGetSchema
)


class ModelMmxInsertMultipleGetSchema(BaseModel):
    data: List[ModelMmxInsertSingleGetSchema]
    n: int


class ModelMmxInsertSingleTableSchema(ModelMmxInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxInsertMultipleTableSchema(BaseModel):
    data: List[ModelMmxInsertSingleTableSchema]
    n: int


ModelMmxSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelMmx, select_out_exclude
)
ModelMmxSelectOutSingleTableSchemaBase = create_model(
    "ModelMmxSelectOutSingleTableSchemaBase",
    __base__=ModelMmxSelectOutSingleTableSchemaBase,
)


class ModelMmxSelectOutSingleTableSchema(ModelMmxSelectOutSingleTableSchemaBase):
    Data: Optional[str] = Field(
        default=None,
        title="数据",
        description="数据",
        max_length=1024,
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelMmxSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmx, select_in_exclude, []
)
ModelMmxSelectInSingleTableSchema = create_model(
    "ModelMmxSelectInSingleTableSchema", __base__=ModelMmxSelectInSingleTableSchema
)
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
sub_Mmx = select(ModelMmx).where(ModelMmx.IMark == 0).subquery()  # type: ignore
sub_Mmx_Data = select(ModelMmxData).where(ModelMmxData.IMark == 0).subquery()  # type: ignore
ModelMmx_sub_stmt = (
    select(
        sub_Mmx,
        sub_Mmx_Data.c.Data.label("Data"),
        sub_user.c.Name.label("ID_Manager_Name"),
    )
    .outerjoin(sub_user, sub_user.c.ID == sub_Mmx.c.IdManager)
    .outerjoin(sub_Mmx_Data, sub_Mmx_Data.c.ID == sub_Mmx.c.ID_Data)
    .subquery()  # type: ignore
)
