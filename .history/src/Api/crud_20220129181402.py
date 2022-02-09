"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-22 10:03:25
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/crud.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-29 18:08:49
# @Software         : Vscode
"""
from pickletools import read_unicodestring1
from sqlalchemy.orm import Session
from . import models, schema
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from .database import SessionLocal
from sqlalchemy import select
from Models import

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/jwt/token")


def verity_password(plain_password: str, hashed_password: str):
    return plain_password == hashed_password


def jwt_get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_schema)
):
    error = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("sub")
        if id is None:
            raise error
    except JWTError:
        raise error
    user = get_user(db, id=id)
    if user is None:
        raise error
    return user


def create_user(db: Session, user: schema.UserCreate):
    db_user = models.User(id=user.id, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, id: str):
    #       model，shcema：DeletMultipleGetSchema
    # "ModelUser"
    # DeleteMultipleTableSchema=Schema(**schema.dict(),Idmanger=idmanager)
    # model_instance=ORM (model,session)
    # if schema.n==1:
    #   result=model_instance.delete(schema)
    # else:
    #   result=model_instance.delete_multiple(schema,multiple=True)
    # return result
    # result = select(models.User).where(models.User.id == id)
    # user = db.execute(result).first()
    return db.query(models.User).filter(models.User.id == id).first()


def jwt_authenticate_user(db: Session, id: str, password: str):
    user = get_user(db=db, id=id)
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
        expire = datetime.utcnow() + timedelta(minutes=100)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
