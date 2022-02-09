"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-02 16:50:20
# @Software         : Vscode
"""
from fastapi import APIRouter
from 
router=APIRouter(
    prefix="/curricula",
    tags=["curricula"],
    )
@router.get("/", response_model=List[ModelCurricula])
