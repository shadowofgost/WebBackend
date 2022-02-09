"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-27 14:15:56
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelMmxData.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-30 12:29:13
# @Software         : Vscode
"""
from typing import Container, List, Optional

from pydantic import BaseModel, Field
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    select,
)
from sqlalchemy.orm import Session, sessionmaker

from .PublicModel import (
    ModelPublic,
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

from .ModelUser import ModelUser

ModelMmxData_nullable_columns = ["Data"]
ModelMmxData_nullable_columns.extend(nullable)


class ModelMmxData(ModelPublic):
    __tablename__ = "t_cymmxdata"

    Data = Column(Unicode(1024), comment="媒体的内容", doc="媒体的内容")


ModelMmxDataUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmxData, update_exclude)


class ModelMmxDataUpdateMultipleGetSchema(BaseModel):
    data: List[ModelMmxDataUpdateSingleGetSchema]
    n: int


class ModelMmxDataUpdateSingleTableSchema(ModelMmxDataUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelMmxDataUpdateMultipleTableSchema(ModelMmxDataUpdateSingleTableSchema):
    data: List[ModelMmxDataUpdateSingleTableSchema]
    n: int


ModelMmxDataInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelMmxData, insert_exclude, ModelMmxData_nullable_columns
)


class ModelMmxDataInsertMultipleGetSchema(BaseModel):
    data: List[ModelMmxDataInsertSingleGetSchema]
    n: int


class ModelMmxDataInsertSingleTableSchema(ModelMmxDataInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxDataInsertMultipleTableSchema(BaseModel):
    data: List[ModelMmxDataInsertSingleTableSchema]
    n: int


ModelMmxDataSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelMmxData, select_out_exclude
)


class ModelMmxDataSelectOutSingleTableSchema(
    ModelMmxDataSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelMmxDataSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmxData, select_in_exclude, []
)

ModelMmxData_sub_stmt = (
    select(
        ModelMmxData,
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelUser.ID == ModelMmxData.IdManager,isouter=True)
    .subquery()
)
