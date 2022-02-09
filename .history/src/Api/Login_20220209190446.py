"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 18:44:32
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Login.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 18:59:31
# @Software         : Vscode
"""
from fastapi import FastAPI, Depends, HTTPException, status, Request, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from Depends import get_db
from pydantic import BaseModel
from .Depends import authenticate_user

class Token(BaseModel):
    access_token: str
    token_type: str


router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post("/", response_model=Token)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(
        db=db, id=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.created_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
