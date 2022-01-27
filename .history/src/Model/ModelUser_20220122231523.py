"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/ModelUser.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-22 23:05:23
# @LastAuthor       : Albert Wang
"""
from operator import index
from pydantic import EmailError
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
from ModelPublic import ModelPublic,sqlalchemy_to_pydantic



class ModelUser(ModelPublic):
    __tablename__ = "t_cyuser"

    Deptid = Column(BigInteger, index=True, comment="用户所在部门的ID", doc="用户所在部门的ID")
    NoCard = Column(Unicode(32), index=True, comment="卡号", doc="卡号，不能超过15字符")
    NoUser = Column(
        Unicode(32), index=True, comment="账号（学工号）", doc="这是账号（学工号），不能超过15字符"
    )
    Name = Column(Unicode(32), index=True, comment="用户名", doc="这是用户名，不能超过15字符")
    Psw = Column(Unicode(32), index=True, comment="密码", doc="密码，不能超过15字符")
    Sex = Column(SmallInteger, index=True, comment="用户性别", doc="这是用户性别，0 女，1 男")
    Attr = Column(
        SmallInteger,
        index=True,
        comment="用户管理权限",
        doc="这是用户属性，表示用户的管理权限，0 普通用户，1 管理员，2 超级管理员（可对管理员进行控制）",
    )
    AttrJf = Column(
        SmallInteger,
        index=True,
        comment="机房管理权限",
        doc="这是用户属性，表示机房管理权限，0 普通用户，1 管理员，2 超级管理员（可对管理员进行控制）",
    )
    Email = Column(Unicode(254), index=True)
    Phone = Column(Integer, index=True)
    Yue = Column(Integer, comment="用户余额1", doc="这是用户余额1，单位为分（默认）")
    Yue2 = Column(Integer, comment="用户余额2", doc="这是用户余额2，单位为分（扩展于特殊需求）")
    LocalID = Column(Unicode(1024), comment="管理房间的ID列表", doc="管理房间的ID列表")


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


PydanticUserex = sqlalchemy_to_pydantic(ModelUserExtension)
