"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/Public.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-22 10:52:38
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
)
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.ext.declarative import declarative_base
from typing import Container, Optional, Type
from time import time,localtime,mktime,struct_time,strptime,ctime
from pydantic import BaseConfig, BaseModel, create_model,Field
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update

Base = declarative_base()
def format_current_time():
    base_time=mktime(strptime('2000-01-01 00:00:00', '%Y-%m-%d %X'))##设定标准或者说基础的时间
    current_time=mktime(localtime())##获取当前时间
    time_update=int(current_time-base_time)##计算时间差
    return time_update
exclude=["back_up1","back_up2","back_up3","back_up4","back_up5","back_up6"]
nullable=["Rem"]
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
                description=None
                comment=None
                max_length=None
                if column.default is None and not column.nullable:
                    default = ...
                if column.doc is not None:
                    description=column.doc
                if column.comment is not None:
                    comment=column.comment
                if hasattr(column.type, "length"):
                    max_length=column.type.length
                fields[name] =(python_type, Field(description=description, max_length=max_length,comment=comment,default=default))
    pydantic_model = create_model(
        db_model.__name__, __config__=config, **fields  # type: ignore
    )
    return pydantic_model

def execution(stmt, session : Session):
    try:
        session.execute(stmt)
        session.commit()
        session.flush()
        return {'msg' : 'execution success'}
    except Exception as e:
        session.rollback()
        return {'error' : 'execution error, database error'}

def id_select(model, id, session : Session):
    stmt = select(model).where(model.id == id)
    try:
        result = session.execute(stmt).first()
        return result
    except Exception as e:
        return {'error' : 'database error'}

def special_choice_select(model, schema, session : Session):
    stmt = select(model).filter_by(**schema.dict())
    try:
        result = session.execute(stmt).all()
        return result
    except Exception as e:
        return {'error' : 'database error'}

def single_insert(model, schema, session : Session):
    stmt = insert(model).values(**schema.dict())
    return execution(stmt, session)

def multiple_insert(model, multiSchema, session : Session):
    mappings = [multiSchema.data[i].dict() for i in range(multiSchema.n)]
    try:
        session.bulk_insert_mappings(model, mappings)
        session.commit()
        session.flush()
        return {'msg' : 'success'}
    except Exception as e:
        session.rollback()
        return {'error' : 'execution error, database error'}

def single_update(model, schema, session : Session):
    stmt = update(model).where(model.id == schema.id).values(**schema.dict())
    return execution(stmt, session)

def multiple_update(model, multiSchema, session : Session):
    mappings = [multiSchema.data[i].dict() for i in range(multiSchema.n)]
    try:
        session.bulk_update_mappings(model, mappings)
        session.commit()
        session.flush()
        return {'msg' : 'success'}
    except Exception as e:
        session.rollback()
        return {'error' : 'execution error, database error'}

def single_delete(model, schema, session : Session):
    stmt = update(model).where(model.id == schema.id).values(IMark = 1, TimeUpdate = schema.TimeUpdate)
    return execution(stmt, session)

def multiple_delete(model, multiSchema, session : Session):
    mappings = [{'id' : multiSchema.data[i].id,
                 'TimeUpdate' : multiSchema.data[i].TimeUpdate,
                 'IMark' : 1}
                 for i in range(multiSchema.n)]
    try:
        session.bulk_update_mappings(model, mappings)
        session.commit()
        session.flush()
        return {'msg' : ' execution success'}
    except Exception as e:
        session.rollback()
        return {'error' : 'execution error, database error'}

def get_session():
    pass
model_dict={}
class ORM:
    def __init__(self, model : str, schema = None, multiple_schema = None, session : Session=None,
                  multiple : bool = False, physical:bool = False, abstract_model :bool=False):
        if session == None:
            self.session = get_session()
        else:
            self.session = session
        if abstract_model == True:
            self.model = model_dict.get(model)
        else:
            self.model = model_dict.get(model).get("model")
            if multiple == False:
                self.delete_schema = model_dict.get(model).get("delete_schema")
                self.insert_schema = model_dict.get(model).get("insert_schema")
                self.update_schema = model_dict.get(model).get("update_schema")
                self.select_schema = model_dict.get(model).get("select_schema")
            else:
                self.delete_schema = model_dict.get(model).get("delete_multiple_schema")
                self.insert_schema = model_dict.get(model).get("insert_multiple_schema")
                self.update_schema = model_dict.get(model).get("update_multiple_schema")
                self.select_schema = model_dict.get(model).get("select_multiple_schema")
        if multiple == True:
            self.schema = multiple_schema
        else:
            self.schema = schema
        if multiple == True and multiple_schema == None:
            raise error

    def special_choice_select(self, offset_data = -1, limit_.data = -1):
        if self.abstract_model == True:
            return self.model.table_special_choice_select(offset_data, limit_data)
        else:
            return model_list.get(self.model).get('tabel_special_choice_select')(self.model, self.schema, self.session, offset_data, limit_data)

    def total_select(self, offset_data = -1, limit_data = -1):
        if self.abstract_model == True:
            return self.model.total_select(offset_data, limit_data)
        else:
            return self.model_list.get(self.model).get('total_select')(self.model, self.schema, self.session, offset_data, limit_data)

    def id_select(self, id):
        if self.abstract_model == True:
            return self.model.id_select(id):
        else:
            return model_list.get(self.model).get('id_select')(self.model, id, self.session)

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

    def insert(self):
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

    def update(self,multiple : bool = False, physical:bool = False, ):
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


    def delete(self):
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

    def singletable_special_choice_select(model, schema, session : Session, offset_data : int = -1, limit_data : int = -1):
        if limit_data == -1 or offset_data == -1:
            stmt = select(model).filter_by(**schema.dict())
        else:
            stmt = select(model).filter_by(**schema.dict()).offset(offset_data).limit(limit_data)

        try:
            result = session.execute(stmt).all()
            return result
        except Exception as e:
            return {"error" : "database error"}

    def singletabel_total_select(model, schema, session : Session, offset_data : int = -1, limit_data : int = -1):
        if limit_data == - 1 or offset_data == -1:
            stmt = select(model)
        else:
            stmt = select(model).offset(offset_data).limit(limit_data)

        try:
            result = session.execute(stmt).all()
        except Exception as e:
            return {"error" : "database error"}
