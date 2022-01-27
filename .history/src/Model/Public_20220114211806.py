"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/Public.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 21:08:05
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

from pydantic import BaseConfig, BaseModel, create_model,Field
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty

Base = declarative_base()

class ModelPublic(Base):
    __abstract__ = True
    ID = Column(
        BigInteger,
        Identity(start=1, increment=1),
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
                title=None
                max_length=None
                if column.default is None and not column.nullable:
                    default = ...
                if column.doc is not None:
                    description=column.doc
                if column.comment is not None:
                    title=column.comment
                if hasattr(column.type, "length"):
                    max_length=column.type.length
                fields[name] =(python_type, Field(description=description, max_length=max_length,title=title,default=default))
    pydantic_model = create_model(
        db_model.__name__, __config__=config, **fields  # type: ignore
    )
    return pydantic_model
