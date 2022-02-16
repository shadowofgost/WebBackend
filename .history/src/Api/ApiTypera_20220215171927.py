"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiTypera.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-15 17:09:29
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from Models import (
    ModelTyperaSelectInSingleTableSchema,
    ModelTyperaSelectOutSingleTableSchema,
    ModelTyperaInsertMultipleGetSchema,
    ModelTyperaUpdateMultipleGetSchema,
    DeleteMultipleGetSchema,
    Execution,
)
from Services import (
    get_curricula,
    service_select,
    service_insert,
    service_update,
    service_delete,
)
from .Depends import get_current_user, get_db

router = APIRouter(
    prefix="/model_typera",
    tags=["model_typera"],
)


class CurriculaGet(BaseModel):
    requires: ModelTyperaSelectInSingleTableSchema
    service_type: int = Field(
        title="选择查询的服务形式",
        description="根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户",
        default=1,
    )


@router.get("/", response_model=Page[ModelTyperaSelectOutSingleTableSchema])
async def api_model_typera_get(
    schema: CurriculaGet,
    Params=Depends(),
    session: Session = Depends(get_db),
    user: ModelTyperaSelectOutSingleTableSchema = Depends(get_current_user),
):
    model = "ModelTypera"
    result_data = service_select(
        session, user.ID, model, schema.service_type, schema.requires
    )
    return paginate(result_data, Params)


@router.post("/", response_model=Execution)
async def api_model_typera_insert(
    schema: ModelTyperaInsertMultipleGetSchema,
    session: Session = Depends(get_db),
    user: ModelTyperaSelectOutSingleTableSchema = Depends(get_current_user),
):
    model = "ModelTypera"
    return service_insert(session, user.ID, model, schema)


@router.put("/", response_model=Execution)
async def api_model_typera_update(
    schema: ModelTyperaUpdateMultipleGetSchema,
    session: Session = Depends(get_db),
    user: ModelTyperaSelectOutSingleTableSchema = Depends(get_current_user),
):
    model = "ModelTypera"
    return service_update(session, user.ID, model, schema)


@router.delete("/", response_model=Execution)
async def api_model_typera_delete(
    schema: DeleteMultipleGetSchema,
    session: Session = Depends(get_db),
    user: ModelTyperaSelectOutSingleTableSchema = Depends(get_current_user),
):
    model = "ModelTypera"
    return service_delete(session, user.ID, model, schema)
