"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-02 14:46:12
# @Software         : Vscode
"""
from .PublicService import delete, insert, update, select
from sqlalchemy.orm import Session


def get_curricula(
    session: Session, id_manager: int, attr: int, service_type: int, schema=None
):
    """
    get_curricula [查询课程表]

    [根据权限查询课程表]

    Parameters
    ----------
    session : Session
        [description]
    id_manager : int
        [description]
    attr : int
        [d]
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过]
    schema : [type], optional
        [description], by default None
    """
    if attr == 1 or 2:
        return select(session,id_manager,"ModelCurricula",service_type,schema)
