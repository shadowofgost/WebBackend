"""
# @Time             : 2022-01-14 16:37:07
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Api/test.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 16:50:31
# @LastAuthor       : Albert Wang
"""
from typing import List, Optional
from fastapi import Response, Cookie
from pydantic import BaseModel,Field
from ModelUser import PydanticUserex
from fastapi import FastAPI, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
import uvicorn

class Test(BaseModel):
    test:Optional[int]=Field(description="这是一个测试",title="test")
app=FastAPI()
@app.post("/test",response_model=PydanticUserex)
def test(
    responese: Response = None
):
    pass



