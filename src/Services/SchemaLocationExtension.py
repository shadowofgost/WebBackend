# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:19:12
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaLocationExtension.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 18:15:13
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelLocationExtension, ModelLocation, ModelUser
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

ModelLocationExtension_nullable_columns = [
    "DateBegin",
    "DateEnd",
    "ModeRun",
    "ModeShangJi",
    "EnableDelayCharged",
    "DelayCharged",
    "EnableLimitYuE_SJ",
    "LimitYuE_SJ",
    "EnableLimitYuE_XJ",
    "LimitYuE_XJ",
    "EnableLimitTime_XJ",
    "LimitTime_XJ",
    "EnableWarnYuE",
    "EnableWarnTime",
    "WarnTime",
    "EnableMinCost",
    "MinCost",
    "Price",
    "PriceMinute",
    "GetEquName",
    "GetEquIp",
    "GetEquMac ",
]
ModelLocationExtension_nullable_columns.extend(nullable)

ModelLocationExtensionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocationExtension, update_exclude,table_name="ModelLocationExtensionUpdateSingleGetSchema"
)


class ModelLocationExtensionUpdateMultipleGetSchema(BaseModel):
    data: List[ModelLocationExtensionUpdateSingleGetSchema]
    n: int


class ModelLocationExtensionUpdateSingleTableSchema(
    ModelLocationExtensionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelLocationExtensionUpdateMultipleTableSchema(BaseModel):
    data: List[ModelLocationExtensionUpdateSingleTableSchema]
    n: int


ModelLocationExtensionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocationExtension, insert_exclude, ModelLocationExtension_nullable_columns,table_name="ModelLocationExtensionInsertSingleGetSchema"
)


class ModelLocationExtensionInsertMultipleGetSchema(BaseModel):
    data: List[ModelLocationExtensionInsertSingleGetSchema]
    n: int


class ModelLocationExtensionInsertSingleTableSchema(
    ModelLocationExtensionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelLocationExtensionInsertMultipleTableSchema(BaseModel):
    data: List[ModelLocationExtensionInsertSingleTableSchema]
    n: int


ModelLocationExtensionSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelLocationExtension, select_out_exclude,table_name="ModelLocationExtensionSelectOutSingleTableSchemaBase"
)
ModelLocationExtensionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelLocationExtension, select_in_exclude, [],table_name="ModelLocationExtensionSelectInSingleTableSchema"
)

class ModelLocationExtensionSelectOutSingleTableSchema(
    ModelLocationExtensionSelectOutSingleTableSchemaBase
):
    ID_Location_Name: Optional[str] = Field(
        default=None, title="地点名称", description="这是这节课程安排课对应的地点名称"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True

sub_location = select(ModelLocation.ID, ModelLocation.Name).where(ModelLocation.IMark == 0).subquery()  # type: ignore
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
sub_location_extension = select(ModelLocationExtension).where(ModelLocationExtension.IMark == 0).subquery()  # type: ignore
ModelLocationExtension_sub_stmt = (
    select(
        sub_location_extension,
        sub_location.c.Name.label("ID_Location_Name"),
        sub_user.c.Name.label("ID_Manager_Name"),  # type: ignore
    )
    .outerjoin(sub_user, sub_user.c.ID == sub_location_extension.c.IdManager)
    .outerjoin(sub_location, sub_location.c.ID == sub_location_extension.c.ID_Location)
    .subquery()  # type: ignore
)
