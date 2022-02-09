"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 16:09:31
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/Public.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-01 20:15:42
# @Software         : Vscode
"""
from ast import Raise
from distutils.log import error
from re import S
from unittest import result
from sqlalchemy import table
from sqlalchemy.orm import Session
from typing import Container, Optional, Type
from ..Models import (
    DeleteMultipleGetSchema,
    ORM,
    DeleteMultipleTableSchema,
    DeleteSingleTableSchema,
    model_dict,
)

error_service_validation = {"error": "在service层验证错误"}


def transform(id_manager: int, schema, multiple_schema, initial_schema):
    try:
        transform_list = [
            schema(IdManager=id_manager, **initial_schema.data[i].dict())
            for i in range(initial_schema.n)
        ]
    except Exception as e:
        Raise
    result_schema = multiple_schema(data=transform_list, n=initial_schema.n)
    return result_schema


def delete(
    session: Session, id_manager: int, model: str, schema: DeleteMultipleGetSchema
) -> dict[str, str]:
    model_instance = ORM(model, session)
    if schema.n == 1:
        try:
            table_schema = DeleteSingleTableSchema(
                IdManager=id_manager, id=schema.data[0].id
            )
        except Exception as e:
            return error_service_validation
        result = model_instance.delete(table_schema)
    else:
        table_schema = multiple_transform(
            id_manager, DeleteSingleTableSchema, DeleteMultipleTableSchema, schema
        )
        result = model_instance.delete(table_schema,multiple=True)
    return result


def update(session: Session, id_manager: int, model: str, schema) -> dict[str, str]:
    model_instance = ORM(model, session)
    single_schema=model_dict[model]["update_single_schema"]
    multiple_schema = model_dict[model]["update_multiple_schema"]
    if schema.n==1:
        try:
            table_schema= single_schema(IdManager=id_manager,**schema.data[0].dict())
        except Exception as e:
            return error_service_validation
    else:
