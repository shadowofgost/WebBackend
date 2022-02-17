"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:57
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceUser.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-15 17:07:09
# @Software         : Vscode
"""
from sqlalchemy.orm import Session

from .ORM import ORM
from .SchemaUser import (
        ModelUserInsertMultipleGetSchema,
    ModelUserInsertMultipleTableSchema,
    ModelUserInsertSingleTableSchema,
    ModelUserSelectInSingleTableSchema,
    ModelUserSelectOutSingleTableSchema,
    ModelUserUpdateMultipleGetSchema,
    ModelUserUpdateMultipleTableSchema,
    ModelUserUpdateSingleTableSchema,
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


def model_user_crud_select(
    session: Session, id_manager: int, service_type: int, schema=None
):
    model = "ModelUser"
    return service_select(session, id_manager, model, service_type, schema)


def get_user_id(session: Session, id: int) -> ModelUserSelectOutSingleTableSchema:
    user_list = model_user_crud_select(session, id, 1)
    try:
        user = ModelUserSelectOutSingleTableSchema(**user_list[0])
        return user
    except Exception:
        raise UserNotFound


def get_user_nouser(
    session: Session, nouser: int
) -> ModelUserSelectOutSingleTableSchema:
    schema = ModelUserSelectInSingleTableSchema(NoUser=nouser)
    user_list = model_user_crud_select(session, 1, 4, schema)
    try:
        user = ModelUserSelectOutSingleTableSchema(**user_list[0])
        return user
    except Exception:
        raise UserNotFound
