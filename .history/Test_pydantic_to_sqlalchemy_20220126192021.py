"""
# @Time             : 2022-01-24 11:45:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Test_pydantic_to_sqlalchemy.py
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-26 19:17:47
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
from src.Core.Settings import SessionLocal
from time import time

session = SessionLocal()
sub = (
    select(
        ModelCoursePlan,
        ModelCurricula.Name.label("ID_Curricula_Name"),
        ModelLocation.Name.label("ID_Location_Name"),
        ModelUser.Name.label("ID_Speaker_Name"),
    )
    .join(
        ModelCurricula,
        ModelCurricula.ID == ModelCoursePlan.ID_Curricula,
        isouter=True,
    )
    .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
    .join(
        ModelLocation,
        ModelLocation.ID == ModelCoursePlan.ID_Location,
        isouter=True,
    )
).subquery()
print(sub
stmt = select(sub).where(sub.selected_columns == 1)
print(type(stmt))
sub2 = (
    select(ModelCoursePlan)
    .join(
        ModelCurricula, ModelCurricula.ID == ModelCoursePlan.ID_Curricula, isouter=True
    )
    .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
    .join(ModelLocation, ModelLocation.ID == ModelCoursePlan.ID_Location, isouter=True)
)
if hasattr(sub2, "c"):
    print(sub2.c)
##print(stmt)
result = session.execute(sub2).mappings().all()
begin = time()
print(result)
end = time()
print(end - begin)
