"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/Public.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 14:47:31
# @LastAuthor       : Albert Wang
"""
from sqlmodel import (
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Unicode,
    BigInteger,
    Field,
    SQLModel,
)
from typing import Optional
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ModelPublic(SQLModel):
    __abstract__ = True
    ID: BigInteger = Field(
        Identity(start=1, increment=1), primary_key=True, nullable=False, index=True
    )
    Rem: Optional[Unicode] = Field(max_length=64)
    Introduction: Optional[Unicode] = Field(max_length=254)
    TimeUpdate: Optional[BigInteger] = Field(index=True)
    IdManager: Optional[BigInteger] = Field(index=True)
    IMark: Optional[Integer]
    back_up1: Optional[Unicode] = Field(max_length=254)
    back_up2: Optional[Unicode] = Field(max_length=254)
    back_up3: Optional[Unicode] = Field(max_length=254)
    back_up4: Optional[Integer]
    back_up5: Optional[Integer]
    back_up6: Optional[Integer]
