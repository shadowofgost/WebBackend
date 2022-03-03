"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:29:53
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaUser.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 20:29:18
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelUser
from pydantic import BaseModel, Field, create_model
from sqlalchemy import select
from sqlalchemy.orm import aliased

from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

ModelUser_nullable_columns = ["Yue", "Yue2", "Email", "Phone", "LocalID"]
ModelUser_nullable_columns.extend(nullable)

ModelUserUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelUser, update_exclude)
ModelUserUpdateSingleGetSchema = create_model(
    "ModelUserUpdateSingleGetSchema", __base__=ModelUserUpdateSingleGetSchema
)


class ModelUserUpdateMultipleGetSchema(BaseModel):
    data: List[ModelUserUpdateSingleGetSchema]
    n: int


class ModelUserUpdateSingleTableSchema(ModelUserUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelUserUpdateMultipleTableSchema(BaseModel):
    data: List[ModelUserUpdateSingleTableSchema]
    n: int


ModelUserInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUser, insert_exclude, ModelUser_nullable_columns
)
ModelUserInsertSingleGetSchema = create_model(
    "ModelUserInsertSingleGetSchema", __base__=ModelUserInsertSingleGetSchema
)


class ModelUserInsertMultipleGetSchema(BaseModel):
    data: List[ModelUserInsertSingleGetSchema]
    n: int


class ModelUserInsertSingleTableSchema(ModelUserInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelUserInsertMultipleTableSchema(BaseModel):
    data: List[ModelUserInsertSingleTableSchema]
    n: int


ModelUserSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelUser, select_out_exclude
)
ModelUserSelectOutSingleTableSchemaBase = create_model(
    "ModelUserSelectOutSingleTableSchemaBase",
    __base__=ModelUserSelectOutSingleTableSchemaBase,
)
ModelUserSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUser, select_in_exclude, []
)
ModelUserSelectInSingleTableSchema = create_model(
    "ModelUserSelectInSingleTableSchema", __base__=ModelUserSelectInSingleTableSchema
)


class ModelUserSelectOutSingleTableSchema(ModelUserSelectOutSingleTableSchemaBase):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


user1 = aliased(ModelUser)
ModelUser_sub_stmt = (
    select(
        ModelUser,
        user1.Name.label("ID_Manager_Name"),
    ).join(user1, user1.ID == ModelUser.IdManager, isouter=True)
).subquery()