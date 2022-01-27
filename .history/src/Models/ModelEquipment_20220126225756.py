"""
# @Time             : 2022-01-13 23:21:52
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelEquipment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 22:57:11
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
from .ModelUser import ModelUser
from .ModelLocation import ModelLocation

ModelEquipment_nullable_columns = [
    "ID_IP",
    "MAC",
    "iTimeBegin",
    "iTimeLogin",
    "WhiteList",
]
ModelEquipment_nullable_columns.extend(nullable)


class ModelEquipment(ModelPublic):
    __tablename__ = "t_cyequipment"

    ID_Location = Column(
        BigInteger,
        index=True,
        comment="地点ID，外键",
        doc="这是地点的id序列号，同时连接location表的外键字段，连接的是id",
    )
    ID_User = Column(BigInteger, index=True, comment="设备拥有者ID", doc="设备拥有者ID")
    Name = Column(Unicode(32), index=True, comment="设备名称", doc="设备名称")
    ID_Location_SN = Column(BigInteger, index=True, comment="位置内编号", doc="位置内编号")
    ID_IP = Column(Unicode(16), index=True, comment="IP地址", doc="IP地址")
    MAC = Column(Unicode(24), comment="MAC地址", doc="MAC地址")
    State = Column(
        SmallInteger, index=True, comment="设备状态", doc="0：正常空闲、1：故障、2：其它、3：正常使用中、4开放"
    )
    Login = Column(SmallInteger, index=True, comment="登陆状态", doc="登录状态，0：未登录、1：已经登录 ")
    Link = Column(SmallInteger, index=True, comment="网络状态", doc="网络状态，0：脱机、1：在线")
    Class_field = Column(
        SmallInteger,
        index=True,
        name="Class",
        comment="设备种类",
        doc="设备种类，0：PC设备、2：刷卡门禁设备，11：服务器设备",
    )
    Dx = Column(Integer, doc="Layout显示坐标位置x（单位像素）", comment="Dx")
    Dy = Column(Integer, doc="Layout显示坐标位置y（单位像素）", comment="Dy")
    iTimeBegin = Column(Integer)
    iTimeLogin = Column(Integer)
    WhiteList = Column(Unicode(1024), doc="白名单", comment="白名单")
    PortListen = Column(Integer, comment="接受数据端口", doc="接收数据端口,默认:1234")
    Type = Column(Integer, comment="刷卡器类型", doc="刷卡器类型,默认:31")
    TimeDelay = Column(Integer, comment="门禁延迟时间", doc="门禁开门延时,默认:5秒")
    KeyCancel = Column(Integer, comment="取消键键码", doc="取消键键码，11")
    KeyDel = Column(Integer, comment="删除键键码", doc="删除键键码，13")
    KeyF1 = Column(Integer, comment="功能键键码", doc="功能键键码，12")
    OnAll = Column(Integer, comment="门禁刷卡总是开门", doc="默认：1 总是开门、1 校验成功后开门")
    RangeEqus = Column(Unicode(64), comment="管理设备范围", doc="管理设备范围")
    ListPlaces = Column(Unicode(64), comment="管理地点范围", doc="与RangeEqus并集关系")
    ID_Plan = Column(BigInteger, comment="计划ID", index=True)
    KeyOk = Column(Integer, comment="确定键键码", doc="确定键键码，14")


ModelEquipmentUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelEquipment, update_exclude
)


class ModelEquipmentUpdateMultipleGetSchema(ModelEquipmentUpdateSingleGetSchema):
    data: List[ModelEquipmentUpdateSingleGetSchema]
    n: int


class ModelEquipmentUpdateSingleTableSchema(ModelEquipmentUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelEquipmentUpdateMultipleTableSchema(ModelEquipmentUpdateSingleTableSchema):
    data: List[ModelEquipmentUpdateSingleTableSchema]
    n: int


ModelEquipmentInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelEquipment, insert_exclude, ModelEquipment_nullable_columns
)


class ModelEquipmentInsertMultipleGetSchema(ModelEquipmentInsertSingleGetSchema):
    data: List[ModelEquipmentInsertSingleGetSchema]
    n: int


class ModelEquipmentInsertSingleTableSchema(ModelEquipmentInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelEquipmentInsertMultipleTableSchema(ModelEquipmentInsertSingleTableSchema):
    data: List[ModelEquipmentInsertSingleTableSchema]
    n: int


ModelEquipmentSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelEquipment, select_out_exclude
)


class ModelEquipmentSelectOutSingleTableSchema(
    ModelEquipmentSelectOutSingleTableSchemaBase
):
    ID_Location_Name: Optional[str] = Field(
        default=None, title="地点名称", description="这是这节课程安排课对应的地点名称"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )


ModelEquipmentSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelEquipment, select_in_exclude, []
)
ModelEquipment_sub_stmt = select(
    ModelEquipment,
    ModelLocation.Name.label("ID_Location_Name"),
    ModelUser.Name.label("ID_Manager_Name"),
).join(ModelUser, ModelUser.ID == ModelEquipment.IdManager).join(Model)
