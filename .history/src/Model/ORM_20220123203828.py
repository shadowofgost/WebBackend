"""
# @Time             : 2022-01-22 14:17:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/ORM.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-23 20:38:07
# @LastAuthor       : Albert Wang
"""
from http.server import executable
from typing import Container, Optional, Type
from sqlalchemy import create_engine, delete, insert, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from ModelUser import ModelUser, ModelUserExtension
from ModelTypera import ModelTypera
from ModelTableInformation import ModelTableInformation
from ModelRunningAccount import ModelRunningAccount
from ModelMmx import ModelMmx,ModelMmxData
from ModelLocation import ModelLocation, ModelLocationExtension
from ModelEquipment import ModelEquipment
from ModelDepartment import ModelDepartment
from ModelCurricula import ModelCurricula

from pydantic import BaseModel

model_dict = {"ModelUser": {"model": ModelUser,"delete_single_schema","insert_single_schema","update_single_schema","select_single_schema","delete_multiple_schema","insert_multiple_schema","update_multiple_schema","select_multiple_schema"}}
name_column_model_dict = {}
error_database_execution = {"error": "database error"}
error_schema_validation = {"error": "schema validation error"}
Base = declarative_base()
session = 1
stmt_format = type(select())
## 所有查询的默认前提条件是接收到的数据不包含IMark字段的数据
def execution(stmt, session: Session) -> dict:
    """
    execution  [执行的查询语言]

    [根据传入的参数进行查询]

    Args:
        stmt ([type]): [需要执行的stmt语句]
        session (Session): [数据库执行所需要的链接]

    Returns:
        dict: [返回执行结果成功或者失败的信息]
    """
    try:
        session.execute(stmt)
        session.commit()
        session.flush()
        return {"msg": "execution success"}
    except Exception as e:
        session.rollback()
        return error_database_execution


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
    if limit_data == -1 or offset_data == -1:
        if physical == False:
            schema_dict = schema.dict()
            schema_dict["IMark"] = 0
            stmt = select(model).filter_by(**schema_dict)
        else:
            stmt = select(model).filter_by(**schema.dict())
    else:
        if physical == False:
            schema_dict = schema.dict()
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
    single_table_condition_select [根据传入的条件进行查询]

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
    name= "%"+name+"%"
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


def single_insert(model, schema, session: Session):
    stmt = insert(model).values(**schema.dict())
    return execution(stmt, session)


def multiple_insert(model, multiple_schema, session: Session):
    mappings = [multiple_schema.data[i].dict() for i in range(multiple_schema.n)]
    try:
        session.bulk_insert_mappings(model, mappings)
        session.commit()
        session.flush()
        return {"msg": "success"}
    except Exception as e:
        session.rollback()
        return error_database_execution


def single_update(model, schema, session: Session):
    stmt = update(model).where(model.id == schema.id).values(**schema.dict())
    return execution(stmt, session)


def multiple_update(model, multiple_schema, session: Session):
    mappings = [multiple_schema.data[i].dict() for i in range(multiple_schema.n)]
    try:
        session.bulk_update_mappings(model, mappings)
        session.commit()
        session.flush()
        return {"msg": "success"}
    except Exception as e:
        session.rollback()
        return error_database_execution


def single_delete(model, schema, session: Session):
    stmt = (
        update(model)
        .where(model.id == schema.id)
        .values(IMark=1, TimeUpdate=schema.TimeUpdate)
    )
    return execution(stmt, session)


def single_delete_physical(model, schema, session: Session):
    stmt = delete(model).where(model.id == schema.id)
    return execution(stmt, session)


def multiple_delete(model, multiple_schema, session: Session):
    mappings = [
        {
            "id": multiple_schema.data[i].id,
            "TimeUpdate": multiple_schema.data[i].TimeUpdate,
            "IMark": 1,
        }
        for i in range(multiple_schema.n)
    ]
    try:
        session.bulk_update_mappings(model, mappings)
        session.commit()
        session.flush()
        return {"msg": " execution success"}
    except Exception as e:
        session.rollback()
        return error_database_execution


def multiple_delete_physical(model, multiple_schema, session: Session):
    try:
        for i in range(multiple_schema.n):
            stmt = delete(model).where(model.id == multiple_schema.data[i].id)
            session.execute(stmt)
        session.commit()
        session.flush()
        return {"msg": "execution success"}
    except Exception as e:
        session.rollback()
        return error_database_execution


def get_session():
    SQLALCHEMY_DATABASE_URL = (
        "mysql+pymysql://web:123456@101.132.135.180:3306/LiveStream?"
    )
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


class ORM:
    def __init__(
        self, model: str, session: Session = None, abstract_model: bool = False
    ):
        """
        __init__ORM初始化,用于初始化具体的表的增删改查操作

        [extended_summary]

        Args:
            model (str): [表名，或者说model名，必须存在在model_dict中]
            session (Session, optional): [启动用于提交的数据库session]. Defaults to None.
            abstract_model (bool, optional): [是否是抽象的表，比如水平分表的总和抽象表，比如User表]. Defaults to False.
        """
        if session == None:
            self.session = get_session()
        else:
            self.session = session
        if abstract_model == True:
            self.model = model_dict[model]["model"](model, session=self.session)
            self.abstract_model = abstract_model
        else:
            self.abstract_model = abstract_model
            self.model = model_dict[model]["model"]
            self.delete_single_schema = model_dict[model]["delete_single_schema"]
            self.insert_single_schema = model_dict[model]["insert_single_schema"]
            self.update_single_schema = model_dict[model]["update_single_schema"]
            self.select_single_schema = model_dict[model]["select_single_schema"]
            self.delete_multiple_schema = model_dict[model]["delete_multiple_schema"]
            self.insert_multiple_schema = model_dict[model]["insert_multiple_schema"]
            self.update_multiple_schema = model_dict[model]["update_multiple_schema"]
            self.select_multiple_schema = model_dict[model]["select_multiple_schema"]

    def multiple_require_select(
        self,
        schema,
        service: bool = True,
        physical: bool = False,
        offset_data: int = -1,
        limit_data: int = -1,
    ):
        """
        multiple_require_select [特殊选择查询]

        [针对一系列要求的值对表进行的查询]

        Args:
            schema ([type]): [接受的表，比如user的schema，id=1，name=。。。。]
            service (bool, optional): [表示是否是业务查询，默认是True表示默认是提供业务形式的查询结果，False表示直接提供表结构的查询结果]. Defaults to True.
            physical (bool, optional): [显示的是逻辑表还是物理表，False表示逻辑表，True表示物理表]. Defaults to False.
            offset_data (int, optional): [sql中的偏移量，从偏移量+1的位置开始选择数据，实现分页功能]. Defaults to -1.
            limit_data (int, optional): [sql中选择的数据总数，表示每一页数据的总的个数]. Defaults to -1.

        Returns:
            [dict]: [返回的是列表形式的值，报错或者查询结果参数]
        """
        if self.abstract_model == True:
            return self.model.multiple_require_select(
                schema, physical, offset_data, limit_data
            )
        else:
            try:
                select_schema = self.select_single_schema(**schema.dict())
            except Exception as e:
                return error_schema_validation
            if service == True:
                return model_dict[self.model]["multiple_require_select"](
                    self.model,
                    select_schema,
                    self.session,
                    physical,
                    offset_data,
                    limit_data,
                )
            else:
                return single_table_multiple_require_select(
                    self.model,
                    select_schema,
                    self.session,
                    physical,
                    offset_data,
                    limit_data,
                )

    def condition_select(
        self,
        condition: str = "",
        service: bool = True,
        physical: bool = False,
        offset_data: int = -1,
        limit_data: int = -1,
    ):
        """
        condition_select [根据传入的条件进行查询]

        [根据传入的参数condition进行查询，condition的格式为：str，举例为：“ModelUser.id>=1,ModelUser.sex==2”这种,如果没有传入参数condition或者传入的是“”，那么查询所有值]

        Args:
            condition (str, optional): [传入的参数]. Defaults to "".
            service (bool, optional): [表示是否是业务查询，默认是True表示默认是提供业务形式的查询结果，False表示直接提供表结构的查询结果]. Defaults to True.
            physical (bool, optional): [显示的是逻辑表还是物理表，False表示逻辑表，True表示物理表]. Defaults to False.
            offset_data (int, optional): [sql中的偏移量，从偏移量+1的位置开始选择数据，实现分页功能]. Defaults to -1.
            limit_data (int, optional): [sql中选择的数据总数，表示每一页数据的总的个数]. Defaults to -1.

        Returns:
            [type]: [description]
        """
        if self.abstract_model == True:
            return self.model.condition_select(
                condition, service, physical, offset_data, limit_data
            )
        else:
            if service == True:
                return model_dict[self.model]["condition_select"](
                    self.model,
                    self.session,
                    condition,
                    physical,
                    offset_data,
                    limit_data,
                )
            else:
                return single_table_condition_select(
                    self.model,
                    self.session,
                    condition,
                    physical,
                    offset_data,
                    limit_data,
                )
    def name_select(
        self,
        name: str,
        service: bool = True,
        physical: bool = False,
        offset_data: int = -1,
        limit_data: int = -1,
    ):
        """
        condition_select [根据传入的条件进行查询]

        [根据传入的参数condition进行查询，condition的格式为：str，举例为：“ModelUser.id>=1,ModelUser.sex==2”这种,如果没有传入参数condition或者传入的是“”，那么查询所有值]

        Args:
            name(str, optional): [传入的name字符串,进行匹配查询name].
            service (bool, optional): [表示是否是业务查询，默认是True表示默认是提供业务形式的查询结果，False表示直接提供表结构的查询结果]. Defaults to True.
            physical (bool, optional): [显示的是逻辑表还是物理表，False表示逻辑表，True表示物理表]. Defaults to False.
            offset_data (int, optional): [sql中的偏移量，从偏移量+1的位置开始选择数据，实现分页功能]. Defaults to -1.
            limit_data (int, optional): [sql中选择的数据总数，表示每一页数据的总的个数]. Defaults to -1.

        Returns:
            [type]: [description]
        """
        if self.abstract_model == True:
            return self.model.condition_select(
                condition, service, physical, offset_data, limit_data
            )
        else:
            if service == True:
                return model_dict[self.model]["condition_select"](
                    self.model,
                    self.session,
                    condition,
                    physical,
                    offset_data,
                    limit_data,
                )
            else:
                return single_table_condition_select(
                    self.model,
                    self.session,
                    condition,
                    physical,
                    offset_data,
                    limit_data,
                )
    def insert(
        self,
        schema,
        multiple: bool = False,
    ):
        """
        insert [插入数据]

        [插入增加新的数据]

        Args:
            schema ([type]): [表示插入提交的表单数据]. Defaults to None.
            multiple (bool, optional): [判断是否是批量插入，如果是False表示不是批量插入，只是增加一个数据，如果是True表示是批量插入]. Defaults to False.

        Returns:
            [type]: [description]
        """

        if self.abstract_model == True:
            return self.model.insert(schema, multiple)
        else:
            if multiple == True:
                try:
                    insert_schema = self.insert_multiple_schema(**schema.dict())
                except Exception as e:
                    return error_schema_validation
                return multiple_insert(self.model, insert_schema, self.session)
            else:
                try:
                    insert_schema = self.insert_single_schema(**schema.dict())
                except Exception as e:
                    return error_schema_validation
                return single_insert(self.model, insert_schema, self.session)

    def update(
        self,
        schema,
        multiple: bool = False,
    ):
        """
        update [修改数据]

        [修改现有的数据]

        Args:
            schema ([type]): [表示插入提交的表单数据]. Defaults to None.
            multiple (bool, optional): [判断是否是批量插入，如果是False表示不是批量插入，只是增加一个数据，如果是True表示是批量插入]. Defaults to False.

        Returns:
            [type]: [description]
        """
        if self.abstract_model == True:
            return self.model.update(schema, multiple)
        else:
            if multiple == True:
                try:
                    update_schema = self.update_multiple_schema(**schema.dict())
                except Exception as e:
                    return error_schema_validation
                return multiple_update(self.model, update_schema, self.session)
            else:
                try:
                    update_schema = self.insert_single_schema(**schema.dict())
                except Exception as e:
                    return error_schema_validation
                return single_update(self.model, update_schema, self.session)

    def delete(
        self,
        schema,
        multiple: bool = False,
        physical: bool = False,
    ):
        """
        delete [删除数据]

        [extended_summary]

        Args:
            schema ([type]): [表示插入提交的表单数据]. Defaults to None.
            multiple (bool, optional): [判断是否是批量插入，如果是False表示不是批量插入，只是增加一个数据，如果是True表示是批量插入]. Defaults to False.
            physical (bool, optional): [表示是否是物理删除数据，False表示非物理删除是逻辑删除，True表示是物理删除]. Defaults to False.

        Returns:
            [type]: [description]
        """
        if self.abstract_model == True:
            return self.model.delete(schema, multiple, physical)
        else:
            if multiple == True:
                try:
                    delete_schema = self.delete_multiple_schema(**schema.dict())
                except Exception as e:
                    return error_schema_validation
                if physical == True:
                    return multiple_delete_physical(
                        self.model, delete_schema, self.session
                    )
                else:
                    return multiple_delete(self.model, delete_schema, self.session)
            else:
                try:
                    delete_schema = self.delete_single_schema(**schema.dict())
                except Exception as e:
                    return error_schema_validation
                if physical == True:
                    return single_delete_physical(
                        self.model, delete_schema, self.session
                    )
                else:
                    return single_delete(self.model, delete_schema, self.session)
