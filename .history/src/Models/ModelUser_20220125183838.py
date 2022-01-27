"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelUser.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 18:33:03
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

ModelUser_nullable_columns = ["Yue", "Yue2", "Email", "Phone", "LocalID"]
ModelUser_nullable_columns.extend(nullable)
ModelUserExtension_nullable_columns = ["Photo_dataF"]
ModelUserExtension_nullable_columns.extend(nullable)


class ModelUser(ModelPublic):
    __tablename__ = "t_cyuser"
    Deptid = Column(BigInteger, index=True, comment="用户所在部门的ID", doc="用户所在部门的ID")
    NoCard = Column(Unicode(32), index=True, comment="卡号", doc="卡号，不能超过15字符")
    NoUser = Column(
        Unicode(32), index=True, comment="账号（学工号）", doc="这是账号（学工号），不能超过15字符"
    )
    Name = Column(Unicode(32), index=True, comment="用户名", doc="这是用户名，不能超过15字符")
    Psw = Column(Unicode(32), index=True, comment="密码", doc="密码，不能超过15字符")
    Sex = Column(SmallInteger, index=True, comment="用户性别", doc="这是用户性别，0 女，1 男")
    Attr = Column(
        SmallInteger,
        index=True,
        comment="用户管理权限",
        doc="这是用户属性，表示用户的管理权限，0 普通用户，1 管理员，2 超级管理员（可对管理员进行控制）",
    )
    AttrJf = Column(
        SmallInteger,
        index=True,
        comment="机房管理权限",
        doc="这是用户属性，表示机房管理权限，0 普通用户，1 管理员，2 超级管理员（可对管理员进行控制）",
    )
    Email = Column(Unicode(254), index=True)
    Phone = Column(Integer, index=True)
    Yue = Column(Integer, comment="用户余额1", doc="这是用户余额1，单位为分（默认）")
    Yue2 = Column(Integer, comment="用户余额2", doc="这是用户余额2，单位为分（扩展于特殊需求）")
    LocalID = Column(Unicode(1024), comment="管理房间的ID列表", doc="管理房间的ID列表")


class ModelUserExtension(ModelPublic):
    __tablename__ = "t_cyuserex"

    Photo = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo_dataF = Column(Unicode(2048), default="0")


ModelUserUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelUser, update_exclude)


class ModelUserUpdateMultipleGetSchema(ModelUserUpdateSingleGetSchema):
    data: List[ModelUserUpdateSingleGetSchema]
    n: int


class ModelUserUpdateSingleTableSchema(ModelUserUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelUserUpdateMultipleTableSchema(ModelUserUpdateSingleTableSchema):
    data: List[ModelUserUpdateSingleTableSchema]
    n: int


ModelUserInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUser, insert_exclude, ModelUser_nullable_columns
)


class ModelUserInsertMultipleGetSchema(ModelUserInsertSingleGetSchema):
    data: List[ModelUserInsertSingleGetSchema]
    n: int


class ModelUserInsertSingleTableSchema(ModelUserInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelUserInsertMultipleTableSchema(ModelUserInsertSingleTableSchema):
    data: List[ModelUserInsertSingleTableSchema]
    n: int


ModelUserSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUser, select_out_exclude
)
ModelUserSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUser, select_in_exclude, []
)
ModelUserExtensionUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, update_exclude
)


class ModelUserExtensionUpdateMultipleGetSchema(
    ModelUserExtensionUpdateSingleGetSchema
):
    data: List[ModelUserExtensionUpdateSingleGetSchema]
    n: int


class ModelUserExtensionUpdateSingleTableSchema(
    ModelUserExtensionUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelUserExtensionUpdateMultipleTableSchema(
    ModelUserExtensionUpdateSingleTableSchema
):
    data: List[ModelUserExtensionUpdateSingleTableSchema]
    n: int


ModelUserExtensionInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, insert_exclude, ModelUserExtension_nullable_columns
)


class ModelUserExtensionInsertMultipleGetSchema(
    ModelUserExtensionInsertSingleGetSchema
):
    data: List[ModelUserExtensionInsertSingleGetSchema]
    n: int


class ModelUserExtensionInsertSingleTableSchema(
    ModelUserExtensionInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelUserExtensionInsertMultipleTableSchema(
    ModelUserExtensionInsertSingleTableSchema
):
    data: List[ModelUserExtensionInsertSingleTableSchema]
    n: int


ModelUserExtensionSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, select_out_exclude
)
ModelUserExtensionSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelUserExtension, select_in_exclude, []
)


def ModelUser_multiple_require_select(
    model,
    schema,
    session: Session,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelUser_multiple_require_select [特殊选择的表]

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


def ModelUser_condition_select(
    model,
    session: Session,
    condition: str = "",
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelUser_condition_select [根据传入的条件进行查询]

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


def ModelUser_name_select(
    model,
    session: Session,
    name: str,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelUser_name_select [根据传入的条件进行查询]

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


def ModelUserExtension_multiple_require_select(
    model,
    schema,
    session: Session,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelUserExtension_multiple_require_select [特殊选择的表]

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


def ModelUserExtension_condition_select(
    model,
    session: Session,
    condition: str = "",
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelUserExtension_condition_select [根据传入的条件进行查询]

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


def ModelUserExtension_name_select(
    model,
    session: Session,
    name: str,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelUserExtension_name_select [根据传入的条件进行查询]

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
