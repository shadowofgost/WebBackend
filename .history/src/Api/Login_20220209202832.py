"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 18:44:32
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Login.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 20:18:31
# @Software         : Vscode
"""
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .Depends import get_db
from pydantic import BaseModel
from .Depends import authenticate_user, created_access_token


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
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = created_access_token(data={"sub": user.ID})
    return {"access_token": access_token, "token_type": "bearer"}
