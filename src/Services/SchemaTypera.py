"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:29:45
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaTypera.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 19:40:53
# @Software         : Vscode
"""
from typing import List, Optional
from pydantic import BaseModel, Field, create_model
from sqlalchemy import select
from Models import ModelTypera, ModelUser


from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

ModelTypera_nullable_columns = []
ModelTypera_nullable_columns.extend(nullable)

ModelTyperaUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelTypera, update_exclude)
ModelTyperaUpdateSingleGetSchema = create_model(
    "ModelTyperaUpdateSingleGetSchema", __base__=ModelTyperaUpdateSingleGetSchema
)


class ModelTyperaUpdateMultipleGetSchema(BaseModel):
    data: List[ModelTyperaUpdateSingleGetSchema]
    n: int


class ModelTyperaUpdateSingleTableSchema(ModelTyperaUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelTyperaUpdateMultipleTableSchema(BaseModel):
    data: List[ModelTyperaUpdateSingleTableSchema]
    n: int


ModelTyperaInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTypera, insert_exclude, ModelTypera_nullable_columns
)
ModelTyperaInsertSingleGetSchema = create_model(
    "ModelTyperaInsertSingleGetSchema", __base__=ModelTyperaInsertSingleGetSchema
)


class ModelTyperaInsertMultipleGetSchema(BaseModel):
    data: List[ModelTyperaInsertSingleGetSchema]
    n: int


class ModelTyperaInsertSingleTableSchema(ModelTyperaInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelTyperaInsertMultipleTableSchema(BaseModel):
    data: List[ModelTyperaInsertSingleTableSchema]
    n: int


ModelTyperaSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelTypera, select_out_exclude
)
ModelTyperaSelectOutSingleTableSchemaBase = create_model(
    "ModelTyperaSelectOutSingleTableSchemaBase",
    __base__=ModelTyperaSelectOutSingleTableSchemaBase,
)


class ModelTyperaSelectOutSingleTableSchema(ModelTyperaSelectOutSingleTableSchemaBase):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelTyperaSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTypera, select_in_exclude, []
)
ModelTyperaSelectInSingleTableSchema = create_model(
    "ModelTyperaSelectInSingleTableSchema",
    __base__=ModelTyperaSelectInSingleTableSchema,
)
ModelTypera_sub_stmt = (
    select(
        ModelTypera,
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelUser.ID == ModelUser.IdManager, isouter=True)
    .where(ModelUser.IMark == 0)  # type: ignore
    .subquery()
)
