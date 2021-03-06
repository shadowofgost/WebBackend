# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:29:31
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaTableInformation.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 18:58:44
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelTableInformation, ModelUser
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

ModelTableInformation_nullable_columns = []
ModelTableInformation_nullable_columns.extend(nullable)

ModelTableInformationUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, update_exclude,table_name="ModelTableInformationUpdateSingleGetSchema"
)


class ModelTableInformationUpdateMultipleGetSchema(BaseModel):
    data: List[ModelTableInformationUpdateSingleGetSchema]
    n: int


class ModelTableInformationUpdateSingleTableSchema(
    ModelTableInformationUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelTableInformationUpdateMultipleTableSchema(BaseModel):
    data: List[ModelTableInformationUpdateSingleTableSchema]
    n: int


ModelTableInformationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, insert_exclude, ModelTableInformation_nullable_columns,table_name="ModelTableInformationInsertSingleGetSchema"
)

class ModelTableInformationInsertMultipleGetSchema(BaseModel):
    data: List[ModelTableInformationInsertSingleGetSchema]
    n: int


class ModelTableInformationInsertSingleTableSchema(
    ModelTableInformationInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelTableInformationInsertMultipleTableSchema(BaseModel):
    data: List[ModelTableInformationInsertSingleTableSchema]
    n: int


ModelTableInformationSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelTableInformation, select_out_exclude,table_name="ModelTableInformationSelectOutSingleTableSchemaBase"
)
ModelTableInformationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, select_in_exclude, [],table_name="ModelTableInformationSelectInSingleTableSchema"
)

class ModelTableInformationSelectOutSingleTableSchema(
    ModelTableInformationSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True

sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
sub_tableinformation = select(ModelTableInformation).where(ModelTableInformation.IMark == 0).subquery()  # type: ignore
ModelTableInformation_sub_stmt = (
    select(
        sub_tableinformation,
        sub_user.c.Name.label("ID_Manager_Name"),
    )
    .outerjoin(sub_user, sub_user.c.ID == sub_tableinformation.c.IdManager)
    .subquery()  # type: ignore
)
