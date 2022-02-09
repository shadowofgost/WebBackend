"""
# @Time             : 2022-01-24 11:45:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Test_pydantic_to_sqlalchemy.py
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 16:40:29
# @LastAuthor       : Albert Wang
"""
from src.Models import (
    ModelUserExtension,
    sqlalchemy_to_pydantic,
    ModelUser,
    ModelCoursePlan,
    ModelCurricula,
    ModelDepartment,
    ModelLocation,
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
)
from src.Config.Settings import SessionLocal
from time import time
session = SessionLocal()
sub = (
    select(ModelCoursePlan)
    .join(
        ModelCurricula, ModelCurricula.ID == ModelCoursePlan.ID_Curricula, isouter=True
    )
    .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
    .join(ModelLocation, ModelLocation.ID == ModelCoursePlan.ID_Location, isouter=True)
).subquery()
stmt = select(sub).filter_by(ID=23)
sub2 = (
    select(ModelCoursePlan)
    .join(
        ModelCurricula, ModelCurricula.ID == ModelCoursePlan.ID_Curricula, isouter=True
    )
    .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
    .join(ModelLocation, ModelLocation.ID == ModelCoursePlan.ID_Location, isouter=True)
)
##print(stmt)
result = session.execute(sub2).
begin=time()
print(result)
end=time()
print(end-begin)
