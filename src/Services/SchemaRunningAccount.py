"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:29:09
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaRunningAccount.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 17:55:29
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelRunningAccount, ModelUser
from pydantic import BaseModel, Field, create_model
from sqlalchemy import select
from sqlalchemy.orm import  aliased

from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

ModelRunningAccount_nullable_columns = ["Money", "Param1"]
ModelRunningAccount_nullable_columns.extend(nullable)

ModelRunningAccountUpdateSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelRunningAccount, update_exclude
)
ModelRunningAccountUpdateSingleGetSchemaBase = create_model(
    "ModelRunningAccountUpdateSingleGetSchemaBase",
    __base__=ModelRunningAccountUpdateSingleGetSchemaBase,
)


class ModelRunningAccountUpdateSingleGetSchema(
    ModelRunningAccountUpdateSingleGetSchemaBase
):
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )

    class Config:
        orm_mode = True


class ModelRunningAccountUpdateMultipleGetSchema(BaseModel):
    data: List[ModelRunningAccountUpdateSingleGetSchema]
    n: int


class ModelRunningAccountUpdateSingleTableSchema(
    ModelRunningAccountUpdateSingleGetSchemaBase
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelRunningAccountUpdateMultipleTableSchema(BaseModel):
    data: List[ModelRunningAccountUpdateSingleTableSchema]
    n: int


ModelRunningAccountInsertSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelRunningAccount, insert_exclude, ModelRunningAccount_nullable_columns
)
ModelRunningAccountInsertSingleGetSchemaBase = create_model(
    "ModelRunningAccountInsertSingleGetSchemaBase",
    __base__=ModelRunningAccountInsertSingleGetSchemaBase,
)


class ModelRunningAccountInsertSingleGetSchema(
    ModelRunningAccountInsertSingleGetSchemaBase
):
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )

    class Config:
        orm_mode = True


class ModelRunningAccountInsertMultipleGetSchema(BaseModel):
    data: List[ModelRunningAccountInsertSingleGetSchema]
    n: int


class ModelRunningAccountInsertSingleTableSchema(
    ModelRunningAccountInsertSingleGetSchemaBase
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelRunningAccountInsertMultipleTableSchema(BaseModel):
    data: List[ModelRunningAccountInsertSingleTableSchema]
    n: int


ModelRunningAccountSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelRunningAccount, select_out_exclude
)
ModelRunningAccountSelectOutSingleTableSchemaBase = create_model(
    "ModelRunningAccountSelectOutSingleTableSchemaBase",
    __base__=ModelRunningAccountSelectOutSingleTableSchemaBase,
)


class ModelRunningAccountSelectOutSingleTableSchema(
    ModelRunningAccountSelectOutSingleTableSchemaBase
):
    ID_User_Name: Optional[str] = Field(
        default=None, title="打卡签到者的姓名", description="这次打卡签到者的姓名"
    )
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelRunningAccountSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelRunningAccount, select_in_exclude, []
)
ModelRunningAccountSelectInSingleTableSchema = create_model(
    "ModelRunningAccountSelectInSingleTableSchema",
    __base__=ModelRunningAccountSelectInSingleTableSchema,
)
user1 = aliased(ModelUser)
ModelRunningAccount_sub_stmt = (
    select(
        ModelRunningAccount,
        ModelUser.Name.label("ID_User_Name"),
        ModelUser.NoUser.label("ID_User_NoUser"),
        user1.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelRunningAccount.ID_User == ModelUser.ID, isouter=True)
    .join(user1, ModelRunningAccount.IdManager == user1.ID, isouter=True)
    .where(ModelRunningAccount.Type_field == 4097)
    .subquery()
)