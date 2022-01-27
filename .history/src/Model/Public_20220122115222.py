"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/Public.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-22 11:51:25
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
    insert,
    update,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from typing import Container, Optional, Type
from time import time, localtime, mktime, struct_time, strptime, ctime
from pydantic import BaseConfig, BaseModel, create_model, Field
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy.orm import Session, sessionmaker
from .ModelUser import ModelUser, ModelUserExtension


Base = declarative_base()


def format_current_time():
    base_time = mktime(strptime("2000-01-01 00:00:00", "%Y-%m-%d %X"))  ##设定标准或者说基础的时间
    current_time = mktime(localtime())  ##获取当前时间
    time_update = int(current_time - base_time)  ##计算时间差
    return time_update


exclude = ["back_up1", "back_up2", "back_up3", "back_up4", "back_up5", "back_up6"]
nullable = ["Rem"]

model_dict = {"ModelUser": {"model": ModelUser}}
error_database_execution = {"error": "database error"}

class ModelPublic(Base):
    __abstract__ = True
    ID = Column(
        BigInteger,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False,
        index=True,
    )
    Rem = Column(Unicode(64))
    Introduction = Column(Unicode(254))
    TimeUpdate = Column(BigInteger, index=True)
    IdManager = Column(BigInteger, index=True)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Unicode(254))
    back_up3 = Column(Unicode(254))
    back_up4 = Column(Integer)
    back_up5 = Column(Integer)
    back_up6 = Column(Integer)


class OrmConfig(BaseConfig):
    orm_mode = True


def sqlalchemy_to_pydantic(
    db_model: Type, *, config: Type = OrmConfig, exclude: Container[str] = []
) -> Type[BaseModel]:
    mapper = inspect(db_model)
    fields = {}
    for attr in mapper.attrs:
        if isinstance(attr, ColumnProperty):
            if attr.columns:
                name = attr.key
                if name in exclude:
                    continue
                column = attr.columns[0]
                python_type: Optional[type] = None
                if hasattr(column.type, "impl"):
                    if hasattr(column.type.impl, "python_type"):
                        python_type = column.type.impl.python_type
                elif hasattr(column.type, "python_type"):
                    python_type = column.type.python_type

                assert python_type, f"Could not infer python_type for {column}"
                default = None
                description = None
                comment = None
                max_length = None
                if column.default is None and not column.nullable:
                    default = ...
                if column.doc is not None:
                    description = column.doc
                if column.comment is not None:
                    comment = column.comment
                if hasattr(column.type, "length"):
                    max_length = column.type.length
                fields[name] = (
                    python_type,
                    Field(
                        description=description,
                        max_length=max_length,
                        comment=comment,
                        default=default,
                    ),
                )
    pydantic_model = create_model(
        db_model.__name__, __config__=config, **fields  # type: ignore
    )
    return pydantic_model


def execution(stmt, session: Session):
    try:
        session.execute(stmt)
        session.commit()
        session.flush()
        return {"msg": "execution success"}
    except Exception as e:
        session.rollback()
        return error_database_execution


def single_table_id_select(model, id, session: Session):
    stmt = select(model).where(model.id == id)
    try:
        result = session.execute(stmt).first()
        return result
    except Exception as e:
        return error_database_execution


def single_table_special_choice_select(
    model, schema, session: Session, offset_data: int = -1, limit_data: int = -1
):
    if limit_data == -1 or offset_data == -1:
        stmt = select(model).filter_by(**schema.dict())
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


def single_table_total_select(
    model, schema, session: Session, offset_data: int = -1, limit_data: int = -1
):
    if limit_data == -1 or offset_data == -1:
        stmt = select(model)
    else:
        stmt = select(model).offset(offset_data).limit(limit_data)

    try:
        result = session.execute(stmt).all()
    except Exception as e:
        return error_database_execution


def single_insert(model, schema, session: Session):
    stmt = insert(model).values(**schema.dict())
    return execution(stmt, session)


def multiple_insert(model, multiSchema, session: Session):
    mappings = [multiSchema.data[i].dict() for i in range(multiSchema.n)]
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


def multiple_update(model, multiSchema, session: Session):
    mappings = [multiSchema.data[i].dict() for i in range(multiSchema.n)]
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


def multiple_delete(model, multiSchema, session: Session):
    mappings = [
        {
            "id": multiSchema.data[i].id,
            "TimeUpdate": multiSchema.data[i].TimeUpdate,
            "IMark": 1,
        }
        for i in range(multiSchema.n)
    ]
    try:
        session.bulk_update_mappings(model, mappings)
        session.commit()
        session.flush()
        return {"msg": " execution success"}
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
            self.delete_schema = model_dict[model]["delete_schema"]
            self.insert_schema = model_dict[model]["insert_schema"]
            self.update_schema = model_dict[model]["update_schema"]
            self.select_schema = model_dict[model]["select_schema"]
            self.delete_multiple_schema = model_dict[model]["delete_multiple_schema"]
            self.insert_multiple_schema = model_dict[model]["insert_multiple_schema"]
            self.update_multiple_schema = model_dict[model]["update_multiple_schema"]
            self.select_multiple_schema = model_dict[model]["select_multiple_schema"]

    def id_select(self, id, physical=False, offset_data=-1, limit_data=-1):
        if self.abstract_model == True:
            return self.model.id_select(id, physical, offset_data, limit_data)
        else:
            if physical == True:
                return single_table_id_select(self.model, id, self.session)
            else:
                return model_dict[self.model]["id_select"](self.model, id, self.session)

    def total_select(self, physical=False, offset_data=-1, limit_data=-1):
        if self.abstract_model == True:
            return self.model.total_select(physical,offset_data, limit_data)
        else:
            if physical== True:
                return single_table_total_select(self.model, self.session, offset_data, limit_data)
            return model_dict[self.model]["total_select"](
                self.model, self.session, offset_data, limit_data
            )

    def special_choice_select(
        self, schema, physical=False, offset_data=-1, limit_data=-1
    ):
        if self.abstract_model == True:
            return self.model.table_special_choice_select(offset_data, limit_data)
        else:
            return model_dict[self.model]["tabel_special_choice_select"](
                self.model, schema, self.session, offset_data, limit_data
            )

    """
    def singletable_id_select(self, id):
        if self.abstract_model == True:
            raise error
        else:
            return singletable_id_select(self.model, id, self.session)

    def singletable_special_choice_select(self, offset_data = -1, limit_data = -1):
        if self.abstract_model == True:
            raise error
        else:
            return singletable_special_choice_select(self.model, self.schema, self.session, offset_data, limit_data)

    def singletable_total_select(self, offset_data = -1, limit_data = -1):
        if self.abstract_model == True:
            raise error
        else:
            return singletable_total_select(self.model, self.schema, self.session, offset_data, limit_data)
    """

    def insert(
        self,
        schema=None,
        multiple_schema=None,
        multiple: bool = False,
        physical: bool = False,
    ):
        try:
            insert_schema = self.insert_schema(**self.schema.dict())
        except Exception as e:
            return error

        if self.abstract_model == True:
            return self.model.insert()
        else:
            if self.multiple == True:
                return multiple_insert(self.model, insert_schema, self.session)
            else:
                return single_insert(self.model, self.schema, self.session)

    def update(
        self,
        schema=None,
        multiple_schema=None,
        multiple: bool = False,
        physical: bool = False,
    ):
        try:
            update_schema = self.update_schema(**self.schema.dict())
        except Exception as e:
            return error

        if self.abstract_model == True:
            return self.model.update()
        else:
            if self.multiple == True:
                return multiple_update(self.model, update_schema, self.session)
            else:
                return single_update(self.model, update_schema, self.session)

    def delete(
        self,
        schema=None,
        multiple_schema=None,
        multiple: bool = False,
        physical: bool = False,
    ):
        try:
            delete_schema = self.delete_schema(**self.schema.dict())
        except Exception as e:
            return error

        if self.abstract_model == True:
            return self.model.delete()
        else:
            if self.multiple == True:
                return multiple_delete(self.model, delete_schema, self.session)
            else:
                return single_delete(self.model, delete_schema, self.session)
