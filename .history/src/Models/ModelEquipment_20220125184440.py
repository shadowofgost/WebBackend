"""
# @Time             : 2022-01-13 23:21:52
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelEquipment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 18:34:39
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

    ID_Location = Column(BigInteger, index=True, comment="设备所在地ID", doc="设备所在地ID")
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


ModelEquipmentSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelEquipment, select_out_exclude
)
ModelEquipmentSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelEquipment, select_in_exclude, []
)


def ModelEquipment_multiple_require_select(
    model,
    schema,
    session: Session,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelEquipment_multiple_require_select [特殊选择的表]

    [当传入的参数中只有id的时候，说明查询id情况下的取值]

    Args:
        model ([type]): [description]
        schema ([type]): [接受的表，比如user的schema，id=1，name=。。。。]
        session (Session): [description]
        physical (bool, optional): [显示的是逻辑表还是物理表，False表示逻辑表，True表示物理表]. Defaults to False.
        offset_data (int, optional): [sql中的偏移量，从偏移量+1的位置开始选择数据，实现分页功能]. Defaults to -1.
        limit_data (int, optional): [sql中选择的数据总数，表示每一页数据的总的个数]. Defaults to -1.

    Returns:
        [type]: [description]
    """
    schema_origin = schema.dict()
    schema_dict = {key: value for key, value in schema_origin.items() if value != None}
    if limit_data == -1 or offset_data == -1:
        if physical == False:
            schema_dict["IMark"] = 0
            stmt = select(model).filter_by(**schema_dict)
        else:
            stmt = select(model).filter_by(**schema.dict())
    else:
        if physical == False:
            schema_dict["IMark"] = 0
            stmt = (
                select(model)
                .filter_by(**schema_dict)
                .offset(offset_data)
                .limit(limit_data)
            )
        else:
            stmt = (
                select(model)
                .filter_by(**schema.dict())
                .offset(offset_data)
                .limit(limit_data)
            )
    try:
        result = session.execute(stmt).all()
        return result
    except Exception as e:
        return error_database_execution


def ModelEquipment_condition_select(
    model,
    session: Session,
    condition: str = "",
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelEquipment_condition_select [根据传入的条件进行查询]

    [根据传入的参数condition进行查询，condition的格式为：str，举例为：“ModelUser.id>=1,ModelUser.sex==2”这种,如果没有传入参数condition或者传入的是“”，那么查询所有值]

    Args:
        model ([type]): [description]
        session (Session): [description]
        condition (str, optional): [传入的参数]. Defaults to "".
        physical (bool, optional): [显示的是逻辑表还是物理表，False表示逻辑表，True表示物理表]. Defaults to False.
        offset_data (int, optional): [sql中的偏移量，从偏移量+1的位置开始选择数据，实现分页功能]. Defaults to -1.
        limit_data (int, optional): [sql中选择的数据总数，表示每一页数据的总的个数]. Defaults to -1.

    Returns:
        [type]: [description]
    """
    if limit_data == -1 or offset_data == -1:
        if physical == False:
            if condition == "" or condition == None:
                stmt = select(model).where(model.IMark == 0)
            else:
                stmt = select(model).where(eval(condition), model.IMark == 0)
        else:
            if condition == "" or condition == None:
                stmt = select(model)
            else:
                stmt = select(model).where(eval(condition))
    else:
        if physical == False:
            if condition == "" or condition == None:
                stmt = (
                    select(model)
                    .where(model.IMark == 0)
                    .offset(offset_data)
                    .limit(limit_data)
                )
            else:
                stmt = (
                    select(model)
                    .where(eval(condition), model.IMark == 0)
                    .offset(offset_data)
                    .limit(limit_data)
                )
        else:
            if condition == "" or condition == None:
                stmt = select(model).offset(offset_data).limit(limit_data)
            else:
                stmt = (
                    select(model)
                    .where(eval(condition))
                    .offset(offset_data)
                    .limit(limit_data)
                )
    try:
        result = session.execute(stmt).all()
        return result
    except Exception as e:
        return error_database_execution


def ModelEquipment_name_select(
    model,
    session: Session,
    name: str,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelEquipment_name_select [根据传入的条件进行查询]

    [根据传入的参数condition进行查询，condition的格式为：str，举例为：“ModelUser.id>=1,ModelUser.sex==2”这种,如果没有传入参数condition或者传入的是“”，那么查询所有值]

    Args:
        model ([type]): [description]
        session (Session): [description]
        name (str, optional): [需要查询的名字,近似查询].
        physical (bool, optional): [显示的是逻辑表还是物理表，False表示逻辑表，True表示物理表]. Defaults to False.
        offset_data (int, optional): [sql中的偏移量，从偏移量+1的位置开始选择数据，实现分页功能]. Defaults to -1.
        limit_data (int, optional): [sql中选择的数据总数，表示每一页数据的总的个数]. Defaults to -1.

    Returns:
        [type]: [description]
    """
    name = "%" + name + "%"
    if limit_data == -1 or offset_data == -1:
        if physical == False:
            stmt = select(model).where(model.Name.like(name), model.IMark == 0)
        else:
            stmt = select(model).where(model.Name.like(name))
    else:
        if physical == False:
            stmt = (
                select(model)
                .where(model.Name.like(name), model.IMark == 0)
                .offset(offset_data)
                .limit(limit_data)
            )
        else:
            stmt = (
                select(model)
                .where(model.Name.like(name))
                .offset(offset_data)
                .limit(limit_data)
            )
    try:
        result = session.execute(stmt).all()
        return result
    except Exception as e:
        return error_database_execution
