"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:57
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceUser.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 19:24:55
# @Software         : Vscode
"""
from sqlalchemy.orm import Session
from .PublicService import service_select
from .SchemaUser import (
    ModelUserSelectInSingleTableSchema,
    ModelUserSelectOutSingleTableSchema,
)
from Components.Exceptions import UserNotFound
from typing import Optional
##TODO:WARNING:后端文件的进行的权限控制系统
class SchemaUserPydantic(ModelUserSelectOutSingleTableSchema):
    ID: int
    Attr: int  ##这个attr是对数据库attr的重新设定，1是管理员，2是教师，3是学生,4 是其他人
    NoUser: str
    Name: str
    Psw: str

    class Config:
        orm_mode = True


def model_user_crud_select(
    session: Session, id_manager: int, service_type: int, schema=None
):
    model = "ModelUser"
    return service_select(session, id_manager, model, service_type, schema)


def modify_user_attr(user: SchemaUserPydantic) -> SchemaUserPydantic:
    if user.NoUser.isdigit() == True:
        user.Attr = 3
    else:
        if user.Attr == 1 or 2:
            user.Attr = 1
        else:
            user.Attr = 2
    return user


def get_user_id(session: Session, id: int) -> SchemaUserPydantic:
    user_list = model_user_crud_select(session, id, 1)
    try:
        user = SchemaUserPydantic(**user_list[0])
        return modify_user_attr(user)
    except Exception:
        raise UserNotFound


def get_user_nouser(session: Session, nouser: str) -> SchemaUserPydantic:
    schema = ModelUserSelectInSingleTableSchema(NoUser=nouser)
    user_list = model_user_crud_select(session, 1, 4, schema)
    print(user_list)
    try:
        user = SchemaUserPydantic(**user_list[0])
        return modify_user_attr(user)
    except Exception:
        raise UserNotFound
