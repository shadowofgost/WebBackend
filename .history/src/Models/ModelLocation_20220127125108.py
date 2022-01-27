"""
# @Time             : 2022-01-13 23:22:21
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelLocation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-27 11:06:27
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
from .PublicValuesAndSchemas import error_database_execution, error_schema_validation
from .ModelUser import ModelUser

ModelLocation_nullable_columns = []
ModelLocation_nullable_columns.extend(nullable)
ModelLocationExtension_nullable_columns = [
    "DateBegin",
    "DateEnd",
    "ModeRun",
    "ModeShangJi",
    "EnableDelayCharged",
    "DelayCharged",
    "EnableLimitYuE_SJ",
    "LimitYuE_SJ",
    "EnableLimitYuE_XJ",
    "LimitYuE_XJ",
    "EnableLimitTime_XJ",
    "LimitTime_XJ",
    "EnableWarnYuE",
    "EnableWarnTime",
    "WarnTime",
    "EnableMinCost",
    "MinCost",
    "Price",
    "PriceMinute",
    "GetEquName",
    "GetEquIp",
    "GetEquMac ",
]
ModelLocationExtension_nullable_columns.extend(nullable)


class ModelLocation(ModelPublic):
    __tablename__ = "t_cylocation"

    ID_Parent = Column(BigInteger, index=True, comment="上级位置ID", doc="这是上级位置ID，顶级位置值为0")
    Name = Column(Unicode(32), index=True, comment="位置名称", doc="这是位置名称，不能超过15字符")


class ModelLocationExtension(ModelPublic):
    __tablename__ = "t_cylocationex"

    ID_Location = Column(
        BigInteger, index=True, comment="位置的唯一标识", doc="关键字，每个位置的唯一标识，一旦添加不能更改"
    )
    Attr = Column(SmallInteger, index=True)
    DateBegin = Column(Integer, index=True)
    DateEnd = Column(Integer, index=True)
    ModeRun = Column(Integer)
    ModeShangJi = Column(Integer)
    EnableDelayCharged = Column(Integer)
    DelayCharged = Column(Integer)
    EnableLimitYuE_SJ = Column(Integer)
    LimitYuE_SJ = Column(Integer)
    EnableLimitYuE_XJ = Column(Integer)
    LimitYuE_XJ = Column(Integer)
    EnableLimitTime_XJ = Column(Integer)
    LimitTime_XJ = Column(Integer)
    EnableWarnYuE = Column(Integer)
    WarnYuE = Column(Integer)
    EnableWarnTime = Column(Integer)
    WarnTime = Column(Integer)
    EnableMinCost = Column(Integer)
    MinCost = Column(Integer)
    Price = Column(Integer)
    PriceMinute = Column(Integer)
    GetEquName = Column(Integer)
    GetEquIp = Column(Integer)
    GetEquMac = Column(Integer)


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
    .join(ModelUser, ModelUser.ID == ModelLocation.IdManager)
    .subquery()
)

ModelLocationExtensionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocationExtension, update_exclude
)


class ModelLocationExtensionUpdateMultipleGetSchema(BaseModel):
    data: List[ModelLocationExtensionUpdateSingleGetSchema]
    n: int


class ModelLocationExtensionUpdateSingleTableSchema(
    ModelLocationExtensionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelLocationExtensionUpdateMultipleTableSchema(BaseModel):
    data: List[ModelLocationExtensionUpdateSingleTableSchema]
    n: int


ModelLocationExtensionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelLocationExtension, insert_exclude, ModelLocationExtension_nullable_columns
)


class ModelLocationExtensionInsertMultipleGetSchema(BaseModel):
    data: List[ModelLocationExtensionInsertSingleGetSchema]
    n: int


class ModelLocationExtensionInsertSingleTableSchema(
    ModelLocationExtensionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelLocationExtensionInsertMultipleTableSchema(
    BaseModel
):
    data: List[ModelLocationExtensionInsertSingleTableSchema]
    n: int


ModelLocationExtensionSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelLocationExtension, select_out_exclude
)


class ModelLocationExtensionSelectOutSingleTableSchema(
    ModelLocationExtensionSelectOutSingleTableSchemaBase
):
    ID_Location_Name: Optional[str] = Field(
        default=None, title="地点名称", description="这是这节课程安排课对应的地点名称"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelLocationExtensionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelLocationExtension, select_in_exclude, []
)


ModelLocationExtension_sub_stmt = (
    select(
        ModelLocationExtension,
        ModelLocation.Name.label("ID_Location_Name"),
        ModelUser.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelUser.ID == ModelLocationExtension.IdManager)
    .join(ModelLocation, ModelLocation.ID == ModelLocationExtension.ID_Location)
    .subquery()
)
