# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-03-17 15:58:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/UpdateDataBase.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-17 17:22:10
# @Software         : Vscode
"""
from unittest import result
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from Config import get_settings
from fastapi import Request, Response
from Models import ModelCurricula, ModelCoursePlan


def update_database():
    webbackend = (
        "mysql+pymysql://web:123456@101.132.135.180:3306/WebBackend?charset=utf8"
    )
    backup = "mysql+pymysql://web:123456@101.132.135.180:3306/Backup?charset=utf8"
    sqlserver = "mssql+pymssql://web:123456@localhost:2233/CyWz?charset=utf8"
    url_list = [sqlserver, backup, webbackend]
    session_list = []
    for i in url_list:
        engine = create_engine(i)
        SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
        session = SessionLocal()
        session_list.append(session)
    stmt = select(
        ModelCurricula.ID, ModelCurricula.RangeEqus, ModelCurricula.RangeUsers
    )
    session = session_list[0]
    result_curricula = session.execute(stmt).mappings().all()
    stmt = select(
        ModelCoursePlan.ID, ModelCoursePlan.RangeEqus, ModelCoursePlan.RangeUsers
    )
    result_courseplan = session.execute(stmt).mappings().all()
    mappings_curricula = [
        {"ID": i["ID"], "RangeUsers": i["RangeUsers"], "RangeEqus": i["RangeEqus"]}
        for i in result_curricula
    ]
    mappings_courseplan = [
        {"ID": i["ID"], "RangeUsers": i["RangeUsers"], "RangeEqus": i["RangeEqus"]}
        for i in result_courseplan
    ]
    for i in range(1, len(session_list)):
        session = session_list[i]
        session.bulk_update_mappings(ModelCurricula, mappings_curricula)
        session.bulk_update_mappings(ModelCoursePlan, mappings_courseplan)
        session.commit()
        session.flush()


update_database()
