"""
# @Time             : 2022-01-13 23:23:15
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelRunningAccount.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-11 18:19:53
# @LastAuthor       : Albert Wang
"""
from typing import Container, List, Optional

from pydantic import BaseModel, Field, create_model
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

ModelRunningAccount_nullable_columns = ["Money", "Param1"]
ModelRunningAccount_nullable_columns.extend(nullable)


class ModelRunningAccount(ModelPublic):
    __tablename__ = "t_cyrunningaccount"

    ID_User = Column(BigInteger, index=True, comment="这是外键用户ID", doc="这是外键，链接User的用户ID")
    Time = Column(
        BigInteger, index=True, comment="生成记录的时间", doc="生成记录（发生费用）的时间，从2000-1-1日计秒"
    )
    Type_field = Column(
        SmallInteger,
        index=True,
        name="Type",
        comment="这是外键，记录的类型",
        doc="这是记录的类型，其值定义如下：参见T_CyTypeRA表每一个功能的id，例如：考勤：4097，这是T_CyTypeRA表的id和外键",
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
        comment="这是外键安排编号",
        doc="这是外键，安排编号，例如：讲座、课程的编号：也就是对应Plan的id此时Type=4097；取消交易记录的ID：Type=0x106，这是连接Plan表的id",
    )


ModelRunningAccountUpdateSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelRunningAccount, update_exclude
)
ModelRunningAccountUpdateSingleGetSchemaBase = create_model("ModelRunningAccountUpdateSingleGetSchemaBase",__base__=ModelRunningAccountUpdateSingleGetSchemaBase)

class ModelRunningAccountUpdateSingleGetSchema(
    ModelRunningAccountUpdateSingleGetSchemaBase
):
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )

    class Config:
        orm_mode = True


class ModelRunningAccountUpdateMultipleGetSchema(BaseModel):
    data: List[ModelRunningAccountUpdateSingleGetSchema]
    n: int


class ModelRunningAccountUpdateSingleTableSchema(
    ModelRunningAccountUpdateSingleGetSchemaBase
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelRunningAccountUpdateMultipleTableSchema(BaseModel):
    data: List[ModelRunningAccountUpdateSingleTableSchema]
    n: int


ModelRunningAccountInsertSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelRunningAccount, insert_exclude, ModelRunningAccount_nullable_columns
)
ModelRunningAccountInsertSingleGetSchemaBase= create_model("ModelRunningAccountInsertSingleGetSchemaBase",__base__=ModelRunningAccountInsertSingleGetSchemaBase)

class ModelRunningAccountInsertSingleGetSchema(
    ModelRunningAccountInsertSingleGetSchemaBase
):
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )

    class Config:
        orm_mode = True


class ModelRunningAccountInsertMultipleGetSchema(BaseModel):
    data: List[ModelRunningAccountInsertSingleGetSchema]
    n: int


class ModelRunningAccountInsertSingleTableSchema(
    ModelRunningAccountInsertSingleGetSchemaBase
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelRunningAccountInsertMultipleTableSchema(BaseModel):
    data: List[ModelRunningAccountInsertSingleTableSchema]
    n: int


ModelRunningAccountSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelRunningAccount, select_out_exclude
)
ModelRunningAccountSelectOutSingleTableSchemaBase= create_model("ModelRunningAccountSelectOutSingleTableSchemaBase",__base__=ModelRunningAccountSelectOutSingleTableSchemaBase)

class ModelRunningAccountSelectOutSingleTableSchema(
    ModelRunningAccountSelectOutSingleTableSchemaBase
):
    ID_User_Name: Optional[str] = Field(
        default=None, title="打卡签到者的姓名", description="这次打卡签到者的姓名"
    )
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelRunningAccountSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelRunningAccount, select_in_exclude, []
)
ModelRunningAccountSelectInSingleTableSchema = create_model("ModelRunningAccountSelectInSingleTableSchema",__base__=ModelRunningAccountSelectInSingleTableSchema)
user1 = aliased(ModelUser)
ModelRunningAccount_sub_stmt = (
    select(
        ModelRunningAccount,
        ModelUser.Name.label("ID_User_Name"),
        ModelUser.NoUser.label("ID_User_NoUser"),
        user1.Name.label("ID_Manager_Name"),
    )
    .join(ModelUser, ModelRunningAccount.ID_User == ModelUser.ID, isouter=True)
    .join(user1, ModelRunningAccount.IdManager == user1.ID, isouter=True)
    .where(ModelRunningAccount.Type_field == 4097)
    .subquery()
)
