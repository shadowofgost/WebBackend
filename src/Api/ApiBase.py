# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 18:49:28
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiBase.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-13 18:15:44
# @Software         : Vscode
"""
from fastapi import FastAPI, Request, Depends
import time
from fastapi.middleware.cors import CORSMiddleware
from .Login import router as login_router
from .ApiCoursePlan import router as api_course_plan_router
from .ApiCurricula import router as api_curricula_router
from .ApiDepartment import router as api_department_router
from .ApiEquipment import router as api_equipment_router
from .ApiLocation import router as api_location_router

##from ...Backup.ApiLocationExtension import router as api_location_extension_router
##from .ApiMmx import router as api_mmx_router
##from .ApiMmxData import router as api_mmx_data_router
from .ApiRunningAccount import router as api_running_account_router

##from .ApiTypera import router as api_typera_router
from .ApiUser import router as api_user_router
from .ApiUserExtension import router as api_user_extension_router

##from .Depends import request_info
from .Middleware import middleware_get_db

##app = FastAPI(dependencies=[Depends(request_info)])
app = FastAPI()
origins = ["http://127.0.0.1:8080" "http://127.0.0.1"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    return await middleware_get_db(request, call_next)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


list_router = [
    login_router,
    api_course_plan_router,
    api_curricula_router,
    api_department_router,
    api_equipment_router,
    api_location_router,
    ##api_location_extension_router,
    ##api_mmx_router,
    ##api_mmx_data_router,
    api_running_account_router,
    ##api_typera_router,
    api_user_router,
    api_user_extension_router,
]
for i in list_router:
    app.include_router(i)
