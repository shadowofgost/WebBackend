"""
# @Time             : 2022-01-13 23:22:21
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelLocation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-30 12:25:57
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

ModelLocation_nullable_columns = []
ModelLocation_nullable_columns.extend(nullable)


class ModelLocation(ModelPublic):
    __tablename__ = "t_cylocation"

    ID_Parent = Column(BigInteger, index=True, comment="上级位置ID", doc="这是上级位置ID，顶级位置值为0")
    Name = Column(Unicode(32), index=True, comment="位置名称", doc="这是位置名称，不能超过15字符")





ModelLocationUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocation, update_exclude
)


class ModelLocationUpdateMultipleGetSchema(BaseModel):
    data: List[ModelLocationUpdateSingleGetSchema]
    n: int


class ModelLocationUpdateSingleTableSchema(ModelLocationUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelLocationUpdateMultipleTableSchema(BaseModel):
    data: List[ModelLocationUpdateSingleTableSchema]
    n: int


ModelLocationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocation, insert_exclude, ModelLocation_nullable_columns
)


class ModelLocationInsertMultipleGetSchema(BaseModel):
    data: List[ModelLocationInsertSingleGetSchema]
    n: int


class ModelLocationInsertSingleTableSchema(ModelLocationInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelLocationInsertMultipleTableSchema(BaseModel):
    data: List[ModelLocationInsertSingleTableSchema]
    n: int


ModelLocationSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelLocation, select_out_exclude
)
ModelLocationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelLocation, select_in_exclude, []
)


class ModelLocationSelectOutSingleTableSchema(
    ModelLocationSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelLocation_sub_stmt = (
    select(ModelLocation, ModelUser.Name.label("ID_Manager_Name"))
    .join(ModelUser, ModelUser.ID == ModelLocation.IdManager,isouter=True)
    .subquery()
)