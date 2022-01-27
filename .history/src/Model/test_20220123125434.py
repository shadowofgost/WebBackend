"""
# @Time             : 2022-01-14 01:00:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/test.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-23 12:45:33
# @LastAuthor       : Albert Wang
"""
import time

print(time.time())
from sqlalchemy.s
from ModelUser import ModelUser

stmt = select(ModelUser).where(eval(""), ModelUser.IMark == 0)
print(type(stmt))
print(type(select()))
