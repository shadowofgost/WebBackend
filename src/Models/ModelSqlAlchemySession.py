"""
# @Time             : 2022-01-14 01:17:55
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelSqlAlchemySession.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-27 15:36:45
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
from sqlalchemy.dialects.mssql import DATETIME2
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


ModelSqlAlchemySession_nullable_columns = []
ModelSqlAlchemySession_nullable_columns.extend(nullable)


class ModelSqlAlchemySession(ModelPublic):
    __tablename__ = "sqlalchemy_session_table"
    session_key = Column(Unicode(40), primary_key=True, index=True)
    session_data = Column(Unicode, nullable=False, index=True)
    expire_date = Column(DATETIME2, nullable=False, index=True)


ModelSqlAlchemySessionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, update_exclude
)


class ModelSqlAlchemySessionUpdateMultipleGetSchema(BaseModel):
    data: List[ModelSqlAlchemySessionUpdateSingleGetSchema]
    n: int


class ModelSqlAlchemySessionUpdateSingleTableSchema(
    ModelSqlAlchemySessionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelSqlAlchemySessionUpdateMultipleTableSchema(BaseModel):
    data: List[ModelSqlAlchemySessionUpdateSingleTableSchema]
    n: int


ModelSqlAlchemySessionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, insert_exclude, ModelSqlAlchemySession_nullable_columns
)


class ModelSqlAlchemySessionInsertMultipleGetSchema(BaseModel):
    data: List[ModelSqlAlchemySessionInsertSingleGetSchema]
    n: int


class ModelSqlAlchemySessionInsertSingleTableSchema(
    ModelSqlAlchemySessionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelSqlAlchemySessionInsertMultipleTableSchema(BaseModel):
    data: List[ModelSqlAlchemySessionInsertSingleTableSchema]
    n: int


ModelSqlAlchemySessionSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, select_out_exclude
)
ModelSqlAlchemySessionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, select_in_exclude, []
)


ModelSqlAlchemySession_sub_stmt=select(ModelSqlAlchemySession)
