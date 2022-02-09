"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 16:09:31
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/PublicService.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-02 17:48:30
# @Software         : Vscode
"""
from ast import Raise
from statistics import mode
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
error_service_null={"error":"所查询的service并不存在"}

def transform(id_manager: int, single_schema, multiple_schema, initial_schema):
    if initial_schema.n == 1:
        try:
            result_schema = single_schema(
                IdManager=id_manager, **initial_schema.data[0].dict()
            )
        except Exception as e:
            raise Exception(error_service_validation)
    else:
        try:
            transform_list = [
                single_schema(IdManager=id_manager, **initial_schema.data[i].dict())
                for i in range(initial_schema.n)
            ]
        except Exception as e:
            raise Exception(error_service_validation)
        try:
            result_schema = multiple_schema(data=transform_list, n=initial_schema.n)
        except Exception as e:
            raise Exception(error_service_validation)
    return result_schema


def service_delete(
    session: Session, id_manager: int, model: str, schema: DeleteMultipleGetSchema
) -> dict[str, str]:
    model_instance = ORM(model, session)
    try:
        table_schema = transform(
        id_manager, DeleteSingleTableSchema, DeleteMultipleTableSchema, schema
    )
    except Exception as e:
        raise Exception(error_service_validation)
    if schema.n == 1:
        result = model_instance.delete(table_schema)
    else:
        result = model_instance.delete(table_schema, multiple=True)
    return result


def service_update(session: Session, id_manager: int, model: str, schema) -> dict[str, str]:
    model_instance = ORM(model, session)
    single_schema = model_dict[model]["update_single_schema"]
    multiple_schema = model_dict[model]["update_multiple_schema"]
    try:
        table_schema = transform(id_manager, single_schema, multiple_schema, schema)
    except Exception as e:
        raise Exception(error_service_validation)
    if schema.n == 1:
        result = model_instance.update(table_schema)
    else:
        result = model_instance.update(table_schema, multiple=True)
    return result


def service_insert(session: Session, id_manager: int, model: str, schema) -> dict[str, str]:
    model_instance = ORM(model, session)
    single_schema = model_dict[model]["insert_single_schema"]
    multiple_schema = model_dict[model]["insert_multiple_schema"]
    try:
        table_schema = transform(id_manager, single_schema, multiple_schema, schema)
    except Exception as e:
        raise Exception(error_service_validation)
    if schema.n == 1:
        result = model_instance.insert(table_schema)
    else:
        result = model_instance.insert(table_schema, multiple=True)
    return result


def service_select(
    session: Session, id_manager: int, model: str, service_type: int, schema=None
):
    """
    select [筛选函数的服务提供]

    [查询的服务提供]

    Parameters
    ----------
    session : Session
        [description]
    id_manager : int
        [description]
    model : str
        [description]
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户]
    schema : [type], optional
        [description], by default None
    name : [type], optional
        [description], by default None

    Returns
    -------
    dict[str,str]
        [description]
    """
    model_instance = ORM(model, session)
    if service_type == 0:
        return model_instance.condition_select()
    elif service_type == 1:
        select_in_schema = model_dict[model]["select_single_schema"]
        try:
            table_schema = select_in_schema(ID=schema.ID)
        except Exception as e:
            return error_service_validation
        return model_instance.multiple_require_select(table_schema)
    elif service_type == 2:
        try:
            name = schema.Name
        except Exception as e:
            return error_service_validation
        return model_instance.name_select(name)
    elif service_type == 3:
        select_in_schema = model_dict[model]["select_single_schema"]
        try:
            table_schema = select_in_schema(**schema.dict())
        except Exception as e:
            return error_service_validation
        return model_instance.multiple_require_select(table_schema)
    elif service_type == 4:
        select_in_schema = model_dict[model]["select_single_schema"]
        try:
            table_schema = select_in_schema(ID=schema.Nouser)
        except Exception as e:
            return error_service_validation
        return model_instance.multiple_require_select(table_schema)
    else:
        pass
