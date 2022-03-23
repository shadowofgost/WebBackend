# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 18:49:28
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Base.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-23 16:55:52
# @Software         : Vscode
"""
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from time import time
from Api.Login import router as login_router
from Api.ApiCoursePlan import router as api_course_plan_router
from Api.ApiCurricula import router as api_curricula_router
from Api.ApiDepartment import router as api_department_router
from Api.ApiEquipment import router as api_equipment_router
from Api.ApiLocation import router as api_location_router
from Api.ApiLocationExtension import router as api_location_extension_router
from Api.ApiMmx import router as api_mmx_router
from Api.ApiMmxData import router as api_mmx_data_router
from Api.ApiRunningAccount import router as api_running_account_router
from Api.ApiTypera import router as api_typera_router
from Api.ApiUser import router as api_user_router
from Api.ApiUserExtension import router as api_user_extension_router
from Api.Depends import request_info
from Api.Middleware import middleware_get_db

app = FastAPI(dependencies=[Depends(request_info)])
app = FastAPI(
    title="人脸识别",
    description="人脸识别考勤的Web端口",
    version="1.0.0",
    terms_of_service="http://47.117.68.250",
    contact={
        "name": "王子睿",
        "email": "shadowofgost@outlook.com",
    },
    license_info={
        "name": "GNU GENERAL PUBLIC LICENSE Version 3",
        "url": "https://www.gnu.org/licenses/quick-guide-gplv3",
    },
)
origins = ["http://127.0.0.1:8080" "http://127.0.0.1"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def get_db(request: Request, call_next):
    return await middleware_get_db(request, call_next)


app.mount("/static", StaticFiles(directory="static"), name="static")

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
