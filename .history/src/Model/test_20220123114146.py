"""
# @Time             : 2022-01-14 01:00:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/test.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-23 11:31:46
# @LastAuthor       : Albert Wang
"""
import time

print(time.time())
from sqlalchemy import select
from ModelUser import ModelUser

stmt = select(ModelUser)
print(type(stmt))
print(type(select()))
