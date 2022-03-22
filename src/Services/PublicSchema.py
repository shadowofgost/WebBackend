# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-03-22 16:46:28
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/PublicSchema.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 17:57:04
# @Software         : Vscode
"""
from pydantic import BaseModel, create_model, validator
from time import localtime, mktime, strptime, time
from typing import List


def format_current_time():
    base_time = mktime(strptime("2000-01-01 00:00:00", "%Y-%m-%d %X"))  ##设定标准或者说基础的时间
    current_time = mktime(localtime())  ##获取当前时间
    time_update = int(current_time - base_time)  ##计算时间差
    return time_update


class DeleteSingleGetSchema(BaseModel):
    ID: int


class DeleteMultipleGetSchema(BaseModel):
    data: List[DeleteSingleGetSchema]
    n: int


class DeleteSingleTableSchema(DeleteSingleGetSchema):
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0


class DeleteMultipleTableSchema(BaseModel):
    data: List[DeleteSingleTableSchema]
    n: int


class Execution(BaseModel):
    message: str


class InsertBase():
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0

class UpdateBase():
    TimeUpdate: int = format_current_time()
    IdManager: int
    IMark: int = 0
