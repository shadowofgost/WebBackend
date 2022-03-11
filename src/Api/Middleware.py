# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-03-09 12:29:34
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Middleware.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 14:21:32
# @Software         : Vscode
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from Config import get_settings
from fastapi import Request, Response
settings = get_settings()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = SessionLocal()


async def middleware_get_db(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
