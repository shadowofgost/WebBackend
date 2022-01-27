"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelPublic.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-24 22:36:32
# @LastAuthor       : Albert Wang
"""
from turtle import title
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
from sqlalchemy.ext.declarative import declarative_base
from typing import Container, Optional, Type
from time import time, localtime, mktime, struct_time, strptime, ctime
from pydantic import BaseConfig, BaseModel, create_model, Field
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import ColumnProperty

Base = declarative_base()


exclude = [
    "back_up1",
    "back_up2",
    "back_up3",
    "back_up4",
    "back_up5",
    "back_up6",
    "IMark",
]
nullable = ["Rem", "Introduction"]


class ModelPublic(Base):
    __abstract__ = True
    ID = Column(
        BigInteger,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False,
        index=True,
        comment="这是数据库id",
        doc="数据库ID字段，表示数据库唯一的值",
    )
    Rem = Column(Unicode(64), comment="备注", doc="备注,一般情况下备注为空")
    Introduction = Column(Unicode(254), comment="简介", doc="简介,一般是介绍表内容的")
    TimeUpdate = Column(
        BigInteger,
        index=True,
        comment="更新时间",
        doc="更新时间,记录最后更新时间；（2000-1-1 0:0:0 经过的秒）",
    )
    IdManager = Column(BigInteger, index=True, comment="最后操作的人的id", doc="最后操作的人的id")
    IMark = Column(
        Integer, index=True, comment="存在标记", doc="存在标记,表示记录是否删除一般删除是1,没删除是0  "
    )
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Unicode(254))
    back_up3 = Column(Unicode(254))
    back_up4 = Column(Integer)
    back_up5 = Column(Integer)
    back_up6 = Column(Integer)


class OrmConfig(BaseConfig):
    orm_mode = True


def sqlalchemy_to_pydantic(
    db_model: Type,
    config: Type = OrmConfig,
    exclude: Container[str] = [],
    nullable: Container[str] = ["*"],
) -> Type[BaseModel]:
    """
    sqlalchemy_to_pydantic [summary]

    [extended_summary]

    Args:
        db_model (Type): [description]
        config (Type, optional): [description]. Defaults to OrmConfig.
        exclude (Container[str], optional): [description]. Defaults to [].
        nullable (Container[str], optional): [description]. Defaults to ["*"].

    Returns:
        Type[BaseModel]: [description]
    """

    mapper = inspect(db_model)
    fields = {}
    for attr in mapper.attrs:
        if isinstance(attr, ColumnProperty):
            if attr.columns:
                name = attr.key
                if name in exclude:
                    continue
                column = attr.columns[0]
                python_type = None
                if hasattr(column.type, "impl"):
                    if hasattr(column.type.impl, "python_type"):
                        python_type = column.type.impl.python_type
                elif hasattr(column.type, "python_type"):
                    python_type = column.type.python_type
                ##assert python_type, f"Could not infer python_type for {column}"
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
                if nullable == ["*"]:
                    pass
                else:
                    if name in nullable:
                        pass
                    else:
                        python_type: type(python_type)
                        default = ...
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
