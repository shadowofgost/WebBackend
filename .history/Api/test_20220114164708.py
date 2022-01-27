"""
# @Time             : 2022-01-14 16:37:07
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Api/test.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 16:46:10
# @LastAuthor       : Albert Wang
"""
from typing import List, Optional
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from ModelUser import PydanticUserex
app=FastAPI()
@app.post("/test",response_model=PydanticUserex)
def test(
    responese: Response = None
):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
