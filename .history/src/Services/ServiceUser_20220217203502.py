"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:57
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceUser.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 20:31:40
# @Software         : Vscode
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .PublicService import service_select
from .SchemaUser import (
    ModelUserSelectInSingleTableSchema,
    ModelUserSelectOutSingleTableSchema
)
from pydantic import Field
UserNotFound = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="User With this username not found"
)
class SchemaUserPydantic(ModelUserSelectInSingleTableSchema):
    ID:int
    Attr:int
    NoUser:int
    Psw:str
    class Config:
        orm_mode = True

def model_user_crud_select(
    session: Session, id_manager: int, service_type: int, schema=None
):
    model = "ModelUser"
    return service_select(session, id_manager, model, service_type, schema)


def get_user_id(session: Session, id: int) -> SchemaUserPydantic:
    user_list = model_user_crud_select(session, id, 1)
    try:
        user = SchemaUserPydantic(**user_list[0])
        return user
    except Exception:
        raise UserNotFound


def get_user_nouser(
    session: Session, nouser: int
) -> SchemaUserPydantic:
    schema = ModelUserSelectInSingleTableSchema(NoUser=nouser)
    user_list = model_user_crud_select(session, 1, 4, schema)
    try:
        user = SchemaUserPydantic(**user_list[0])
        return user
    except Exception:
        raise UserNotFound
