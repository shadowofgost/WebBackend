"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelUser.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 20:01:48
# @LastAuthor       : Albert Wang
"""
from typing import Container, List, Optional

from pydantic import BaseModel, Field
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    select,
)
from sqlalchemy.orm import Session, sessionmaker

from .ModelPublic import (
    ModelPublic,
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)
from .PublicValues import error_database_execution, error_schema_validation

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
    NoSfz = Column(BigInteger, index=True, comment="身份证号", doc="身份证号")
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
    Power = Column(
        SmallInteger,
        index=True,
        comment="未知",
        doc="未知，可选值为0，2，85，127",
    )
    PowerJf = Column(
        SmallInteger,
        index=True,
        comment="未知",
        doc="未知，可选值为0，8，10",
    )
    Email = Column(Unicode(254), index=True)
    Phone = Column(Integer, index=True)
    Yue = Column(Integer, comment="用户余额1", doc="这是用户余额1，单位为分（默认）")
    Yue2 = Column(Integer, comment="用户余额2", doc="这是用户余额2，单位为分（扩展于特殊需求）")
    LocalID = Column(Unicode(1024), comment="管理房间的ID列表", doc="管理房间的ID列表")


class ModelUserExtension(ModelPublic):
    __tablename__ = "t_cyuserex"
    NoUser = Column(
        Unicode(32), index=True, comment="账号（学工号）", doc="这是账号（学工号），不能超过15字符"
    )
    NoSfz = Column(BigInteger, index=True, comment="身份证号", doc="身份证号")
    FaceFearture=Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo_dataF = Column(Unicode(2048), default="0")


ModelUserUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelUser, update_exclude)


class ModelUserUpdateMultipleGetSchema(ModelUserUpdateSingleGetSchema):
    data: List[ModelUserUpdateSingleGetSchema]
    n: int


class ModelUserUpdateSingleTableSchema(ModelUserUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelUserUpdateMultipleTableSchema(ModelUserUpdateSingleTableSchema):
    data: List[ModelUserUpdateSingleTableSchema]
    n: int


ModelUserInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUser, insert_exclude, ModelUser_nullable_columns
)


class ModelUserInsertMultipleGetSchema(ModelUserInsertSingleGetSchema):
    data: List[ModelUserInsertSingleGetSchema]
    n: int


class ModelUserInsertSingleTableSchema(ModelUserInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelUserInsertMultipleTableSchema(ModelUserInsertSingleTableSchema):
    data: List[ModelUserInsertSingleTableSchema]
    n: int


ModelUserSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUser, select_out_exclude
)
ModelUserSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUser, select_in_exclude, []
)
ModelUserExtensionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, update_exclude
)


class ModelUserExtensionUpdateMultipleGetSchema(
    ModelUserExtensionUpdateSingleGetSchema
):
    data: List[ModelUserExtensionUpdateSingleGetSchema]
    n: int


class ModelUserExtensionUpdateSingleTableSchema(
    ModelUserExtensionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelUserExtensionUpdateMultipleTableSchema(
    ModelUserExtensionUpdateSingleTableSchema
):
    data: List[ModelUserExtensionUpdateSingleTableSchema]
    n: int


ModelUserExtensionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, insert_exclude, ModelUserExtension_nullable_columns
)


class ModelUserExtensionInsertMultipleGetSchema(
    ModelUserExtensionInsertSingleGetSchema
):
    data: List[ModelUserExtensionInsertSingleGetSchema]
    n: int


class ModelUserExtensionInsertSingleTableSchema(
    ModelUserExtensionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelUserExtensionInsertMultipleTableSchema(
    ModelUserExtensionInsertSingleTableSchema
):
    data: List[ModelUserExtensionInsertSingleTableSchema]
    n: int


ModelUserExtensionSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, select_out_exclude
)
ModelUserExtensionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, select_in_exclude, []
)
