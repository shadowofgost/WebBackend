"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-02 17:50:22
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Depends.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-09 13:00:37
# @Software         : Vscode
"""
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

from Components.Exceptions import CredentialsError, IncorrectPassword, notAuthenticated
from Config import get_settings
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from loguru import logger
from passlib.context import CryptContext
from Services import SchemaUserPydantic, get_user_id, get_user_nouser
from sqlalchemy.orm import Session
from .Middleware import SessionLocal
pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/jwt/token")
settings= get_settings()


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


async def verity_password(plain_password: str, hashed_password: str):
    return plain_password == hashed_password


async def get_current_user(
    request: Request, token: str = Depends(oauth2_schema)
) -> SchemaUserPydantic:
    db = request.state.db
    try:
        payload = jwt.decode(
            token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
    except JWTError:
        raise CredentialsError
    id = payload.get("sub")
    if id is None:
        raise CredentialsError
    else:
        id_token = int(id)
        user = get_user_id(db, id_token)
        return user


async def authenticate_user(
    db: Session, nouser: str, password: str
) -> SchemaUserPydantic:
    user = get_user_nouser(db, nouser)
    result_verify = await verity_password(
        plain_password=password, hashed_password=user.Psw
    )
    if not result_verify:
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

## 以下是未使用的函数
async def request_info(request: Request):
    logger.bind(name=None).info(f"{request.method} {request.url}")
    try:
        body = await request.json()
        logger.bind(payload=body, name=None).debug("request_json: ")
    except:
        body = await request.body()
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
