# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:21:20
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiRunningAccount.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-23 13:15:57
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends, Query
from fastapi_pagination import Page, Params, paginate
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from Services import (
    service_select,
    service_insert,
    service_update,
    service_delete,
    SchemaUserPydantic,
    ModelRunningAccountSelectInSingleTableSchema,
    ModelRunningAccountSelectOutSingleTableSchema,
    ModelRunningAccountInsertMultipleGetSchema,
    ModelRunningAccountUpdateMultipleGetSchema,
    DeleteMultipleGetSchema,
    RunningAccountSchema,
    get_running_account,
    Execution,
)
from .Depends import get_current_user, get_db

router = APIRouter(
    prefix="/model_runningaccount",
    tags=["model_runningaccount"],
)


class CurriculaGet(BaseModel):
    requires: ModelRunningAccountSelectInSingleTableSchema
    service_type: int = Field(
        title="选择查询的服务形式",
        description="根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户",
        default=0,
    )
    page: int = Field(default=1, title="页数", description="查询用的页码数")
    size: int = Field(default=5, title="记录的数量", description="一个页面查询记录的数量")


@router.post("/result", response_model=Page[RunningAccountSchema])
async def api_result(
    course_plan: int = Query(default=None, title="需要查询的courseplam，也就是课程安排的id的值"),
    page:int= Query(default=1, title="查询用的页码数"),
    size:int= Query(default=5, title="一个页面查询记录的数量",ge=5,le=100),
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema=ModelRunningAccountSelectInSingleTableSchema(Param2=course_plan)
    result_data = get_running_account(session, user, schema)
    params = Params(page=page, size=size)
    return paginate(result_data, params)


@router.post(
    "/search", response_model=Page[ModelRunningAccountSelectOutSingleTableSchema]
)
async def api_model_runningaccount_get(
    schema: CurriculaGet,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    model = "ModelRunningAccount"
    result_data = service_select(session, model, schema.service_type, schema.requires)
    params = Params(page=schema.page, size=schema.size)
    return paginate(result_data, params)


@router.post("/", response_model=Execution)
async def api_model_runningaccount_insert(
    schema: ModelRunningAccountInsertMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelRunningAccount"
    return service_insert(session, user.ID, model, schema)


@router.put("/", response_model=Execution)
async def api_model_runningaccount_update(
    schema: ModelRunningAccountUpdateMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelRunningAccount"
    return service_update(session, user.ID, model, schema)


@router.delete("/", response_model=Execution)
async def api_model_runningaccount_delete(
    schema: DeleteMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelRunningAccount"
    return service_delete(session, user.ID, model, schema)
