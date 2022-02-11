"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:15:19
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiCurricula.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 20:18:58
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
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
    requires: ModelCurriculaSelectInSingleTableSchema
    service_type: int = Field(
        title="选择查询的服务形式",
        description="根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户",
        default=1,
    )


@router.get("/", response_model=Page[ModelCurriculaSelectOutSingleTableSchema])
def api_curricula_get(
    schema: CurriculaGet,
    Params=Depends(),
    session: Session = Depends(get_db),
    user: ModelCurriculaSelectOutSingleTableSchema = Depends(get_current_user),
):
    result_data = get_curricula(
        session, user.ID, user.Attr, schema.service_type, schema.requires
    )
    return paginate(result_data,Params)