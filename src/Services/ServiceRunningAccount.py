# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:20
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceRunningAccount.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-23 15:14:57
# @Software         : Vscode
"""
from typing import List, Optional

from Components import error_database_execution, error_service_null
from loguru import logger
from Models import ModelCoursePlan, ModelCurricula, ModelRunningAccount, ModelUser
from pydantic import Field, BaseModel, validator
from sqlalchemy import select
from sqlalchemy.orm import Session
from .SchemaRunningAccount import (
    ModelRunningAccountSelectInSingleTableSchema,
    ModelRunningAccountSelectOutSingleTableSchemaBase,
)
from .ServiceUser import SchemaUserPydantic


##TODO:这里的schema不一样，需要注意是根据RunningAccount直接手写的。
class RunningAccountSchema(BaseModel):
    ID: Optional[int] = Field(
        default=None,
        title="id序列号",
        description="这是RunningAccount表的id序列号,如果为None表示数据不存在，打卡缺勤,status是未签到",
    )
    Time: int = Field(
        default=0,
        title="0表示此数据不存在，生成记录的时间",
        description="生成记录（发生费用）的时间，从2000-1-1日计秒,如果默认为0表示此数据不存在",
    )
    Type: int = Field(
        default=4097,
        title="这是外键，记录的类型",
        description="这是记录的类型，其值定义如下：参见T_CyTypeRA表每一个功能的id，例如：考勤：4097，这是T_CyTypeRA表的id和外键",
    )
    Param2: Optional[int] = Field(
        title="这是外键安排编号",
        description="这是外键，安排编号，例如：讲座、课程的编号：也就是对应Plan的id此时Type=4097；取消交易记录的ID：Type=0x106，这是连接Plan表的id",
    )
    ID_User: int = Field(title="这是外键用户ID", description="这是外键，链接User的用户ID")
    ID_User_Name: Optional[str] = Field(
        default=None, title="打卡签到者的姓名", description="这次打卡签到者的姓名"
    )
    ID_User_NoUser: Optional[str] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )
    TimeBegin: int = Field(title="课程开始的时间", description="这是这节课开始的时间，从2000-1-1日计秒")
    TimeEnd: int = Field(title="课程结束的时间", description="这是这节课结束的时间，从2000-1-1日计秒")
    Status: int = Field(
        default=0, title="签到状态", description="这是这节课程的签到状态，0表示未知，1表示已签到，2表示未签到，3表示迟到"
    )

    @validator("Type", pre=True)
    def Type_format(cls, v):
        if v is None:
            return 4097
        else:
            return v

    @validator("Time", pre=True)
    def Time_format(cls, v):
        if v is None:
            return 0
        else:
            return v

    class Config:
        orm_mode = True


def update_status(data: List[RunningAccountSchema]):
    tmp = []
    for i in range(len(data)):
        if data[i].Time == 0 or data[i].Time is None:
            data[i].Status = 2
        elif data[i].Time >= data[i].TimeBegin:
            data[i].Status = 1
        elif data[i].TimeBegin < data[i].Time < data[i].TimeEnd:
            data[i].Status = 3
        else:
            data[i].Status = 0
        tmp.append(data[i].dict())
    return tmp


def execute_database(stmt, session):
    try:
        result = session.execute(stmt).mappings().all()
    except Exception as e:
        logger.error("数据库执行出错，查看数据库数据情况")
        raise error_database_execution
    return result


def transform_into_schema(
    data_initial: dict, time_begin: int, time_end: int, id_courseplan: int
):
    try:
        data = RunningAccountSchema(
            **data_initial, TimeBegin=time_begin, TimeEnd=time_end
        )
    except Exception as e:
        logger.error("数据转化出错")
        raise error_database_execution
    data.Param2 = id_courseplan
    return data


##TODO:WARNING随着sqlalchemy的升级，subquery的查询列的方法会发生改变，会从原来的sub.c.column_name变成sub.column_name
def get_for_student(
    session: Session,
    user: SchemaUserPydantic,
    id_courseplan: int,
):
    """
    获取用户的运行账户
    """
    null_student = {
        "ID": None,
        "ID_User": user.ID,
        "ID_User_NoUser": user.NoUser,
        "ID_User_Name": user.Name,
        "Param2": id_courseplan,
        "Time": 0,
    }
    sub_course_plan = (
        select(
            ModelCoursePlan.ID_Curricula,  # type: ignore
            ModelCoursePlan.TimeBegin,
            ModelCoursePlan.TimeEnd,  # type: ignore
        )
        .where(ModelCoursePlan.ID == id_courseplan)
        .where(ModelCoursePlan.IMark == 0)
    )
    result_courseplan = execute_database(sub_course_plan, session)
    id_curricula = result_courseplan[0]["ID_Curricula"]
    time_begin = result_courseplan[0]["TimeBegin"]
    time_end = result_courseplan[0]["TimeEnd"]
    ##上述操作是为了获取课程开始时间和结束时间
    sub_runningaccount = (
        select(ModelRunningAccount)
        .where(
            ModelRunningAccount.Type == 4097,
            ModelRunningAccount.IMark == 0,  # type: ignore
            ModelRunningAccount.Param2 == id_courseplan,
        )
        .subquery()
    )
    sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).where(ModelUser.ID == user.ID).subquery()  # type: ignore
    stmt = select(
        sub_runningaccount,
        sub_user.c.Name.label("ID_User_Name"),
        sub_user.c.NoUser.label("ID_User_NoUser"),
    ).outerjoin(sub_user, sub_runningaccount.c.ID_User == sub_user.c.ID)
    result = execute_database(stmt, session)
    if result == []:
        data = transform_into_schema(
            null_student,
            time_begin,
            time_end,
            id_courseplan,
        )
    else:
        data = transform_into_schema(result[0], time_begin, time_end, id_courseplan)
    data = update_status([data])
    return data


def get_for_teacher(session: Session, user: SchemaUserPydantic, id_courseplan: int):
    sub_course_plan = (
        select(
            ModelCoursePlan.ID_Curricula,  # type: ignore
            ModelCoursePlan.TimeBegin,
            ModelCoursePlan.TimeEnd,  # type: ignore
        )
        .where(ModelCoursePlan.ID == id_courseplan)
        .where(ModelCoursePlan.IMark == 0)
    )
    result_courseplan = execute_database(sub_course_plan, session)
    id_curricula = result_courseplan[0]["ID_Curricula"]
    time_begin = result_courseplan[0]["TimeBegin"]
    time_end = result_courseplan[0]["TimeEnd"]
    ##上述操作是为了获取课程开始时间和结束时间
    stmt = (
        select(ModelCurricula.RangeUsers)  # type: ignore
        .where(ModelCurricula.ID == id_curricula)
        .where(ModelCurricula.IMark == 0)
    )
    RangeUsers = execute_database(stmt, session)
    range_users_initial_data = RangeUsers[0]["RangeUsers"].strip().split(";")
    range_users = [int(i.strip()) for i in range_users_initial_data if i != ""]
    sub_runningaccount = (
        select(ModelRunningAccount)
        .where(ModelRunningAccount.Type == 4097)
        .where(ModelRunningAccount.IMark == 0)
        .where(ModelRunningAccount.Param2 == id_courseplan)
        .subquery()  # type: ignore
    )
    sub_user = (
        select(ModelUser)
        .where(ModelUser.IMark == 0)
        .where(ModelUser.NoUser.in_(range_users))
        .subquery()  # type: ignore
    )
    stmt = select(
        sub_user.c.ID.label("ID_User"),
        sub_user.c.Name.label("ID_User_Name"),
        sub_user.c.NoUser.label("ID_User_NoUser"),
        sub_runningaccount,
    ).outerjoin(sub_runningaccount, sub_runningaccount.c.ID_User == sub_user.c.ID)
    result_data = execute_database(stmt, session)
    data_initial_list = []
    for i in range(len(result_data)):
        data_initial_list.append(
            transform_into_schema(
                result_data[i],
                time_begin=time_begin,
                time_end=time_end,
                id_courseplan=id_courseplan,
            )
        )
    data = update_status(data_initial_list)
    return data


def get_for_admin(
    session: Session,
    user: SchemaUserPydantic,
    service_type: int,
    schema: ModelRunningAccountSelectInSingleTableSchema,
):
    pass


def get_running_account(
    session: Session,
    user: SchemaUserPydantic,
    schema: ModelRunningAccountSelectInSingleTableSchema,
):
    """
    获取用户的运行账户
    """
    if user.Attr == 1 or user.Attr == 2:
        return get_for_teacher(session, user, schema.Param2)
    elif user.Attr == 3:
        return get_for_student(session, user, schema.Param2)
    else:
        return get_for_student(session, user, schema.Param2)
