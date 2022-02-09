"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 18:49:28
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/ApiBase.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-09 20:43:50
# @Software         : Vscode
"""
from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware
from .Login import router as login_router
from .ApiCurricula import router as api_curricula_router

app = FastAPI()

origins = ["http://127.0.0.1:8080" "http://127.0.0.1"]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login_router)
app.include_router(api_curricula_router)

