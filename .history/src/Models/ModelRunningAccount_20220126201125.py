"""
# @Time             : 2022-01-13 23:23:15
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelRunningAccount.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 20:01:24
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

ModelRunningAccount_nullable_columns = ["Money", "Param1"]
ModelRunningAccount_nullable_columns.extend(nullable)


class ModelRunningAccount(ModelPublic):
    __tablename__ = "t_cyrunningaccount"

    ID_User = Column(BigInteger, index=True, comment="用户ID", doc="用户ID")
    Time = Column(
        BigInteger, index=True, comment="生成记录的时间", doc="生成记录（发生费用）的时间，从2000-1-1日计秒"
    )
    Type_field = Column(
        SmallInteger,
        index=True,
        name="Type",
        comment="记录的类型",
        doc="这是记录的类型，其值定义如下：参见T_CyTypeRA表每一个功能的id，例如：考勤：4097",
    )
    Money = Column(Integer, comment="发生的费用", doc="发生的费用，单位为分")
    Param1 = Column(
        BigInteger,
        index=True,
        comment="考勤机编号",
        doc="这是考勤机编号，例如：收费管理员的ID：1910007,此时Type=0x101，上机机位编号：556678 此时Type=0x201，门禁考勤机编号：11111 此时Type=0x1001",
    )
    Param2 = Column(
        BigInteger,
        index=True,
        comment="安排编号",
        doc="这是安排编号，例如：讲座、课程的编号：也就是对应Plan的id此时Type=4097；取消交易记录的ID：Type=0x106，",
    )


ModelRunningAccountUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelRunningAccount, update_exclude
)


class ModelRunningAccountUpdateMultipleGetSchema(
    ModelRunningAccountUpdateSingleGetSchema
):
    data: List[ModelRunningAccountUpdateSingleGetSchema]
    n: int


class ModelRunningAccountUpdateSingleTableSchema(
    ModelRunningAccountUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelRunningAccountUpdateMultipleTableSchema(
    ModelRunningAccountUpdateSingleTableSchema
):
    data: List[ModelRunningAccountUpdateSingleTableSchema]
    n: int


ModelRunningAccountInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelRunningAccount, insert_exclude, ModelRunningAccount_nullable_columns
)


class ModelRunningAccountInsertMultipleGetSchema(
    ModelRunningAccountInsertSingleGetSchema
):
    data: List[ModelRunningAccountInsertSingleGetSchema]
    n: int


class ModelRunningAccountInsertSingleTableSchema(
    ModelRunningAccountInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelRunningAccountInsertMultipleTableSchema(
    ModelRunningAccountInsertSingleTableSchema
):
    data: List[ModelRunningAccountInsertSingleTableSchema]
    n: int


ModelRunningAccountSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelRunningAccount, select_out_exclude
)
ModelRunningAccountSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelRunningAccount, select_in_exclude, []
)
