# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:18:25
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaEquipment.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-13 17:43:17
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelEquipment, ModelLocation, ModelUser
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

ModelEquipment_nullable_columns = [
    "ID_IP",
    "MAC",
    "iTimeBegin",
    "iTimeLogin",
    "WhiteList",
]
ModelEquipment_nullable_columns.extend(nullable)

ModelEquipmentUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelEquipment, update_exclude
)
ModelEquipmentUpdateSingleGetSchema = create_model(
    "ModelEquipmentUpdateSingleGetSchema", __base__=ModelEquipmentUpdateSingleGetSchema
)


class ModelEquipmentUpdateMultipleGetSchema(BaseModel):
    data: List[ModelEquipmentUpdateSingleGetSchema]
    n: int


class ModelEquipmentUpdateSingleTableSchema(ModelEquipmentUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelEquipmentUpdateMultipleTableSchema(BaseModel):
    data: List[ModelEquipmentUpdateSingleTableSchema]
    n: int


ModelEquipmentInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelEquipment, insert_exclude, ModelEquipment_nullable_columns
)
ModelEquipmentInsertSingleGetSchema = create_model(
    "ModelEquipmentInsertSingleGetSchema", __base__=ModelEquipmentInsertSingleGetSchema
)


class ModelEquipmentInsertMultipleGetSchema(BaseModel):
    data: List[ModelEquipmentInsertSingleGetSchema]
    n: int


class ModelEquipmentInsertSingleTableSchema(ModelEquipmentInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelEquipmentInsertMultipleTableSchema(BaseModel):
    data: List[ModelEquipmentInsertSingleTableSchema]
    n: int


ModelEquipmentSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelEquipment, select_out_exclude
)
ModelEquipmentSelectOutSingleTableSchemaBase = create_model(
    "ModelEquipmentSelectOutSingleTableSchemaBase",
    __base__=ModelEquipmentSelectOutSingleTableSchemaBase,
)


class ModelEquipmentSelectOutSingleTableSchema(
    ModelEquipmentSelectOutSingleTableSchemaBase
):
    ID_Location_Name: Optional[str] = Field(
        default=None, title="地点名称", description="这是这节课程安排课对应的地点名称"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelEquipmentSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelEquipment, select_in_exclude, []
)
ModelEquipmentSelectInSingleTableSchema = create_model(
    "ModelEquipmentSelectInSingleTableSchema",
    __base__=ModelEquipmentSelectInSingleTableSchema,
)
sub_location = select(ModelLocation.ID, ModelLocation.Name).where(ModelLocation.IMark == 0).subquery()  # type: ignore
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
sub_equipment = select(ModelEquipment).where(ModelEquipment.IMark == 0).subquery()  # type: ignore
ModelEquipment_sub_stmt = (
    select(
        sub_equipment,
        sub_location.c.Name.label("ID_Location_Name"),
        sub_user.c.Name.label("ID_Manager_Name"),  # type: ignore
    )
    .outerjoin(sub_user, sub_user.c.ID == sub_equipment.c.IdManager)
    .outerjoin(sub_location, sub_location.c.ID == sub_equipment.c.ID_Location)
    .subquery()  # type: ignore
)
