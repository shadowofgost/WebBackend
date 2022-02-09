"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-07 15:05:40
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ModelUserCrud.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 18:13:33
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
)
from .PublicService import (
    service_update,
    service_insert,
    service_select,
    service_delete,
)
from fastapi import HTTPException, status

UserNotFound = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="User With this username not found"
)


def model_user_crud_delete(schema: DeleteMultipleGetSchema, session: Session, id):
    model = "ModelUser"
    return service_delete(session, id, model, schema)


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


def model_user_crud_select(
    session: Session, id_manager: int, service_type: int, schema=None
):
    model = "ModelUser"
    return service_select(session, id_manager, model, service_type, schema)


def get_user(session: Session, id_manager: int):
    user_list = model_user_crud_select(session, id_manager, 1)
    try:
        user = ModelUserSelectOutSingleTableSchema(**user_list[0])
        return user
    except Exception:
        raise UserNotFound
