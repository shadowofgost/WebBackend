"""
# @Time             : 2022-01-14 01:17:55
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelSqlAlchemySession.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 18:00:13
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import Column,Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from .PublicModel import ModelPublic

class ModelSqlAlchemySession(ModelPublic):
    __tablename__ = "sqlalchemy_session_table"
    session_key = Column(Unicode(40), primary_key=True, index=True)
    session_data = Column(Unicode, nullable=False, index=True)
    expire_date = Column(DATETIME2, nullable=False, index=True)
