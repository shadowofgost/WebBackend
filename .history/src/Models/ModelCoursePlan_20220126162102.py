"""
# @Time             : 2022-01-13 23:19:45
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelCoursePlan.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 16:14:14
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
from sqlalchemy.orm import Session, sessionmaker, aliased

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
from .ModelCurricula import ModelCurricula
from .ModelLocation import ModelLocation
from .ModelUser import ModelUser

ModelCoursePlan_nullable_columns = [
    "RangeUsers",
    "ListDepts",
    "RangeEqus",
    "ListPlaces",
    "MapUser2Equ",
    "AboutSpeaker",
]
ModelCoursePlan_nullable_columns.extend(nullable)


class ModelCoursePlan(ModelPublic):
    __tablename__ = "t_cyplan"
    ID_Curricula = Column(BigInteger, index=True, comment="课程ID", doc="这是课程的id序列号")
    ID_Location = Column(BigInteger, index=True, comment="地点ID", doc="这是地点的id序列号")
    ID_Speaker = Column(BigInteger, index=True, comment="主讲人ID", doc="这是主讲人的id序列号")
    TimeBegin = Column(
        Integer, index=True, comment="开始时间", doc="这是开始时间,单位是秒，每一天0时0分0秒开始的秒数"
    )
    TimeEnd = Column(Integer, index=True, comment="结束时间", doc="这是结束时间,单位是秒")
    Attr = Column(
        SmallInteger,
        index=True,
        comment="类型判断",
        doc="1代表实验类型、2代表普通上课类型、3讲座考勤类型，0或NULL同T_CyCurricula 实验类型：奇数刷卡派位，偶数刷卡下机，并记录派位编号 上课考勤类型：刷卡记录刷卡机编号 讲座考勤类型：刷卡记录刷卡机编号 ",
    )
    Charge = Column(SmallInteger, index=True, comment="收费类型字段", doc="免费0、收费1、开放2，NULL")
    PwAccess = Column(
        SmallInteger, index=True, comment="派位字段", doc="不派位0、刷卡派位1（派位指用户刷卡时系统指定座位）"
    )
    PwContinuous = Column(
        SmallInteger, index=True, comment="是否连续排位字段", doc="连续派位0、随机派位1"
    )
    PwDirection = Column(
        SmallInteger, index=True, comment="排位顺序字段", doc="顺序派位0、逆序派位1（当设置为随机派位时本功能无效）"
    )
    DoorOpen = Column(SmallInteger, index=True, comment="是否开门字段", doc="开门0、不开门1")
    TimeBeginCheckBegin = Column(
        Integer, comment="考勤开始的时刻表", doc="安排考勤开始的最早时间（单位为分钟，0代表无效）"
    )
    TimeBeginCheckEnd = Column(
        Integer, comment="考勤开始的时刻表", doc="安排考勤开始的最晚时间（单位为分钟，0代表无效）"
    )
    TimeEndCheckBegin = Column(
        Integer, comment="考勤结束的时刻表", doc="安排考勤结束的最早时间（单位为分钟，0代表无效）"
    )
    TimeEndCheckEnd = Column(
        Integer, comment="考勤开始的最早时刻表", doc="安排考勤结束的最早时间（单位为分钟，0代表无效）"
    )
    RangeUsers = Column(Unicode(1024), comment="学生学号列表", doc="学生学号列表，以逗号分隔")
    ListDepts = Column(Unicode(1024), comment="部门列表", doc="参加安排的部门列表，以逗号分隔")
    RangeEqus = Column(Unicode(1024), comment="座位范围列表", doc="课程使用的座位范围列表")
    ListPlaces = Column(Unicode(1024), comment="地点列表", doc="课程使用的地点列表")
    MapUser2Equ = Column(Unicode(1024), comment="对应列表", doc="学生和课程的对应表")
    AboutSpeaker = Column(Unicode(1024), comment="主讲人信息", doc="主讲人信息")


ModelCoursePlanUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelCoursePlan, update_exclude
)


class ModelCoursePlanUpdateMultipleGetSchema(ModelCoursePlanUpdateSingleGetSchema):
    data: List[ModelCoursePlanUpdateSingleGetSchema]
    n: int


class ModelCoursePlanUpdateSingleTableSchema(ModelCoursePlanUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelCoursePlanUpdateMultipleTableSchema(ModelCoursePlanUpdateSingleTableSchema):
    data: List[ModelCoursePlanUpdateSingleTableSchema]
    n: int


ModelCoursePlanInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelCoursePlan, insert_exclude, ModelCoursePlan_nullable_columns
)


class ModelCoursePlanInsertMultipleGetSchema(ModelCoursePlanInsertSingleGetSchema):
    data: List[ModelCoursePlanInsertSingleGetSchema]
    n: int


class ModelCoursePlanInsertSingleTableSchema(ModelCoursePlanInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelCoursePlanInsertMultipleTableSchema(ModelCoursePlanInsertSingleTableSchema):
    data: List[ModelCoursePlanInsertSingleTableSchema]
    n: int


ModelCoursePlanSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelCoursePlan, select_out_exclude
)
ModelCoursePlanSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelCoursePlan, select_in_exclude, []
)


def ModelCoursePlan_multiple_require_select(
    model,
    schema,
    session: Session,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelCoursePlan_multiple_require_select [特殊选择的表]

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
            stmt = (
                select(
                    ModelCoursePlan,
                    ModelCurricula.Name.label("ID_Curricula_Name"),
                    ModelLocation.Name.label("ID_Location_Name"),
                    ModelUser.Name.label("ID_Speaker_Name"),
                )
                .join(
                    ModelCurricula,
                    ModelCurricula.ID == ModelCoursePlan.ID_Curricula,
                    isouter=True,
                )
                .join(
                    ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True
                )
                .join(
                    ModelLocation,
                    ModelLocation.ID == ModelCoursePlan.ID_Location,
                    isouter=True,
                )
            )
            stmt = select(
                ModelCoursePlan,
                ModelCurricula.Name.label("ID_Curricula_Name"),
                ModelLocation.Name.label("ID_Location_Name"),
                ModelUser.Name.label("ID_Speaker_Name"),
            ).filter_by(**schema_dict)
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


def ModelCoursePlan_condition_select(
    model,
    session: Session,
    condition: str = "",
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelCoursePlan_condition_select [根据传入的条件进行查询]

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


def ModelCoursePlan_name_select(
    model,
    session: Session,
    name: str,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelCoursePlan_name_select [根据传入的条件进行查询]

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
