"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-25 17:54:21
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/PublicValuesAndSchemas.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-27 15:06:07
# @Software         : Vscode
"""
from fileinput import filename
from typing import Container, List, Optional, Type
from time import localtime, mktime, strptime, time
from pydantic import BaseModel
import sys  # 即添加包名的搜索路径
import os

path = os.path.dirname(__file__)
filename_list = [
    filename_str.split(".")[0] for filename_str in os.listdir(path) if filename_str.endswith(".py")
]
print(filename_list)


def format_current_time():
    base_time = mktime(strptime("2000-01-01 00:00:00", "%Y-%m-%d %X"))  ##设定标准或者说基础的时间
    current_time = mktime(localtime())  ##获取当前时间
    time_update = int(current_time - base_time)  ##计算时间差
    return time_update


class DeleteSingleGetSchema(BaseModel):
    id: int


class DeleteMultipleGetSchema(BaseModel):
    data: List[DeleteSingleGetSchema]
    n: int


class DeleteSingleTableSchema(DeleteSingleGetSchema):
    TimeUpdate: int = format_current_time()


class DeleteMultipleTableSchema(BaseModel):
    data: List[DeleteSingleTableSchema]
    n: int


error_database_execution = {"error": "database error"}
error_schema_validation = {"error": "schema validation error"}
error_fuction_not_implemented = {"error": "function not implemented"}
model_dict = {}
name_column_model_dict = {}
name_column_model_list = [
    "ModelUser",
    "ModelTypera" "ModelTableInformation",
    "ModelLocation",
    "ModelEquipment",
    "ModelDepartment",
    "ModelCurricula",
]
name_model_list = ["ModelCoursePlan", "ModelCurricula", "ModelDepartment"]
