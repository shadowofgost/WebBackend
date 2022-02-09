"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 16:09:31
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/Public.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-01 20:37:46
# @Software         : Vscode
"""
from ast import Raise
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


def transform(id_manager: int, single_schema, multiple_schema, initial_schema):
    if initial_schema.n == 1:
        try:
            result_schema = single_schema(
                IdManager=id_manager, **initial_schema.data[0].dict()
            )
        except Exception as e:
            Raise
    else:
        try:
            transform_list = [
                single_schema(IdManager=id_manager, **initial_schema.data[i].dict())
                for i in range(initial_schema.n)
            ]
        except Exception as e:
            Raise
        try:
            result_schema = multiple_schema(data=transform_list, n=initial_schema.n)
        except Exception as e:
            Raise
    return result_schema


def delete(
    session: Session, id_manager: int, model: str, schema: DeleteMultipleGetSchema
) -> dict[str, str]:
    model_instance = ORM(model, session)
    table_schema = transform(
        id_manager, DeleteSingleTableSchema, DeleteMultipleTableSchema, schema
    )
    if schema.n == 1:
        result = model_instance.delete(table_schema)
    else:
        result = model_instance.delete(table_schema, multiple=True)
    return result


def update(session: Session, id_manager: int, model: str, schema) -> dict[str, str]:
    model_instance = ORM(model, session)
    single_schema = model_dict[model]["update_single_schema"]
    multiple_schema = model_dict[model]["update_multiple_schema"]
    table_schema = transform(id_manager, single_schema, multiple_schema, schema)
    if schema.n == 1:
        result = model_instance.update(table_schema)
    else:
        result = model_instance.update(table_schema, multiple=True)
    return result


def insert(session: Session, id_manager: int, model: str, schema) -> dict[str, str]:
    model_instance = ORM(model, session)
    single_schema = model_dict[model]["insert_single_schema"]
    multiple_schema = model_dict[model]["insert_multiple_schema"]
    table_schema = transform(id_manager, single_schema, multiple_schema, schema)
    if schema.n == 1:
        result = model_instance.insert(table_schema)
    else:
        result = model_instance.insert(table_schema, multiple=True)
    return result


def select(session: Session,id_manager:int,model:str,schema)->dict[str,str]:
    pass
