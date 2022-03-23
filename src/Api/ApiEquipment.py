# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:19:57
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiEquipment.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-23 12:51:26
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from Services import (
    service_select,
    service_insert,
    service_update,
    service_delete,
    SchemaUserPydantic,
    ModelEquipmentSelectInSingleTableSchema,
    ModelEquipmentSelectOutSingleTableSchema,
    ModelEquipmentInsertMultipleGetSchema,
    ModelEquipmentUpdateMultipleGetSchema,
    DeleteMultipleGetSchema,
    Execution,
)
from .Depends import get_current_user, get_db

router = APIRouter(
    prefix="/model_equipment",
    tags=["model_equipment"],
)


class CurriculaGet(BaseModel):
    requires: ModelEquipmentSelectInSingleTableSchema
    service_type: int = Field(
        title="选择查询的服务形式",
        description="根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户",
        default=0,
    )
    page: int = Field(default=1, title="页数", description="查询用的页码数")
    size: int = Field(default=5, title="记录的数量", description="一个页面查询记录的数量")


@router.post("/search", response_model=Page[ModelEquipmentSelectOutSingleTableSchema])
async def api_model_equipment_get(
    schema: CurriculaGet,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    model = "ModelEquipment"
    result_data = service_select(session, model, schema.service_type, schema.requires)
    params = Params(page=schema.page, size=schema.size)
    return paginate(result_data, params)


@router.post("/", response_model=Execution)
async def api_model_equipment_insert(
    schema: ModelEquipmentInsertMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelEquipment"
    return service_insert(session, user.ID, model, schema)


@router.put("/", response_model=Execution)
async def api_model_equipment_update(
    schema: ModelEquipmentUpdateMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelEquipment"
    return service_update(session, user.ID, model, schema)


@router.delete("/", response_model=Execution)
async def api_model_equipment_delete(
    schema: DeleteMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelEquipment"
    return service_delete(session, user.ID, model, schema)
