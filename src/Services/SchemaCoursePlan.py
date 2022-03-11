# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:19:24
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaCoursePlan.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 19:38:33
# @Software         : Vscode
"""
from typing import List, Optional

from Models import (
    ModelCoursePlan,
    ModelCurricula,
    ModelLocation,
    ModelUser,
)
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

ModelCoursePlan_nullable_columns = [
    "RangeUsers",
    "ListDepts",
    "RangeEqus",
    "ListPlaces",
    "MapUser2Equ",
    "AboutSpeaker",
]
ModelCoursePlan_nullable_columns.extend(nullable)

ModelCoursePlanUpdateSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelCoursePlan, update_exclude
)
ModelCoursePlanUpdateSingleGetSchemaBase = create_model(
    "ModelCoursePlanUpdateSingleGetSchemaBase",
    __base__=ModelCoursePlanUpdateSingleGetSchemaBase,
)


class ModelCoursePlanUpdateSingleGetSchema(ModelCoursePlanUpdateSingleGetSchemaBase):
    ID_Speaker_NoUser: int

    class Config:
        orm_mode = True


class ModelCoursePlanUpdateMultipleGetSchema(BaseModel):
    data: List[ModelCoursePlanUpdateSingleGetSchema]
    n: int


class ModelCoursePlanUpdateSingleTableSchema(ModelCoursePlanUpdateSingleGetSchemaBase):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelCoursePlanUpdateMultipleTableSchema(BaseModel):
    data: List[ModelCoursePlanUpdateSingleTableSchema]
    n: int


ModelCoursePlanInsertSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelCoursePlan, insert_exclude, ModelCoursePlan_nullable_columns
)
ModelCoursePlanInsertSingleGetSchemaBase = create_model(
    "ModelCoursePlanInsertSingleGetSchemaBase",
    __base__=ModelCoursePlanInsertSingleGetSchemaBase,
)


class ModelCoursePlanInsertSingleGetSchema(ModelCoursePlanInsertSingleGetSchemaBase):
    ID_Speaker_NoUser: int

    class Config:
        orm_mode = True


class ModelCoursePlanInsertMultipleGetSchema(BaseModel):
    data: List[ModelCoursePlanInsertSingleGetSchema]
    n: int


class ModelCoursePlanInsertSingleTableSchema(ModelCoursePlanInsertSingleGetSchemaBase):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelCoursePlanInsertMultipleTableSchema(BaseModel):
    data: List[ModelCoursePlanInsertSingleTableSchema]
    n: int


ModelCoursePlanSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelCoursePlan, select_out_exclude
)
ModelCoursePlanSelectOutSingleTableSchemaBase = create_model(
    "ModelCoursePlanSelectOutSingleTableSchemaBase",
    __base__=ModelCoursePlanSelectOutSingleTableSchemaBase,
)


class ModelCoursePlanSelectOutSingleTableSchema(
    ModelCoursePlanSelectOutSingleTableSchemaBase
):
    ID_Curricula_Name: Optional[str] = Field(
        default=None, title="课程名称", description="这是这节课程安排课对应的课程名称"
    )
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


ModelCoursePlanSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelCoursePlan, select_in_exclude, []
)
ModelCoursePlanSelectInSingleTableSchema = create_model(
    "ModelCoursePlanSelectInSingleTableSchema",
    __base__=ModelCoursePlanSelectInSingleTableSchema,
)
##TODO:修改sql查询语句因为超过三个join使得mysql的性能会大幅下降。
user1 = aliased(ModelUser)
ModelCoursePlan_sub_stmt = (
    select(
        ModelCoursePlan,
        ModelCurricula.Name.label("ID_Curricula_Name"),
        ModelLocation.Name.label("ID_Location_Name"),  # type: ignore
        ModelUser.Name.label("ID_Speaker_Name"),
        ModelUser.NoUser.label("ID_Speaker_NoUser"),
        user1.Name.label("ID_Manager_Name"),
    )
    .where(ModelCurricula.IMark == 0)
    .where(ModelUser.IMark == 0)
    .where(ModelLocation.IMark == 0)
    .where(user1.IMark == 0)
    .join(
        ModelCurricula,
        ModelCurricula.ID == ModelCoursePlan.ID_Curricula,
        isouter=True,
    )
    .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
    .join(
        ModelLocation,
        ModelLocation.ID == ModelCoursePlan.ID_Location,
        isouter=True,
    )
    .join(user1, user1.ID == ModelCoursePlan.IdManager, isouter=True)  # type: ignore
    .subquery()  # type: ignore
)
