"""
# @Time             : 2022-01-23 22:26:56
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Test/Test.py
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-27 14:30:40
# @LastAuthor       : Albert Wang
"""
from typing import Container, Optional, Type

a = 1
print(Optional[type(a).__name__])
model_dict = {
    "ModelCoursePlan": {
        "delete_single_schema": DeleteSingleTableSchema,
        "delete_multiple_schema": DeleteMultipleTableSchema,
        "delete_single_get_schema": DeleteSingleGetSchema,
        "delete_multiple_get_schema": DeleteMultipleGetSchema,
        "update_single_schema": ModelCoursePlanUpdateSingleTableSchema,
        "update_multiple_schema": ModelCoursePlanUpdateMultipleTableSchema,
        "update_single_get_schema": ModelCoursePlanUpdateSingleGetSchema,
        "update_multiple_get_schema": ModelCoursePlanUpdateMultipleGetSchema,
        "insert_single_schema": ModelCoursePlanInsertSingleTableSchema,
        "insert_multiple_schema": ModelCoursePlanInsertMultipleTableSchema,
        "insert_single_get_schema": ModelCoursePlanInsertSingleGetSchema,
        "insert_multiple_get_schema": ModelCoursePlanInsertMultipleGetSchema,
        "select_single_schema": ModelCoursePlanSelectInSingleTableSchema,
        "select_multiple_schema": ModelCoursePlanSelectOutSingleTableSchema,
        "model": ModelCoursePlan,
        "service_sub_stmt": ModelCoursePlan_sub_stmt,
    },
    "ModelCurricula": {
        "delete_single_schema": DeleteSingleTableSchema,
        "delete_multiple_schema": DeleteMultipleTableSchema,
        "delete_single_get_schema": DeleteSingleGetSchema,
        "delete_multiple_get_schema": DeleteMultipleGetSchema,
        "update_single_schema": ModelCurriculaUpdateSingleTableSchema,
        "update_multiple_schema": ModelCurriculaUpdateMultipleTableSchema,
        "update_single_get_schema": ModelCurriculaUpdateSingleGetSchema,
        "update_multiple_get_schema": ModelCurriculaUpdateMultipleGetSchema,
        "insert_single_schema": ModelCurriculaInsertSingleTableSchema,
        "insert_multiple_schema": ModelCurriculaInsertMultipleTableSchema,
        "insert_single_get_schema": ModelCurriculaInsertSingleGetSchema,
        "insert_multiple_get_schema": ModelCurriculaInsertMultipleGetSchema,
        "select_single_schema": ModelCurriculaSelectInSingleTableSchema,
        "selct_multiple_schema": ModelCurriculaSelectOutSingleTableSchema,
        "service_sub_stmt": ModelCurricula_sub_stmt,
        "model": ModelCurricula,
    },
    "ModelDepartment": {
        "delete_single_schema": DeleteSingleTableSchema,
        "delete_multiple_schema": DeleteMultipleTableSchema,
        "delete_single_get_schema": DeleteSingleGetSchema,
        "delete_multiple_get_schema": DeleteMultipleGetSchema,
        "update_single_schema": ModelDepartmentUpdateSingleTableSchema,
        "update_multiple_schema": ModelDepartmentUpdateMultipleTableSchema,
        "update_single_get_schema": ModelDepartmentUpdateSingleGetSchema,
        "update_multiple_get_schema": ModelDepartmentUpdateMultipleGetSchema,
        "insert_single_schema": ModelDepartmentInsertSingleTableSchema,
        "insert_multiple_schema": ModelDepartmentInsertMultipleTableSchema,
        "insert_single_get_schema": ModelDepartmentInsertSingleGetSchema,
        "insert_multiple_get_schema": ModelDepartmentInsertMultipleGetSchema,
        "select_single_schema": ModelDepartmentSelectInSingleTableSchema,
        "select_multiple_schema": ModelDepartmentSelectOutSingleTableSchema,
        "model": ModelDepartment,
        "service_sub_stmt": ModelDepartment_sub_stmt,
    },
    "ModelEquipment": {
        "delete_single_schema": DeleteSingleTableSchema,
        "delete_multiple_schema": DeleteMultipleTableSchema,
        "delete_single_get_schema": DeleteSingleGetSchema,
        "delete_multiple_get_schema": DeleteMultipleGetSchema,
        "update_single_schema": ModelEquipmentUpdateSingleTableSchema,
        "update_multiple_schema": ModelEquipmentUpdateMultipleTableSchema,
        "update_single_get_schema": ModelEquipmentUpdateSingleGetSchema,
        "update_multiple_get_schema": ModelEquipmentUpdateMultipleGetSchema,
        "insert_single_schema": ModelEquipmentInsertSingleTableSchema,
        "insert_multiple_schema": ModelEquipmentInsertMultipleTableSchema,
        "insert_single_get_schema": ModelEquipmentInsertSingleGetSchema,
        "insert_multiple_get_schema": ModelEquipmentInsertMultipleGetSchema,
        "select_single_schema": ModelEquipmentSelectInSingleTableSchema,
        "select_multiple_schema": ModelEquipmentSelectOutSingleTableSchema,
        "model": ModelEquipment,
        "service_sub_stmt": ModelEquipment_sub_stmt,
    },
    "ModelLocation": {
        "delete_single_schema": DeleteSingleTableSchema,
        "delete_multiple_schema": DeleteMultipleTableSchema,
        "delete_single_get_schema": DeleteSingleGetSchema,
        "delete_multiple_get_schema": DeleteMultipleGetSchema,
        "update_single_schema": ModelLocationUpdateSingleTableSchema,
        "update_multiple_schema": ModelLocationUpdateMultipleTableSchema,
        "update_single_get_schema": ModelLocationUpdateSingleGetSchema,
        "update_multiple_get_schema": ModelLocationUpdateMultipleGetSchema,
        "insert_single_schema": ModelLocationInsertSingleTableSchema,
        "insert_multiple_schema": ModelLocationInsertMultipleTableSchema,
        "insert_single_get_schema": ModelLocationInsertSingleGetSchema,
        "insert_multiple_get_schema": ModelLocationInsertMultipleGetSchema,
        "select_single_schema": ModelLocationSelectInSingleTableSchema,
        "select_multiple_schema": ModelLocationSelectOutSingleTableSchema,
        "model": ModelLocation,
        "service_sub_stmt": ModelLocation_sub_stmt,
    },
}
name_column_model_dict = {
    "ModelUser": ModelUser,
    "ModelTypera": ModelTypera,
    "ModelTableInformation": ModelTableInformation,
    "ModelLocation": ModelLocation,
    "ModelEquipment": ModelEquipment,
    "ModelDepartment": ModelDepartment,
    "ModelCurricula": ModelCurricula,
}
