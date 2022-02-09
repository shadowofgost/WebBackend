"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-02 17:50:22
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Depends.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 18:03:15
# @Software         : Vscode
"""
from datetime import datetime, timedelta
from http.client import UNAUTHORIZED
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel
from ..Config import get_settings
from ..Services.ModelUserCrud import model_user_crud_select
from .Exceptions import notAuthenticated,CredentialsError,UserNotFound,IncorrectPassword,InvalidData,

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/jwt/token")
settings = get_settings()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = SessionLocal()


class Token(BaseModel):
    access_token: str
    token_type: str


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
            raise notAuthenticated
        else:
            id_token = int(id)
    except JWTError:
        raise notAuthenticated
    user = model_user_crud_select(session=db, id_manager=id_token, service_type=1)
    if user is None:
        raise notAuthenticated
    return user


def authenticate_user(db: Session, id: str, password: str):
    user = model_user_crud_select(session=db, id_manager=id, service_type=1)
    if not user:
        return False
    if not verity_password(plain_password=password, hashed_password=user.password):
        return False
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
