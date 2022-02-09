"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-02 14:36:04
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
        [description]
    service_type : int
        [description]
    schema : [type], optional
        [description], by default None
    """
    if attr==1 or 2:
