# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-13 18:28:37
# @Software         : Vscode
"""
from Models import ModelCurricula, ModelLocation, ModelUser
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List
from .PublicService import service_select
from Components import error_service_null
from .SchemaCurricula import ModelCurriculaSelectInSingleTableSchema


def orm_for_student(
    session: Session,
    id_manager: int,
    service_type: int,
    schema: ModelCurriculaSelectInSingleTableSchema,
):
    """
    orm_for_student [特殊的orm操作]

    [针对学生查询课表的特殊需求专门写的orm查询操作。]

    Parameters
    ----------
    session : Session
        [description]
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，2表示通过name查询数据]
    id_manager : int
        [description]
    schema : ModelCurriculaSelectInSingleTableSchema
        [description]
    """
    sub_user = select(ModelUser.ID, ModelUser.Name, ModelUser.NoUser).where(ModelUser.IMark == 0).subquery()  # type: ignore
    sub_location = select(ModelLocation.ID, ModelLocation.Name).where(ModelLocation.IMark == 0).subquery()  # type: ignore
    if service_type == 0:
        sub_curricula = (
            select(ModelCurricula)
            .where(ModelCurricula.RangeUsers.like("%{}%".format(str(id_manager))))
            .where(ModelCurricula.IMark == 0)
            .subquery()  # type: ignore
        )
        stmt = (
            select(
                sub_curricula,
                sub_location.c.Name.label("ID_Location_Name"),
                sub_user.c.Name.label("ID_Speaker_Name"),  # type: ignore
            )
            .outerjoin(sub_user, sub_user.c.ID == sub_curricula.c.ID_Speaker)
            .outerjoin(sub_location, sub_location.c.ID == sub_curricula.c.ID_Location)
        )
    elif service_type == 2:
        sub_curricula = (
            select(ModelCurricula)
            .where(ModelCurricula.RangeUsers.like("%{}%".format(str(id_manager))))
            .where(ModelCurricula.Name.like("%{}%".format(schema.Name)))  # type: ignore
            .where(ModelCurricula.IMark == 0)
            .subquery()  # type: ignore
        )
        stmt = (
            select(
                sub_curricula,
                sub_location.c.Name.label("ID_Location_Name"),
                sub_user.c.Name.label("ID_Speaker_Name"),  # type: ignore
            )
            .outerjoin(sub_user, sub_user.c.ID == sub_curricula.c.ID_Speaker)
            .outerjoin(sub_location, sub_location.c.ID == sub_curricula.c.ID_Location)
        )
    else:
        raise error_service_null
    try:
        return session.execute(stmt).mappings().all()
    except Exception:
        raise error_service_null


def get_curricula(
    session: Session,
    id_manager: int,
    attr: int,
    service_type: int,
    schema: ModelCurriculaSelectInSingleTableSchema,
) -> List[dict]:
    """
    get_curricula [查询课程表]

    [根据权限查询课程表]

    Parameters
    ----------
    session : Session
        [description]
    id_manager : intint
        [description]
    attr : int
        [默认是使用0，用户，1，管理员，2，超级管理员]
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过Nouser进行查询]
    schema : [type], optional
        [description], by default None
        [description], by default None
    extra_attr : int, optional
        [额外的权限，用于service层用户的角色的判断,0表示学生，1表示老师], by default 0

    Returns
    -------
    [type]
        [description]
    """
    model_name = "ModelCurricula"
    if attr == 1:
        return service_select(session, model_name, service_type, schema)
    elif attr == 3:
        return orm_for_student(session, id_manager, service_type, schema)
    elif attr == 2:
        schema.ID_Speaker = id_manager
        if service_type == 0:
            return service_select(session, model_name, 3, schema)
        else:
            return service_select(session, model_name, service_type, schema)
    else:
        raise error_service_null
