"""
# @Time             : 2022-01-13 23:22:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelMmx.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 20:01:16
# @LastAuthor       : Albert Wang
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

from .ModelPublic import (
    ModelPublic,
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)
from .PublicValues import error_database_execution, error_schema_validation

ModelMmx_nullable_columns = []
ModelMmx_nullable_columns.extend(nullable)
ModelMmxData_nullable_columns = ["Data"]
ModelMmxData_nullable_columns.extend(nullable)


class ModelMmx(ModelPublic):
    __tablename__ = "t_cymmx"

    ID_Data = Column(BigInteger, index=True, comment="媒体内容的ID", doc="媒体内容的ID")
    ID_Type = Column(SmallInteger, index=True, comment="媒体类型", doc="媒体类型，1为PPT类型")


class ModelMmxData(ModelPublic):
    __tablename__ = "t_cymmxdata"

    Data = Column(Unicode(1024), comment="媒体的内容", doc="媒体的内容")


ModelMmxUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmx, update_exclude)


class ModelMmxUpdateMultipleGetSchema(ModelMmxUpdateSingleGetSchema):
    data: List[ModelMmxUpdateSingleGetSchema]
    n: int


class ModelMmxUpdateSingleTableSchema(ModelMmxUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelMmxUpdateMultipleTableSchema(ModelMmxUpdateSingleTableSchema):
    data: List[ModelMmxUpdateSingleTableSchema]
    n: int


ModelMmxInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelMmx, insert_exclude, ModelMmx_nullable_columns
)


class ModelMmxInsertMultipleGetSchema(ModelMmxInsertSingleGetSchema):
    data: List[ModelMmxInsertSingleGetSchema]
    n: int


class ModelMmxInsertSingleTableSchema(ModelMmxInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxInsertMultipleTableSchema(ModelMmxInsertSingleTableSchema):
    data: List[ModelMmxInsertSingleTableSchema]
    n: int


ModelMmxSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmx, select_out_exclude
)
ModelMmxSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmx, select_in_exclude, []
)
ModelMmxDataUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmxData, update_exclude)


class ModelMmxDataUpdateMultipleGetSchema(ModelMmxDataUpdateSingleGetSchema):
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


class ModelMmxDataInsertMultipleGetSchema(ModelMmxDataInsertSingleGetSchema):
    data: List[ModelMmxDataInsertSingleGetSchema]
    n: int


class ModelMmxDataInsertSingleTableSchema(ModelMmxDataInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxDataInsertMultipleTableSchema(ModelMmxDataInsertSingleTableSchema):
    data: List[ModelMmxDataInsertSingleTableSchema]
    n: int


ModelMmxDataSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmxData, select_out_exclude
)
ModelMmxDataSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmxData, select_in_exclude, []
)
