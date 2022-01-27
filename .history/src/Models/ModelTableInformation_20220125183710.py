"""
# @Time             : 2022-01-13 23:23:28
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTableInformation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 18:33:22
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

ModelTableInformation_nullable_columns = []
ModelTableInformation_nullable_columns.extend(nullable)


class ModelTableInformation(ModelPublic):
    __tablename__ = "t_cytableinfo"

    Name = Column(Unicode(50), index=True)
    NameTable = Column(Unicode(50), index=True)


ModelTableInformationUpdateSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, update_exclude
)


class ModelTableInformationUpdateMultipleGetSchema(
    ModelTableInformationUpdateSingleGetSchema
):
    data: List[ModelTableInformationUpdateSingleGetSchema]
    n: int


class ModelTableInformationUpdateSingleTableSchema(
    ModelTableInformationUpdateSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelTableInformationUpdateMultipleTableSchema(
    ModelTableInformationUpdateSingleTableSchema
):
    data: List[ModelTableInformationUpdateSingleTableSchema]
    n: int


ModelTableInformationInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, insert_exclude, ModelTableInformation_nullable_columns
)


class ModelTableInformationInsertMultipleGetSchema(
    ModelTableInformationInsertSingleGetSchema
):
    data: List[ModelTableInformationInsertSingleGetSchema]
    n: int


class ModelTableInformationInsertSingleTableSchema(
    ModelTableInformationInsertSingleGetSchema
):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelTableInformationInsertMultipleTableSchema(
    ModelTableInformationInsertSingleTableSchema
):
    data: List[ModelTableInformationInsertSingleTableSchema]
    n: int


ModelTableInformationSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, select_out_exclude
)
ModelTableInformationSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelTableInformation, select_in_exclude, []
)


def ModelTableInformation_multiple_require_select(
    model,
    schema,
    session: Session,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelTableInformation_multiple_require_select [特殊选择的表]

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


def ModelTableInformation_condition_select(
    model,
    session: Session,
    condition: str = "",
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelTableInformation_condition_select [根据传入的条件进行查询]

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


def ModelTableInformation_name_select(
    model,
    session: Session,
    name: str,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    ModelTableInformation_name_select [根据传入的条件进行查询]

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
