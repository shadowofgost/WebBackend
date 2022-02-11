"""
# @Time             : 2022-01-24 11:45:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Test.py
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-11 17:28:48
# @LastAuthor       : Albert Wang
"""
from attr import has
from src.Models import (
    ModelUserExtension,
    sqlalchemy_to_pydantic,
    ModelUser,
    ModelCoursePlan,
    ModelCurricula,
    ModelDepartment,
    ModelLocation,
    ModelRunningAccount,
    ModelCurriculaSelectInSingleTableSchema,
    ModelCurricula,
)
from src.Models.ModelCurricula import (
    ModelCurriculaSelectOutSingleTableSchemaBase,
    ModelCurriculaSelectOutSingleTableSchema,
    ModelCurriculaSelectInSingleTableSchema,
)
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    select,
    subquery,
    create_engine,
)
from src.Services import PublicService, ServiceCurricula
from sqlalchemy.orm import Session, sessionmaker, aliased
from time import time
from src.Config import get_settings
from Test2 import test_exception
from pydantic import create_model

settings = get_settings()


def test_model():
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    user1 = aliased(ModelUser)
    sub = (
        select(
            ModelRunningAccount,
            ModelRunningAccount.ID,
            ModelUser.Name.label("ID_User_Name"),
            ModelUser.NoUser.label("ID_User_NoUser"),
            user1.Name.label("ID_Manager_Name"),
        )
        .join(ModelUser, ModelRunningAccount.ID_User == ModelUser.ID)
        .join(user1, ModelRunningAccount.IdManager == user1.ID)
        .where(ModelRunningAccount.Type_field == 4097)
        .subquery()
    )
    """
    if hasattr(sub, "c"):
        a = sub.c.ID_Curricula_Name.like("%计算机%")
        stmt = select(sub).where(a)
    else:
        stmt = select(sub)
    """
    stmt = select(sub)
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
    result = session.execute(stmt).mappings().all()
    end = time()
    print(result)
    print(end - begin)


def test_model_name():
    test_schema = create_model(
        "test_schema",
        __base__=ModelCurriculaSelectInSingleTableSchema,
    )
    print(test_schema.__dict__)


test_model_name()
