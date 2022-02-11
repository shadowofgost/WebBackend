"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-02 17:50:22
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Depends.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-11 20:57:35
# @Software         : Vscode
"""
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ..Config import get_settings
from ..Services import get_user_id, get_user_nouser
from .Exceptions import (
    CredentialsError,
    IncorrectPassword,
    InvalidData,
    UserNotFound,
    notAuthenticated,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/jwt/token")
settings = get_settings()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = SessionLocal()


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if "user" in kwargs:
            return await func(*args, **kwargs)
        raise notAuthenticated

    return wrapper


def get_db():
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    try:
        db = session
        yield db
    finally:
        db.close()


def verity_password(plain_password: str, hashed_password: str):
    return plain_password == hashed_password


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_schema)
):
    try:
        payload = jwt.decode(
            token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        id: str = payload.get("sub")
        if id is None:
            raise CredentialsError
        else:
            id_token = int(id)
    except JWTError:
        raise CredentialsError
    try:
        user = get_user_id(db, id_token)
        return user
    except Exception:
        raise CredentialsError


def authenticate_user(db: Session, nouser: str, password: str):
    nouser_process = int(nouser)
    user = get_user_nouser(db, nouser_process)
    if not verity_password(plain_password=password, hashed_password=user.Psw):
        raise IncorrectPassword
    return user


def created_access_token(data: dict, expires_delta: Optional[timedelta] = None):
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
