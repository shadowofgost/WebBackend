"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-27 14:16:12
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelUserExtension.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-27 14:24:21
# @Software         : Vscode
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
from sqlalchemy.orm import Session, sessionmaker, aliased
from .ModelUser import ModelUser
from .PublicModel import (
    ModelPublic,
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)

ModelUserExtension_nullable_columns = ["Photo_dataF"]
ModelUserExtension_nullable_columns.extend(nullable)


class ModelUserExtension(ModelPublic):
    __tablename__ = "t_cyuserex"
    NoUser = Column(
        Unicode(32), index=True, comment="账号（学工号）", doc="这是账号（学工号），不能超过15字符"
    )
    NoSfz = Column(BigInteger, index=True, comment="身份证号", doc="身份证号")
    FaceFearture = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo_dataF = Column(Unicode(2048), default="0")


ModelUserExtensionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, update_exclude
)


class ModelUserExtensionUpdateMultipleGetSchema(BaseModel):
    data: List[ModelUserExtensionUpdateSingleGetSchema]
    n: int


class ModelUserExtensionUpdateSingleTableSchema(
    ModelUserExtensionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelUserExtensionUpdateMultipleTableSchema(BaseModel):
    data: List[ModelUserExtensionUpdateSingleTableSchema]
    n: int


ModelUserExtensionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, insert_exclude, ModelUserExtension_nullable_columns
)


class ModelUserExtensionInsertMultipleGetSchema(BaseModel):
    data: List[ModelUserExtensionInsertSingleGetSchema]
    n: int


class ModelUserExtensionInsertSingleTableSchema(
    ModelUserExtensionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelUserExtensionInsertMultipleTableSchema(BaseModel):
    data: List[ModelUserExtensionInsertSingleTableSchema]
    n: int


ModelUserExtensionSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelUserExtension, select_out_exclude
)


class ModelUserExtensionSelectOutSingleTableSchema(
    ModelUserExtensionSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelUserExtension_sub_stmt = (
    select(
        ModelUserExtension,
        ModelUser.Name.label("ID_Manager_Name"),
    ).join(ModelUser, ModelUser.ID == ModelUserExtension.IdManager, isouter=True)
).subquery()

ModelUserExtensionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, select_in_exclude, []
)
