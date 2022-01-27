"""
# @Time             : 2022-01-14 01:17:55
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/Session.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-22 13:03:42
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
from .ModelPublic import ModelPublic


class DjangoSession(ModelPublic):
    __tablename__ = "django_session"
    session_key = Column(Unicode(40), primary_key=True, index=True)
    session_data = Column(Unicode, nullable=False, index=True)
    expire_date = Column(DATETIME2, nullable=False, index=True)
