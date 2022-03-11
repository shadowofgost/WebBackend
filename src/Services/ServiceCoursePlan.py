# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-23 15:52:34
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceCoursePlan.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 17:36:26
# @Software         : Vscode
"""
from sqlalchemy.orm import Session

from .PublicService import service_select
from .SchemaCoursePlan import ModelCoursePlanSelectInSingleTableSchema


def get_course_plan(
    session: Session,
    attr: int,
    service_type: int,
    schema: ModelCoursePlanSelectInSingleTableSchema,
):
    """
    get_course_plan _summary_

    _extended_summary_

    Parameters
    ----------
    session : Session
        _description_
    id_manager : int
        _description_
    attr : int
        _description_
    service_type : int
        _description_
    schema : ModelCoursePlanSelectInSingleTableSchema
        _description_

    Returns
    -------
    _type_
        假设教师和学生提交的schema中包含id_curricula的json数据格式。
    """
    model = "ModelCoursePlan"
    if attr == 1:
        return service_select(session,  model, service_type, schema)
    else:
        return service_select(session,  model, 3, schema)
