"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-07 15:05:40
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ModelUserCrud.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 17:41:21
# @Software         : Vscode
"""
from sqlalchemy.orm import Session

from ..Models import (
    ORM,
    ModelUserInsertMultipleGetSchema,
    ModelUserInsertMultipleTableSchema,
    ModelUserInsertSingleTableSchema,
    ModelUserSelectInSingleTableSchema,
    ModelUserSelectOutSingleTableSchema,
    ModelUserUpdateMultipleGetSchema,
    ModelUserUpdateMultipleTableSchema,
    ModelUserUpdateSingleTableSchema,
    DeleteMultipleGetSchema,
    PublicValuesAndSchemas,
)
from .PublicService import service_update, service_insert, service_select

def model_user_crud_delete( schema: ModelUserUpdateMultipleGetSchema, session: Session, id):


def model_user_crud_update(
    schema: ModelUserUpdateMultipleGetSchema, session: Session, id
):
    model = "ModelUser"
    return service_update(session, id, model, schema)


def model_user_crud_insert(
    schema: ModelUserInsertMultipleGetSchema, session: Session, id
):
    model = "ModelUser"
    return service_insert(session, id, model, schema)


def model_user_service_select(
    session: Session, id_manager: int, model: str, service_type: int, schema=None
):
    """
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户]

    Returns
    -------
    dict[str,str]
        [description]
    """
    model_instance = ORM(model, session)
    if service_type == 0:
        return model_instance.condition_select()
    elif service_type == 1:
        select_in_schema = PublicValuesAndSchemas.model_dict[model][
            "select_single_schema"
        ]
        try:
            table_schema = select_in_schema(ID=schema.id)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.multiple_require_select(table_schema)
    elif service_type == 2:
        try:
            name = schema.Name
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.name_select(name)
    elif service_type == 3:
        select_in_schema = PublicValuesAndSchemas.model_dict[model][
            "select_single_schema"
        ]
        try:
            table_schema = select_in_schema(**schema.dict())
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.multiple_require_select(table_schema)
    elif service_type == 4:
        select_in_schema = PublicValuesAndSchemas.model_dict[model][
            "select_single_schema"
        ]
        try:
            table_schema = select_in_schema(ID=schema.Nouser)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.multiple_require_select(table_schema)
    else:
        pass


class UserSchema(ModelUserSelectOutSingleTableSchema):
    is_authenticated: bool = False

    class Config:
        orm_mode = True


def get_user(session: Session, id: int) -> UserSchema:
    model = "ModelUser"
    user = service_select(session, id, model, 1)
