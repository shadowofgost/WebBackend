"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 14:19:43
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Decorators.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 14:25:18
# @Software         : Vscode
"""
from .Exceptions import notAuthenticated
from functools import wraps


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if "user" in kwargs and kwargs["user"].is_authenticated:
            return await func(*args, **kwargs)
        raise notAuthenticated

    return wrapper
