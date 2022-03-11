# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Time             : 2022-01-24 11:45:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Test.py
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-03-11 20:14:45
# @LastAuthor       : Albert Wang
"""
from hashlib import algorithms_available
from Models import (
    ModelUserExtension,
    ModelUser,
    ModelCoursePlan,
    ModelCurricula,
    ModelDepartment,
    ModelLocation,
    ModelRunningAccount,
    ModelCurricula,
)
from Services.SchemaCurricula import (
    ModelCurriculaSelectOutSingleTableSchemaBase,
    ModelCurriculaSelectOutSingleTableSchema,
    ModelCurriculaSelectInSingleTableSchema,
)
from Services.SchemaRunningAccount import (
    ModelRunningAccountSelectOutSingleTableSchema,
)
from sqlalchemy import (
    select,
    create_engine,
)
from sqlalchemy.orm import Session, sessionmaker, aliased
from time import time
from Config import get_settings
from pydantic import create_model
from jose import JWTError, jwt
from fastapi_pagination import Params
settings = get_settings()


def test_model():
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    user1 = aliased(ModelUser)
    id_courseplan = 100
    range_users = [1717401034, 1717401055, 1717401081, 1917401001]
    sub_runningaccount = (
        select(ModelRunningAccount)
        .where(ModelRunningAccount.Type == 4097)
        .where(ModelRunningAccount.IMark == 0)
        .where(ModelRunningAccount.Param2 == id_courseplan)
        .subquery()  # type: ignore
    )
    sub_user = (
        select(ModelUser)
        .where(ModelUser.IMark == 0)
        .where(ModelUser.NoUser.in_(range_users))
        .subquery()  # type: ignore
    )
    stmt = select(
        sub_user.c.ID.label("ID_User_Back"),
        sub_user.c.Name.label("ID_User_Name"),
        sub_user.c.NoUser.label("ID_User_NoUser"),
        sub_runningaccount,
    ).join(sub_runningaccount, sub_runningaccount.c.ID_User == sub_user.c.ID)
    """
    if hasattr(sub, "c"):
        a = sub.c.ID_Curricula_Name.like("%计算机%")
        stmt = select(sub).where(a)
    else:
        stmt = select(sub)
    """
    sub2 = (
        select(ModelCoursePlan)
        .join(
            ModelCurricula,
            ModelCurricula.ID == ModelCoursePlan.ID_Curricula,
            isouter=True,
        )
        .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
        .join(
            ModelLocation, ModelLocation.ID == ModelCoursePlan.ID_Location, isouter=True
        )
    )
    print(stmt)
    begin = time()
    result = session.execute(stmt).scalars().all()
    end = time()
    print(result)
    print(ModelRunningAccountSelectOutSingleTableSchema.__dict__)
    print(end - begin)


def test_model_name():
    test_schema = create_model(
        "test_schema",
        __base__=ModelCurriculaSelectInSingleTableSchema,
    )
    print(test_schema.__dict__)


def jwt_test():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjExLCJleHAiOjE2NDY5OTMxODl9.g7xOy8IOJ_HEpT7INYUGXz-8Vv0xJBjq0ttGI7GedgM"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjExLCJleHAiOjE2NDY5OTUyMDJ9.YaSyMJC8WkxdWHfTD_N7RZAUWrGQ6FrJPXPDNuZg8a4"
    key = settings.SECRET_KEY
    algorithms = settings.ALGORITHM
    print("error")
    print(token)
    payload = jwt.decode(token=token, key=key, algorithms=algorithms)
    print("error")
param=Params(page=1,size=10)
print(param)
