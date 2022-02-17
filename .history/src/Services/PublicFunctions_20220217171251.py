"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:02:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/PublicFunctions.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 17:04:03
# @Software         : Vscode
"""
from time import ctime, localtime, mktime, strptime, struct_time, time
from typing import Container, Optional, Type
from pydantic import BaseConfig, BaseModel, Field, create_model
from sqlalchemy.ext.declarative import declarative_base
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
update_exclude = exclude[:]
update_exclude.extend(["TimeUpdate", "IdManager"])
insert_exclude = update_exclude[:]
insert_exclude.extend(["ID"])
select_out_exclude = exclude[:-1]
select_in_exclude = exclude[:]

nullable = ["Rem", "Introduction"]


def format_current_time():
    base_time = mktime(strptime("2000-01-01 00:00:00", "%Y-%m-%d %X"))  ##设定标准或者说基础的时间
    current_time = mktime(localtime())  ##获取当前时间
    time_update = int(current_time - base_time)  ##计算时间差
    return time_update
class OrmConfig(BaseConfig):
    orm_mode = True


def sqlalchemy_to_pydantic(
    db_model: Type,
    exclude: Container[str] = [],
    nullable: Container[str] = ["*"],
    config: Type = OrmConfig,
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
                title = None
                max_length = None
                if column.default is None and not column.nullable:
                    default = ...
                if column.doc is not None:
                    description = column.doc
                if column.comment is not None:
                    title = column.comment
                if hasattr(column.type, "length"):
                    max_length = column.type.length
                if nullable == ["*"]:
                    pass
                elif nullable == []:
                    python_type: Optional[type(python_type)]
                    default = None
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
                        title=title,
                        default=default,
                    ),
                )
    pydantic_model = create_model(
        db_model.__name__, __config__=config, **fields  # type: ignore
    )
    return pydantic_model
