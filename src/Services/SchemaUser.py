# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:29:53
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaUser.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 19:19:28
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelUser
from pydantic import BaseModel, Field, create_model, validator
from sqlalchemy import select
from sqlalchemy.orm import aliased
from passlib.context import CryptContext
from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

##TODO:自动数据加密系统
pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
ModelUser_nullable_columns = ["Yue", "Yue2", "Email", "Phone", "LocalID"]
ModelUser_nullable_columns.extend(nullable)

ModelUserUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUser, update_exclude, table_name="ModelUserUpdateSingleGetSchema"
)


class ModelUserUpdateMultipleGetSchema(BaseModel):
    data: List[ModelUserUpdateSingleGetSchema]
    n: int


class ModelUserUpdateSingleTableSchema(ModelUserUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


##TODO:暗文加密系统的表单
"""
class ModelUserUpdateSingleTableSchema(ModelUserUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0
    @validator('Psw', pre=True)
    def Psw_hash(cls, v):
        if v is not None:
            return pwd_context.hash(v)
    @validator('NoSfz', pre=True)
    def NoSfz_hash(cls, v):
        if v is not None:
            return pwd_context.hash(v)
"""


class ModelUserUpdateMultipleTableSchema(BaseModel):
    data: List[ModelUserUpdateSingleTableSchema]
    n: int


ModelUserInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUser,
    insert_exclude,
    ModelUser_nullable_columns,
    table_name="ModelUserInsertSingleGetSchema",
)


class ModelUserInsertMultipleGetSchema(BaseModel):
    data: List[ModelUserInsertSingleGetSchema]
    n: int


class ModelUserInsertSingleTableSchema(ModelUserInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


##TODO:暗文加密系统的表单
"""
class ModelUserInsertSingleTableSchema(ModelUserInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0
    @validator('Psw', pre=True)
    def Psw_hash(cls, v):
        if v is not None:
            return pwd_context.hash(v)
    @validator('NoSfz', pre=True)
    def NoSfz_hash(cls, v):
        if v is not None:
            return pwd_context.hash(v)
"""


class ModelUserInsertMultipleTableSchema(BaseModel):
    data: List[ModelUserInsertSingleTableSchema]
    n: int


ModelUserSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelUser, select_out_exclude, table_name="ModelUserSelectOutSingleTableSchemaBase"
)
ModelUserSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUser, select_in_exclude, [], table_name="ModelUserSelectInSingleTableSchema"
)


class ModelUserSelectOutSingleTableSchema(ModelUserSelectOutSingleTableSchemaBase):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


##TODO:WARNING:随着sqlalchemy的升级，subquery的查询列的方法会发生改变，会从原来的sub.c.column_name变成sub.column_name
sub_sub = select(ModelUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
ModelUser_sub_stmt = (
    select(
        sub_sub,
        sub_user.c.Name.label("ID_Manager_Name"),
    )
    .outerjoin(sub_user, sub_user.c.ID == sub_sub.c.IdManager)
    .subquery()  # type: ignore
)
