# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:17:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaDepartment.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 18:11:03
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
    ModelDepartment, update_exclude, table_name="ModelDepartmentUpdateSingleGetSchema"
)

class ModelDepartmentUpdateMultipleGetSchema(BaseModel):
    data: List[ModelDepartmentUpdateSingleGetSchema]
    n: int


class ModelDepartmentUpdateSingleTableSchema(ModelDepartmentUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


class ModelDepartmentUpdateMultipleTableSchema(BaseModel):
    data: List[ModelDepartmentUpdateSingleTableSchema]
    n: int


ModelDepartmentInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelDepartment, insert_exclude, ModelDepartment_nullable_columns,table_name="ModelDepartmentInsertSingleGetSchema"
)


class ModelDepartmentInsertMultipleGetSchema(BaseModel):
    data: List[ModelDepartmentInsertSingleGetSchema]
    n: int


class ModelDepartmentInsertSingleTableSchema(ModelDepartmentInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


class ModelDepartmentInsertMultipleTableSchema(BaseModel):
    data: List[ModelDepartmentInsertSingleTableSchema]
    n: int


ModelDepartmentSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelDepartment, select_out_exclude,table_name="ModelDepartmentSelectOutSingleTableSchemaBase"
)
ModelDepartmentSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelDepartment, select_in_exclude, [],table_name="ModelDepartmentSelectInSingleTableSchema"
)

class ModelDepartmentSelectOutSingleTableSchema(
    ModelDepartmentSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


sub_department = select(ModelDepartment).where(ModelDepartment.IMark == 0).subquery()  # type: ignore
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
ModelDepartment_sub_stmt = (
    select(sub_department, sub_user.c.Name.label("ID_Manager_Name"))
    .outerjoin(sub_user, sub_department.c.IdManager == sub_user.c.ID)
    .subquery()  # type: ignore
)
