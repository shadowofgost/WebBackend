"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-25 16:19:06
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelUserGroup.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-25 16:39:15
# @Software         : Vscode
"""
from sqlalchemy import (
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    BigInteger,
    table,
)
from .ModelPublic import (
    ModelPublic,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
    format_current_time,
)


class ModelUserExtension(ModelPublic):
    __tablename__ = "t_cyuserex"

    Photo = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo_dataF = Column(Unicode(2048), default="0")


class ModelAuthUserGroups(ModelPublic):
    __tablename__ = "auth_user_groups"

    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)


class ModelAuthUserUserPermissions(ModelPublic):
    __tablename__ = "auth_user_user_permissions"

    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class ModelAuthGroup(ModelPublic):
    __tablename__ = "auth_group"

    name = Column(Unicode(150), nullable=False)


class ModelAuthGroupPermissions(ModelPublic):
    __tablename__ = "auth_group_permissions"

    group_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class ModelAuthPermission(ModelPublic):
    __tablename__ = "auth_permission"

    name = Column(Unicode(255), nullable=False)
    content_type_id = Column(Integer, nullable=False)
    codename = Column(Unicode(100), nullable=False)
