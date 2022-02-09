"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-02 17:50:22
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Depends.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-07 15:01:48
# @Software         : Vscode
"""
from ..Core import SessionLocal

error_get_connect_database = {}


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_user():
    
