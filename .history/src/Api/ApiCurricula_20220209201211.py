"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 20:12:09
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate
from sqlalchemy.orm import Session
from pydantic import BaseModel, F
from ..Models import (
    ModelCurriculaSelectOutSingleTableSchema,
    ModelCurriculaSelectInSingleTableSchema,
)
from .Depends import get_db, get_current_user
from ..Services import get_curricula

router = APIRouter(
    prefix="/curricula",
    tags=["curricula"],
)


class CurriculaGet(BaseModel):
    schema: ModelCurriculaSelectInSingleTableSchema
    service_type: int = FilePath


@router.get("/", response_model=Page[ModelCurriculaSelectOutSingleTableSchema])
def api_curricula_get(
    schema: ModelCurriculaSelectInSingleTableSchema,
    Params=Depends(),
    session: Session = Depends(get_db),
    user: ModelCurriculaSelectOutSingleTableSchema = Depends(get_current_user),
):
    return get_curricula(session, user.ID, user.Attr, service_type, schema)
