"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-02 15:34:53
# @Software         : Vscode
"""
from .PublicService import delete, insert, update, select
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..Models import ModelCurriculaSelectInSingleTableSchema
from typing import List, Optional


def orm_for_student(session: Session,id_manager:int,service_type:int, schema:ModelCurriculaSelectInSingleTableSchema):
    '''
    orm_for_student [特殊的orm操作]

    [针对学生查询课表的特殊需求专门写的orm查询操作。]

    Parameters
    ----------
    session : Session
        [description]
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过Nouser进行查询]
    id_manager : int
        [description]
    schema : ModelCurriculaSelectInSingleTableSchema
        [description]
    '''
    

def get_curricula(
    session: Session,
    id_manager: int,
    attr: int,
    service_type: int,
    schema: ModelCurriculaSelectInSingleTableSchema,
    extra_attr: int = 0,
):
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
    if attr == 1 or 2:
        return select(session, id_manager, "ModelCurricula", service_type, schema)
    elif attr == 0:
        if extra_attr == 0:
            return orm_for_student(session,id_manager,service_type, schema)
        elif extra_attr == 1:
            schema.ID_Speaker = id_manager
            if service_type == 0:
                return select(session, id_manager, "ModelCurricula", 3, schema)
            else:
                return select(session, id_manager, "ModelCurricula", service_type, schema)
