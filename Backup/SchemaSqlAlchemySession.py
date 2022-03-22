# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:58:17
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaSqlAlchemySession.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 14:26:16
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelSqlAlchemySession
from pydantic import BaseModel, create_model
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

ModelSqlAlchemySession_nullable_columns = []
ModelSqlAlchemySession_nullable_columns.extend(nullable)

ModelSqlAlchemySessionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, update_exclude
)
ModelSqlAlchemySessionUpdateSingleGetSchema = create_model(
    "ModelSqlAlchemySessionUpdateSingleGetSchema",
    __base__=ModelSqlAlchemySessionUpdateSingleGetSchema,
)


class ModelSqlAlchemySessionUpdateMultipleGetSchema(BaseModel):
    data: List[ModelSqlAlchemySessionUpdateSingleGetSchema]
    n: int


class ModelSqlAlchemySessionUpdateSingleTableSchema(
    ModelSqlAlchemySessionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelSqlAlchemySessionUpdateMultipleTableSchema(BaseModel):
    data: List[ModelSqlAlchemySessionUpdateSingleTableSchema]
    n: int


ModelSqlAlchemySessionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, insert_exclude, ModelSqlAlchemySession_nullable_columns
)
ModelSqlAlchemySessionInsertSingleGetSchema = create_model(
    "ModelSqlAlchemySessionInsertSingleGetSchema",
    __base__=ModelSqlAlchemySessionInsertSingleGetSchema,
)


class ModelSqlAlchemySessionInsertMultipleGetSchema(BaseModel):
    data: List[ModelSqlAlchemySessionInsertSingleGetSchema]
    n: int


class ModelSqlAlchemySessionInsertSingleTableSchema(
    ModelSqlAlchemySessionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int=0


class ModelSqlAlchemySessionInsertMultipleTableSchema(BaseModel):
    data: List[ModelSqlAlchemySessionInsertSingleTableSchema]
    n: int


ModelSqlAlchemySessionSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, select_out_exclude
)
ModelSqlAlchemySessionSelectOutSingleTableSchema = create_model(
    "ModelSqlAlchemySessionSelectOutSingleTableSchema",
    __base__=ModelSqlAlchemySessionSelectOutSingleTableSchema,
)
ModelSqlAlchemySessionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelSqlAlchemySession, select_in_exclude, []
)
ModelSqlAlchemySessionSelectInSingleTableSchema = create_model(
    "ModelSqlAlchemySessionSelectInSingleTableSchema",
    __base__=ModelSqlAlchemySessionSelectInSingleTableSchema,
)

ModelSqlAlchemySession_sub_stmt = select(ModelSqlAlchemySession)
