"""
# @Time             : 2022-01-13 23:23:28
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTableInformation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-30 12:30:02
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

ModelTableInformation_nullable_columns = []
ModelTableInformation_nullable_columns.extend(nullable)


class ModelTableInformation(ModelPublic):
    __tablename__ = "t_cytableinfo"

    Name = Column(Unicode(50), index=True)
    NameTable = Column(Unicode(50), index=True)


ModelTableInformationUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, update_exclude
)


class ModelTableInformationUpdateMultipleGetSchema(BaseModel):
    data: List[ModelTableInformationUpdateSingleGetSchema]
    n: int


class ModelTableInformationUpdateSingleTableSchema(
    ModelTableInformationUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelTableInformationUpdateMultipleTableSchema(BaseModel):
    data: List[ModelTableInformationUpdateSingleTableSchema]
    n: int


ModelTableInformationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, insert_exclude, ModelTableInformation_nullable_columns
)


class ModelTableInformationInsertMultipleGetSchema(BaseModel):
    data: List[ModelTableInformationInsertSingleGetSchema]
    n: int


class ModelTableInformationInsertSingleTableSchema(
    ModelTableInformationInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelTableInformationInsertMultipleTableSchema(BaseModel):
    data: List[ModelTableInformationInsertSingleTableSchema]
    n: int


ModelTableInformationSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelTableInformation, select_out_exclude
)


class ModelTableInformationSelectOutSingleTableSchema(
    ModelTableInformationSelectOutSingleTableSchemaBase
):
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelTableInformationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, select_in_exclude, []
)
ModelTableInformation_sub_stmt = (
    select(
        ModelTableInformation,
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(
        ModelUser,
        ModelUser.ID == ModelTableInformation.IdManager,
    isouter=True)
    .subquery()
)
