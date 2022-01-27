"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelUser.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 16:26:11
# @LastAuthor       : Albert Wang
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
)

ModelUser_nullable_columns = ["Yue", "Yue2", "Email", "Phone", "LocalID"]
ModelUser_nullable_columns.extend(nullable)
ModelUserExtension_nullable_columns = ["Photo_dataF"]
ModelUserExtension_nullable_columns.extend(nullable)


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
