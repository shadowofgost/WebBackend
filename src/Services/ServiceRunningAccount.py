"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:20
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceRunningAccount.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-09 11:51:13
# @Software         : Vscode
"""
from Models import ModelUser, ModelCoursePlan, ModelRunningAccount, ModelCurricula
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import Field
from typing import Optional, List
from Components.Exceptions import error_service_null, error_database_execution
from .SchemaRunningAccount import (
    ModelRunningAccountSelectInSingleTableSchema,
    ModelRunningAccountSelectOutSingleTableSchemaBase,
)
from .ServiceUser import SchemaUserPydantic

##TODO:这里的schema不一样，需要注意是根据RunningAccount直接手写的。
class RunningAccountSchema(ModelRunningAccountSelectOutSingleTableSchemaBase):
    ID: Optional[int] = Field(
        default=None,
        title="id序列号",
        description="这是RunningAccount表的id序列号,如果为None表示数据不存在，打卡缺勤,status是未签到",
    )
    Time: int = Field(title="生成记录的时间", description="生成记录（发生费用）的时间，从2000-1-1日计秒")
    ID_User_Name: Optional[str] = Field(
        default=None, title="打卡签到者的姓名", description="这次打卡签到者的姓名"
    )
    ID_User_NoUser: Optional[int] = Field(
        default=None, title="打卡者的学号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )
    TimeBegin: int = Field(title="课程开始的时间", description="这是这节课开始的时间，从2000-1-1日计秒")
    TimeEnd: int = Field(title="课程结束的时间", description="这是这节课结束的时间，从2000-1-1日计秒")
    Status: int = Field(
        default=0, title="签到状态", description="这是这节课程的签到状态，0表示未知，1表示已签到，2表示未签到，3表示迟到"
    )

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
        raise error_database_execution
    return result


def transform_into_schema(data_initial: dict):
    try:
        data = RunningAccountSchema(**data_initial)
    except Exception as e:
        raise error_database_execution
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
        "TimeBegin": 0,
        "TimeEnd": 0,
    }
    sub_runningaccount = (
        select(ModelRunningAccount)
        .where(
            ModelRunningAccount.Type == 4097,
            ModelRunningAccount.IMark == 0,
            ModelRunningAccount.Param2 == id_courseplan,
        )
        .subquery()
    )
    sub_course_plan = (
        select(ModelCoursePlan.ID, ModelCoursePlan.TimeBegin, ModelCoursePlan.TimeEnd)
        .where(ModelCoursePlan.IMark == 0)
        .where(ModelCoursePlan.ID == id_courseplan)
        .subquery()
    )
    sub_user = select(ModelUser).where(ModelUser.IMark == 0).subquery()
    stmt = (
        select(
            sub_runningaccount,
            sub_course_plan.c.TimeBegin,
            sub_course_plan.c.TimeEnd,
            sub_user.c.Name.label("ID_User_Name"),
            sub_user.c.NoUser.label("ID_User_NoUser"),
        )
        .join(
            sub_course_plan,
            sub_runningaccount.c.Param2 == sub_course_plan.c.ID,
            isouter=True,
        )
        .join(sub_user, sub_runningaccount.c.ID_User == sub_user.c.ID, isouter=True)
    )
    result = execute_database(stmt, session)
    if result == []:
        stmt = select(sub_course_plan)
        result_courseplan = execute_database(stmt, session)
        null_student["TimeBegin"] = result_courseplan[0]["TimeBegin"]
        null_student["TimeEnd"] = result_courseplan[0]["TimeEnd"]
        data = transform_into_schema(null_student)
    else:
        data = transform_into_schema(result[0])
    data = update_status([data])
    return data[0]


def get_for_teacher(session: Session, user: SchemaUserPydantic, id_courseplan: int):
    stmt = (
        select(
            ModelCoursePlan.ID_Curricula,
            ModelCoursePlan.TimeBegin,
            ModelCoursePlan.TimeEnd,
        )
        .where(ModelCoursePlan.ID == id_courseplan)
        .where(ModelCoursePlan.IMark == 0)
    )
    result_courseplan = execute_database(stmt, session)
    id_curricula = result_courseplan[0]["ID_Curricula"]
    time_begin = result_courseplan[0]["TimeBegin"]
    time_end = result_courseplan[0]["TimeEnd"]
    stmt = (
        select(ModelCurricula.RangeUsers)
        .where(ModelCurricula.ID == id_curricula)
        .where(ModelCurricula.IMark == 0)
    )
    RangeUsers = execute_database(stmt, session)
    range_users_initial_data = RangeUsers[0]["RangeUsers"].split(";")
    range_users = [int(i) for i in range_users_initial_data]
    sub_runningaccount = (
        select(ModelRunningAccount)
        .where(ModelRunningAccount.Type == 4097)
        .where(ModelRunningAccount.IMark == 0)
        .where(ModelRunningAccount.Param2 == id_courseplan)
        .subquery()
    )
    sub_user = (
        select(ModelUser)
        .where(ModelUser.IMark == 0)
        .where(ModelUser.NoUser.in_(range_users))
        .subquery()
    )
    stmt = select(
        sub_user.c.ID.label("ID_User_Back"),
        sub_user.c.Name.label("ID_User_Name"),
        sub_user.c.NoUser.label("ID_User_NoUser"),
        sub_runningaccount,
    ).join(sub_runningaccount, sub_runningaccount.c.ID_User == sub_user.c.ID)
    result_data = execute_database(stmt, session)
    data_initial_list = []
    for i in range(len(result_data)):
        result_data[i]["TimeBegin"] = time_begin
        result_data[i]["TimeEnd"] = time_end
        result_data[i]["Param2"] = id_courseplan
        result_data[i]["ID_User"] = result_data[i]["ID_User_Back"]
        data_initial_list.append(transform_into_schema(result_data[i]))
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
