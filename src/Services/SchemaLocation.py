# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:18:46
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaLocation.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 17:59:41
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelLocation, ModelUser
from pydantic import BaseModel, Field
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
    ModelLocation, update_exclude, table_name="ModelLocationUpdateSingleGetSchema"
)


class ModelLocationUpdateMultipleGetSchema(BaseModel):
    data: List[ModelLocationUpdateSingleGetSchema]
    n: int


class ModelLocationUpdateSingleTableSchema(ModelLocationUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


class ModelLocationUpdateMultipleTableSchema(BaseModel):
    data: List[ModelLocationUpdateSingleTableSchema]
    n: int


ModelLocationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocation,
    insert_exclude,
    ModelLocation_nullable_columns,
    table_name="ModelLocationInsertSingleGetSchema",
)


class ModelLocationInsertMultipleGetSchema(BaseModel):
    data: List[ModelLocationInsertSingleGetSchema]
    n: int


class ModelLocationInsertSingleTableSchema(ModelLocationInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


class ModelLocationInsertMultipleTableSchema(BaseModel):
    data: List[ModelLocationInsertSingleTableSchema]
    n: int


ModelLocationSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelLocation,
    select_out_exclude,
    table_name="ModelLocationSelectOutSingleTableSchemaBase",
)

ModelLocationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelLocation,
    select_in_exclude,
    [],
    table_name="ModelLocationSelectInSingleTableSchema",
)


class ModelLocationSelectOutSingleTableSchema(
    ModelLocationSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


sub_location = select(ModelLocation).where(ModelLocation.IMark == 0).subquery()  # type: ignore
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
ModelLocation_sub_stmt = (
    select(sub_location, sub_user.c.Name.label("ID_Manager_Name"))
    .outerjoin(sub_user, sub_user.c.ID == sub_location.c.IdManager)
    .subquery()  # type: ignore
)
