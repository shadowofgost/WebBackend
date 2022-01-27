"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-25 17:54:21
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/PublicValuesAndSchemas.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-27 15:47:18
# @Software         : Vscode
"""
from fileinput import filename
from typing import Container, List, Optional, Type
from time import localtime, mktime, strptime, time
from pydantic import BaseModel

error_database_execution = {"error": "database error"}
error_schema_validation = {"error": "schema validation error"}
error_fuction_not_implemented = {"error": "function not implemented"}


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


def format_current_time():

    base_time = mktime(strptime("2000-01-01 00:00:00", "%Y-%m-%d %X"))  ##设定标准或者说基础的时间
    current_time = mktime(localtime())  ##获取当前时间
    time_update = int(current_time - base_time)  ##计算时间差
    return time_update


def import_models_schemas():
    ##把Model下的所有符合要求的实体model类和schema导入到当前的模块中
    import os
    from re import match

    name_column_model_list = [
        "ModelUser",
        "ModelTypera" "ModelTableInformation",
        "ModelLocation",
        "ModelEquipment",
        "ModelDepartment",
        "ModelCurricula",
    ]
    model_dict = {}
    name_column_model_dict = {}
    name_model_list = ["ModelCoursePlan", "ModelCurricula", "ModelDepartment"]
    path = os.path.dirname(__file__)
    model_filename_list = [
        filename_str.split(".")[0]
        for filename_str in os.listdir(path)
        if filename_str.endswith(".py")
        and match(r"Model", filename_str) is not None
        and match(r"ModelAbstract", filename_str) is None
    ]
    for model_filename in model_filename_list:
        tmp_dict = {}
        exec(
            f"from .{model_filename}  import ({model_filename} ,{model_filename}UpdateSingleGetSchema,{model_filename}UpdateMultipleGetSchema,{model_filename}UpdateSingleTableSchema,{model_filename}UpdateMultipleTableSchema,{model_filename}InsertSingleGetSchema,{model_filename}InsertMultipleGetSchema,{model_filename}InsertSingleTableSchema,{model_filename}InsertMultipleTableSchema,{model_filename}SelectOutSingleTableSchema,{model_filename}SelectInSingleTableSchema,{model_filename}_sub_stmt,)"
        )  ##导入对应的模块
        tmp_dict[model_filename] = eval(model_filename)
        tmp_dict["delete_single_schema"] = (DeleteSingleTableSchema,)
        tmp_dict["delete_multiple_schema"] = (DeleteMultipleTableSchema,)
        tmp_dict["delete_single_get_schema"] = (DeleteSingleGetSchema,)
        tmp_dict["delete_multiple_get_schema"] = (DeleteMultipleGetSchema,)
        tmp_dict["update_single_schema"] = (ModelCurriculaUpdateSingleTableSchema,)
        tmp_dict["update_multiple_schema"] = (ModelCurriculaUpdateMultipleTableSchema,)
        tmp_dict["update_single_get_schema"] = (ModelCurriculaUpdateSingleGetSchema,)
        tmp_dict["update_multiple_get_schema"] = (
            ModelCurriculaUpdateMultipleGetSchema,
        )
        tmp_dict["insert_single_schema"] = (ModelCurriculaInsertSingleTableSchema,)
        tmp_dict["insert_multiple_schema"] = (ModelCurriculaInsertMultipleTableSchema,)
        tmp_dict["insert_single_get_schema"] = (ModelCurriculaInsertSingleGetSchema,)
        tmp_dict["insert_multiple_get_schema"] = (
            ModelCurriculaInsertMultipleGetSchema,
        )
        tmp_dict["select_single_schema"] = (ModelCurriculaSelectInSingleTableSchema,)
        tmp_dict["selct_multiple_schema"] = (ModelCurriculaSelectOutSingleTableSchema,)
        tmp_dict["service_sub_stmt"] = (ModelCurricula_sub_stmt,)
        tmp_dict["model"] = (ModelCurricula,)
        ##exec(f"from {model_filename} import {model_filename}")
    return locals()


import_models_schemas()
