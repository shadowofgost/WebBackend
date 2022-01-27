"""
# @Time             : 2022-01-13 23:23:40
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTypera.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-27 11:14:32
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

from .ModelUser import ModelUser

ModelTypera_nullable_columns = []
ModelTypera_nullable_columns.extend(nullable)


class ModelTypera(ModelPublic):
    __tablename__ = "t_cytypera"

    ID_Parent = Column(BigInteger, index=True, comment="上级类型的ID", doc="上级类型的ID，顶级类型值为0")
    Name = Column(Unicode(128), index=True, comment="类型名称", doc="这是类型名称，不能超过15字符")


ModelTyperaUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelTypera, update_exclude)


class ModelTyperaUpdateMultipleGetSchema(BaseModel):
    data: List[ModelTyperaUpdateSingleGetSchema]
    n: int


class ModelTyperaUpdateSingleTableSchema(ModelTyperaUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelTyperaUpdateMultipleTableSchema(BaseModel):
    data: List[ModelTyperaUpdateSingleTableSchema]
    n: int


ModelTyperaInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTypera, insert_exclude, ModelTypera_nullable_columns
)


class ModelTyperaInsertMultipleGetSchema(BaseModel):
    data: List[ModelTyperaInsertSingleGetSchema]
    n: int


class ModelTyperaInsertSingleTableSchema(ModelTyperaInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelTyperaInsertMultipleTableSchema(BaseModel):
    data: List[ModelTyperaInsertSingleTableSchema]
    n: int


ModelTyperaSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelTypera, select_out_exclude
)


class ModelTyperaSelectOutSingleTableSchema(ModelTyperaSelectOutSingleTableSchemaBase):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelTyperaSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTypera, select_in_exclude, []
)
ModelTypera_sub_stmt = (
    select(
        ModelTypera,
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelUser.ID == ModelUser.IdManager)
    .subquery()
)
