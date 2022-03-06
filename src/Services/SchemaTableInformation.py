"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:29:31
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaTableInformation.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-24 10:59:28
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
    ModelTableInformation, update_exclude
)
ModelTableInformationUpdateSingleGetSchema = create_model(
    "ModelTableInformationUpdateSingleGetSchema",
    __base__=ModelTableInformationUpdateSingleGetSchema,
)


class ModelTableInformationUpdateMultipleGetSchema(BaseModel):
    data: List[ModelTableInformationUpdateSingleGetSchema]
    n: int


class ModelTableInformationUpdateSingleTableSchema(
    ModelTableInformationUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelTableInformationUpdateMultipleTableSchema(BaseModel):
    data: List[ModelTableInformationUpdateSingleTableSchema]
    n: int


ModelTableInformationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, insert_exclude, ModelTableInformation_nullable_columns
)
ModelTableInformationInsertSingleGetSchema = create_model(
    "ModelTableInformationInsertSingleGetSchema",
    __base__=ModelTableInformationInsertSingleGetSchema,
)


class ModelTableInformationInsertMultipleGetSchema(BaseModel):
    data: List[ModelTableInformationInsertSingleGetSchema]
    n: int


class ModelTableInformationInsertSingleTableSchema(
    ModelTableInformationInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelTableInformationInsertMultipleTableSchema(BaseModel):
    data: List[ModelTableInformationInsertSingleTableSchema]
    n: int


ModelTableInformationSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelTableInformation, select_out_exclude
)
ModelTableInformationSelectOutSingleTableSchemaBase = create_model(
    "ModelTableInformationSelectOutSingleTableSchemaBase",
    __base__=ModelTableInformationSelectOutSingleTableSchemaBase,
)


class ModelTableInformationSelectOutSingleTableSchema(
    ModelTableInformationSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelTableInformationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, select_in_exclude, []
)
ModelTableInformationSelectInSingleTableSchema = create_model(
    "ModelTableInformationSelectInSingleTableSchema",
    __base__=ModelTableInformationSelectInSingleTableSchema,
)
ModelTableInformation_sub_stmt = (
    select(
        ModelTableInformation,
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelUser.ID == ModelTableInformation.IdManager, isouter=True)
    .where(ModelUser.IMark == 0)
    .subquery()
)
