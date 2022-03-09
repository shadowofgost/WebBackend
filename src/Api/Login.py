"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 18:44:32
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Login.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-09 12:44:14
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel,Field
from sqlalchemy.orm import Session

from .Depends import authenticate_user, created_access_token, get_db


class Token(BaseModel):
    access_token: str
    token_type: str
    attr:int= Field(title="用户权限设置",description="这个attr是对数据库attr的重新设定，1是管理员，2是教师，3是学生,4 是其他人")


router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post("/", response_model=Token)
async def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    access_token = await created_access_token(data={"sub": user.ID})
    return {"access_token": access_token, "token_type": "bearer","attr":user.Attr}
