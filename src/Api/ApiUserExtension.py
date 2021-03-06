# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:22:46
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiUserExtension.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 22:18:55
# @Software         : Vscode
"""
from fastapi import APIRouter, Depends, UploadFile
from fastapi_pagination import Page, Params, paginate
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from Services import (
    service_select,
    service_insert,
    service_update,
    service_delete,
    SchemaUserPydantic,
    ModelUserExtensionSelectInSingleTableSchema,
    ModelUserExtensionSelectOutSingleTableSchema,
    ModelUserExtensionInsertSingleGetSchema,
    ModelUserExtensionUpdateSingleGetSchema,
    ModelUserExtensionInsertMultipleGetSchema,
    ModelUserExtensionUpdateMultipleGetSchema,
    DeleteMultipleGetSchema,
    Execution,
)
from .Depends import get_current_user, get_db

router = APIRouter(
    prefix="/model_userextension",
    tags=["model_userextension"],
)


class CurriculaGet(BaseModel):
    requires: ModelUserExtensionSelectInSingleTableSchema
    service_type: int = Field(
        title="选择查询的服务形式",
        description="根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户",
        default=0,
    )
    page: int = Field(default=1, title="页数", description="查询用的页码数")
    size: int = Field(default=5, title="记录的数量", description="一个页面查询记录的数量")


@router.post(
    "/search", response_model=Page[ModelUserExtensionSelectOutSingleTableSchema]
)
async def api_model_userextension_get(
    schema: CurriculaGet,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    model = "ModelUserExtension"
    result_data = service_select(session, model, schema.service_type, schema.requires)
    params = Params(page=schema.page, size=schema.size)
    return paginate(result_data, params)


@router.post("/", response_model=Execution)
async def api_model_userextension_insert(
    NoUser: str,
    file: UploadFile,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    model = "ModelUserExtension"
    photo=await file.read()
    schema_single = ModelUserExtensionInsertSingleGetSchema(
        NoUser=NoUser,
        FaceFeature=photo,
        Photo=photo,
    )
    schema = ModelUserExtensionInsertMultipleGetSchema(data=[schema_single], n=1)
    return service_insert(session, user.ID, model, schema)


@router.put("/", response_model=Execution)
async def api_model_userextension_update(
    ID: int,
    NoUser: str,
    file: UploadFile,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    model = "ModelUserExtension"
    photo=await file.read()
    schema_single = ModelUserExtensionUpdateSingleGetSchema(
        ID=ID,
        NoUser=NoUser,
        FaceFeature=photo,
        Photo=photo,
    )
    schema = ModelUserExtensionUpdateMultipleGetSchema(data=[schema_single], n=1)
    return service_update(session, user.ID, model, schema)


@router.delete("/", response_model=Execution)
async def api_model_userextension_delete(
    schema: DeleteMultipleGetSchema,
    session: Session = Depends(get_db),
    user: SchemaUserPydantic = Depends(get_current_user),
):
    schema.n = len(schema.data)
    model = "ModelUserExtension"
    return service_delete(session, user.ID, model, schema)
