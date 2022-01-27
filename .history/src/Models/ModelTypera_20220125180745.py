"""
# @Time             : 2022-01-13 23:23:40
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTypera.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 17:57:44
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import (
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    BigInteger,
    select,
)
from sqlalchemy.orm import Session, sessionmaker
from .PublicValues import error_database_execution, error_schema_validation
from pydantic import BaseModel, Field
from typing import Container, List, Optional
from .ModelPublic import (
    ModelPublic,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
    format_current_time,
)

ModelTypera_nullable_columns = []
ModelTypera_nullable_columns.extend(nullable)


class ModelTypera(ModelPublic):
    __tablename__ = "t_cytypera"

    ID_Parent = Column(BigInteger, index=True, comment="上级类型的ID", doc="上级类型的ID，顶级类型值为0")
    Name = Column(Unicode(128), index=True, comment="类型名称", doc="这是类型名称，不能超过15字符")


ModelTyperaUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelTypera, update_exclude)


class ModelTyperaUpdateMultipleGetSchema(ModelTyperaUpdateSingleGetSchema):
    data: List[ModelTyperaUpdateSingleGetSchema]
    n: int


class ModelTyperaUpdateSingleTableSchema(ModelTyperaUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelTyperaUpdateMultipleTableSchema(ModelTyperaUpdateSingleTableSchema):
    data: List[ModelTyperaUpdateSingleTableSchema]
    n: int


ModelTyperaInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTypera, insert_exclude, ModelTypera_nullable_columns
)


class ModelTyperaInsertMultipleGetSchema(ModelTyperaInsertSingleGetSchema):
    data: List[ModelTyperaInsertSingleGetSchema]
    n: int


class ModelTyperaInsertSingleTableSchema(ModelTyperaInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelTyperaInsertMultipleTableSchema(ModelTyperaInsertSingleTableSchema):
    data: List[ModelTyperaInsertSingleTableSchema]
    n: int


ModelTyperaSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTypera, select_out_exclude
)
ModelTyperaSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTypera, select_in_exclude, []
)
