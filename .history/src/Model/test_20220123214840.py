"""
# @Time             : 2022-01-14 01:00:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/test.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-23 21:38:39
# @LastAuthor       : Albert Wang
"""
import time

print(time.time())
from sqlalchemy import select
from ModelUser import ModelUser
from pydantic import BaseModel, Field
from typing import Container, Optional, Type

stmt = select(ModelUser.Name.label("test")).where(ModelUser.Name.like("%a%"))
print(type(stmt))
print(stmt)
print(type(select()))


class test(BaseModel):
    id: int
    name: str = "nihao"
    age: Optional[int] = 1

class test_2(test):
    id:int=1
test1 = test(id=1)
test2 = test(id=2, name="test")
test3 = test(id=3, name="test", age=None)
print(test.__dict__)
print(test1)
print(test2)
print(test3)
print(test_2.__dict__)
