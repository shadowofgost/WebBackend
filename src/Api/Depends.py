# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-02 17:50:22
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Depends.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 21:03:19
# @Software         : Vscode
"""
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

import loguru

from Components import CredentialsError, IncorrectPassword, notAuthenticated
from Config import get_settings
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from loguru import logger
from passlib.context import CryptContext
from Services import SchemaUserPydantic, get_user_id, get_user_nouser
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")
settings = get_settings()
authenticate_path_dict = {
    1: {"*": {"*"}},
    2: {
        "/model_curricula/search": ["POST"],
        "/model_courseplan/search": ["POST"],
        "/model_runningaccount/result": ["POST"],
        "/model_runningaccount/": ["POST", "PUT"],
        "/model_user/current_user": ["GET"],
        "/model_user/": ["PUT"],
        "/model_userextension/search": ["GET"],
        "/model_userextension/": ["PUT"],
    },
    3: {
        "/model_curricula/search": ["POST"],
        "/model_courseplan/search": ["POST"],
        "/model_runningaccount/result": ["POST"],
        "/model_user/current_user": ["GET"],
        "/model_user/": ["PUT"],
        "/model_userextension/search": ["GET"],
        "/model_userextension/": ["PUT"],
    },
}  ##权限路径控制系统，控制不同权限能使用的路径示意。


async def get_db(request: Request):
    return request.state.db


"""
async def depends_get_db():
    session = SessionLocal()
    try:
        db = session
        yield db
    finally:
        db.close()
"""


async def verify_password(plain_password: str, hashed_password: str):
    return plain_password == hashed_password


async def hashed_verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def verity_authenticate_path(path: str, method: str, user: SchemaUserPydantic):
    authenticate_path = authenticate_path_dict[user.Attr]
    path_list = authenticate_path.keys()
    if user.Attr == 1:
        pass
    else:
        if path not in path_list:
            logger.error("用户没有权限")
            raise notAuthenticated
        else:
            methods_list = authenticate_path_dict[user.Attr][path]
            if method not in methods_list:
                logger.error("用户没有权限")
                raise notAuthenticated
            else:
                pass


async def authenticate_user(
    db: Session, nouser: str, password: str
) -> SchemaUserPydantic:
    user = get_user_nouser(db, nouser)
    result_verify = await verify_password(
        plain_password=password, hashed_password=user.Psw
    )
    if not result_verify:
        logger.error("用户输入的密码不正确")
        raise IncorrectPassword
    return user


async def created_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + settings.TOKEN_EXPIRE_MINUTES
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(
    request: Request, token=Depends(oauth2_schema)
) -> SchemaUserPydantic:
    db = request.state.db
    try:
        payload = jwt.decode(
            token=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
    except JWTError:
        logger.error("用户没有登录，token缺失")
        raise CredentialsError
    id = payload.get("sub")
    id_token = int(id)
    user = get_user_id(db, id_token)
    await verity_authenticate_path(request.url.path, request.method, user)  ##控制使用权限
    return user


## 以下是未使用的函数


async def request_info(request: Request):
    logger.bind(name=None).info(f"{request.method} {request.url}")
    try:
        body = await request.json()
        logger.bind(payload=body, name=None).debug("request_json: ")
    except:
        try:
            body = await request.body()
        except:
            try:
                body = await request.form()
            except:
                body = "无法获取提交的信息"
    if len(body) != 0:
        # 有请求体，记录日志
        logger.bind(payload=body, name=None).debug(body)


async def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if "user" in kwargs:
            return await func(*args, **kwargs)
        raise notAuthenticated

    return wrapper
