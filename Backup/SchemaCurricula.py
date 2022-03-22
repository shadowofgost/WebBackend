# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:16:37
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-13 17:39:35
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelCurricula, ModelLocation, ModelUser
from pydantic import BaseModel, Field, create_model
from sqlalchemy import select
from sqlalchemy.orm import Session, aliased

from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

ModelCurricula_nullable_columns = [
    "RangeUsers",
    "ListDepts",
    "RangeEqus",
    "ListPlaces",
    "MapUser2Equ",
    "AboutSpeaker",
]
ModelCurricula_nullable_columns.extend(nullable)
ModelCurriculaUpdateSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelCurricula, update_exclude
)
ModelCurriculaUpdateSingleGetSchemaBase = create_model(
    "ModelCurriculaUpdateSingleGetSchemaBase",
    __base__=ModelCurriculaUpdateSingleGetSchemaBase,
)


class ModelCurriculaUpdateSingleGetSchema(ModelCurriculaUpdateSingleGetSchemaBase):
    ID_Speaker_NoUser: int

    class Config:
        orm_mode = True


class ModelCurriculaUpdateMultipleGetSchema(BaseModel):
    data: List[ModelCurriculaUpdateSingleGetSchema]
    n: int


class ModelCurriculaUpdateSingleTableSchema(ModelCurriculaUpdateSingleGetSchemaBase):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelCurriculaUpdateMultipleTableSchema(BaseModel):
    data: List[ModelCurriculaUpdateSingleTableSchema]
    n: int


ModelCurriculaInsertSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelCurricula, insert_exclude, ModelCurricula_nullable_columns
)
ModelCurriculaInsertSingleGetSchemaBase = create_model(
    "ModelCurriculaInsertSingleGetSchemaBase",
    __base__=ModelCurriculaInsertSingleGetSchemaBase,
)


class ModelCurriculaInsertSingleGetSchema(ModelCurriculaInsertSingleGetSchemaBase):
    ID_Speaker_NoUser: int

    class Config:
        orm_mode = True


class ModelCurriculaInsertMultipleGetSchema(BaseModel):
    data: List[ModelCurriculaInsertSingleGetSchema]
    n: int


class ModelCurriculaInsertSingleTableSchema(ModelCurriculaInsertSingleGetSchemaBase):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelCurriculaInsertMultipleTableSchema(BaseModel):
    data: List[ModelCurriculaInsertSingleTableSchema]
    n: int


ModelCurriculaSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelCurricula, select_out_exclude
)

ModelCurriculaSelectOutSingleTableSchemaBase = create_model(
    "ModelCurriculaSelectOutSingleTableSchemaBase",
    __base__=ModelCurriculaSelectOutSingleTableSchemaBase,
)


class ModelCurriculaSelectOutSingleTableSchema(
    ModelCurriculaSelectOutSingleTableSchemaBase
):
    ID_Location_Name: Optional[str] = Field(
        default=None, title="地点名称", description="这是这节课程安排课对应的地点名称"
    )
    ID_Speaker_Name: Optional[str] = Field(
        default=None, title="老师名称", description="这是这节课程安排课对应的上课老师的姓名"
    )
    ID_Speaker_NoUser: Optional[int] = Field(
        default=None, title="老师/演讲者的教职工号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelCurriculaSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelCurricula, select_in_exclude, []
)
ModelCurriculaSelectInSingleTableSchema = create_model(
    "ModelCurriculaSelectInSingleTableSchema",
    __base__=ModelCurriculaSelectInSingleTableSchema,
)
sub_curricula = select(ModelCurricula).where(ModelCurricula.IMark == 0).subquery()  # type: ignore
sub_location = select(ModelLocation.ID, ModelLocation.Name).where(ModelLocation.IMark == 0).subquery()  # type: ignore
sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
user1 = aliased(sub_user)
ModelCurricula_sub_stmt = (
    select(
        sub_curricula,
        sub_location.c.Name.label("ID_Location_Name"),  # type: ignore
        sub_user.c.Name.label("ID_Speaker_Name"),
        sub_user.c.NoUser.label("ID_Speaker_NoUser"),
        user1.c.Name.label("ID_Manager_Name"),
    )
    .outerjoin(sub_user, sub_user.c.ID == sub_curricula.c.ID_Speaker)
    .outerjoin(sub_location, sub_location.c.ID == sub_curricula.c.ID_Location)
    .outerjoin(user1, user1.c.ID == sub_curricula.c.IdManager)  # type: ignore
    .subquery()  # type: ignore
)
