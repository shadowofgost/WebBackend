"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-02 17:40:30
# @Software         : Vscode
"""
from fastapi import APIRouter,Depends
from ..Models import ModelCurriculaSelectOutSingleTableSchema
from fastapi_pagination import paginate,Page,Params
router=APIRouter(
    prefix="/curricula",
    tags=["curricula"],
    )
@router.get("/", response_model=Page[ModelCurriculaSelectOutSingleTableSchema])
def api_curricula_get(Params=Depends()):
