"""
# @Time             : 2022-01-13 23:22:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelMmx.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-25 17:59:00
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import (
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    BigInteger,
    select,
)
from sqlalchemy.orm import Session, sessionmaker
from .PublicValues import error_database_execution, error_schema_validation
from pydantic import BaseModel, Field
from typing import Container, List, Optional

from .ModelPublic import (
    ModelPublic,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
    format_current_time,
)

ModelMmx_nullable_columns = []
ModelMmx_nullable_columns.extend(nullable)
ModelMmxData_nullable_columns = ["Data"]
ModelMmxData_nullable_columns.extend(nullable)


class ModelMmx(ModelPublic):
    __tablename__ = "t_cymmx"

    ID_Data = Column(BigInteger, index=True, comment="媒体内容的ID", doc="媒体内容的ID")
    ID_Type = Column(SmallInteger, index=True, comment="媒体类型", doc="媒体类型，1为PPT类型")


class ModelMmxData(ModelPublic):
    __tablename__ = "t_cymmxdata"

    Data = Column(Unicode(1024), comment="媒体的内容", doc="媒体的内容")


ModelMmxUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmx, update_exclude)


class ModelMmxUpdateMultipleGetSchema(ModelMmxUpdateSingleGetSchema):
    data: List[ModelMmxUpdateSingleGetSchema]
    n: int


class ModelMmxUpdateSingleTableSchema(ModelMmxUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelMmxUpdateMultipleTableSchema(ModelMmxUpdateSingleTableSchema):
    data: List[ModelMmxUpdateSingleTableSchema]
    n: int


ModelMmxInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelMmx, insert_exclude, ModelMmx_nullable_columns
)


class ModelMmxInsertMultipleGetSchema(ModelMmxInsertSingleGetSchema):
    data: List[ModelMmxInsertSingleGetSchema]
    n: int


class ModelMmxInsertSingleTableSchema(ModelMmxInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxInsertMultipleTableSchema(ModelMmxInsertSingleTableSchema):
    data: List[ModelMmxInsertSingleTableSchema]
    n: int


ModelMmxSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmx, select_out_exclude
)
ModelMmxSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmx, select_in_exclude, []
)
ModelMmxDataUpdateSingleGetSchema = sqlalchemy_to_pydantic(ModelMmxData, update_exclude)


class ModelMmxDataUpdateMultipleGetSchema(ModelMmxDataUpdateSingleGetSchema):
    data: List[ModelMmxDataUpdateSingleGetSchema]
    n: int


class ModelMmxDataUpdateSingleTableSchema(ModelMmxDataUpdateSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelMmxDataUpdateMultipleTableSchema(ModelMmxDataUpdateSingleTableSchema):
    data: List[ModelMmxDataUpdateSingleTableSchema]
    n: int


ModelMmxDataInsertSingleGetSchema = sqlalchemy_to_pydantic(
    ModelMmxData, insert_exclude, ModelMmxData_nullable_columns
)


class ModelMmxDataInsertMultipleGetSchema(ModelMmxDataInsertSingleGetSchema):
    data: List[ModelMmxDataInsertSingleGetSchema]
    n: int


class ModelMmxDataInsertSingleTableSchema(ModelMmxDataInsertSingleGetSchema):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelMmxDataInsertMultipleTableSchema(ModelMmxDataInsertSingleTableSchema):
    data: List[ModelMmxDataInsertSingleTableSchema]
    n: int


ModelMmxDataSelectOutSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmxData, select_out_exclude
)
ModelMmxDataSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelMmxData, select_in_exclude, []
)


def single_table_multiple_require_select(
    model,
    schema,
    session: Session,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    single_table_multiple_require_select [特殊选择的表]

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


def single_table_condition_select(
    model,
    session: Session,
    condition: str = "",
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    single_table_condition_select [根据传入的条件进行查询]

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


def single_table_name_select(
    model,
    session: Session,
    name: str,
    physical: bool = False,
    offset_data: int = -1,
    limit_data: int = -1,
):
    """
    single_table_name_select [根据传入的条件进行查询]

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
