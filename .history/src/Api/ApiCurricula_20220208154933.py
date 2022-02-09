"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-08 15:41:53
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate
from sqlalchemy.orm import Session

from ..Models import ModelCurriculaSelectOutSingleTableSchema,ModelUser
from .Depends import get_db,get_user

router=APIRouter(
    prefix="/curricula",
    tags=["curricula"],
    )
@router.get("/", response_model=Page[ModelCurriculaSelectOutSingleTableSchema])
def api_curricula_get(Params=Depends(),session:Session=Depends(get_db),user:ModelUser=Depends(get_user)):
    pass
