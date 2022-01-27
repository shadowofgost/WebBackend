"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-25 17:54:21
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/PublicValuesAndSchemas.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-01-27 12:50:10
# @Software         : Vscode
"""
from typing import Container, List, Optional, Type
from time import localtime, mktime, strptime, time
from pydantic import BaseModel
from .ModelCoursePlan import (
    ModelCoursePlan,
    ModelCoursePlanUpdateSingleGetSchema,
    ModelCoursePlanUpdateMultipleGetSchema,
    ModelCoursePlanUpdateSingleTableSchema,
    ModelCoursePlanUpdateMultipleTableSchema,
    ModelCoursePlanInsertSingleGetSchema,
    ModelCoursePlanInsertMultipleGetSchema,
    ModelCoursePlanInsertSingleTableSchema,
    ModelCoursePlanInsertMultipleTableSchema,
    ModelCoursePlanSelectOutSingleTableSchema,
    ModelCoursePlanSelectInSingleTableSchema,
    ModelCoursePlan_sub_stmt,
)
from .ModelCurricula import (
    ModelCurricula,
    ModelCurriculaUpdateSingleGetSchema,
    ModelCurriculaUpdateMultipleGetSchema,
    ModelCurriculaUpdateSingleTableSchema,
    ModelCurriculaUpdateMultipleTableSchema,
    ModelCurriculaInsertSingleGetSchema,
    ModelCurriculaInsertMultipleGetSchema,
    ModelCurriculaInsertSingleTableSchema,
    ModelCurriculaInsertMultipleTableSchema,
    ModelCurriculaSelectOutSingleTableSchema,
    ModelCurriculaSelectInSingleTableSchema,
    ModelCurricula_sub_stmt,
)
from .ModelDepartment import (
    ModelDepartment,
    ModelDepartmentUpdateSingleGetSchema,
    ModelDepartmentUpdateMultipleGetSchema,
    ModelDepartmentUpdateSingleTableSchema,
    ModelDepartmentUpdateMultipleTableSchema,
    ModelDepartmentInsertSingleGetSchema,
    ModelDepartmentInsertMultipleGetSchema,
    ModelDepartmentInsertSingleTableSchema,
    ModelDepartmentInsertMultipleTableSchema,
    ModelDepartmentSelectOutSingleTableSchema,
    ModelDepartmentSelectInSingleTableSchema,
    ModelDepartment_sub_stmt,
)
from .ModelEquipment import (
    ModelEquipment,
    ModelEquipmentUpdateSingleGetSchema,
    ModelEquipmentUpdateMultipleGetSchema,
    ModelEquipmentUpdateSingleTableSchema,
    ModelEquipmentUpdateMultipleTableSchema,
    ModelEquipmentInsertSingleGetSchema,
    ModelEquipmentInsertMultipleGetSchema,
    ModelEquipmentInsertSingleTableSchema,
    ModelEquipmentInsertMultipleTableSchema,
    ModelEquipmentSelectOutSingleTableSchema,
    ModelEquipmentSelectInSingleTableSchema,
    ModelEquipment_sub_stmt,
)
from .ModelLocation import (
    ModelLocation,
    ModelLocationUpdateSingleGetSchema,
    ModelLocationUpdateMultipleGetSchema,
    ModelLocationUpdateSingleTableSchema,
    ModelLocationUpdateMultipleTableSchema,
    ModelLocationInsertSingleGetSchema,
    ModelLocationInsertMultipleGetSchema,
    ModelLocationInsertSingleTableSchema,
    ModelLocationInsertMultipleTableSchema,
    ModelLocationSelectOutSingleTableSchema,
    ModelLocationSelectInSingleTableSchema,
    ModelLocation_sub_stmt,
    ModelLocationExtension,
    ModelLocationExtensionUpdateSingleGetSchema,
    ModelLocationExtensionUpdateMultipleGetSchema,
    ModelLocationExtensionUpdateSingleTableSchema,
    ModelLocationExtensionUpdateMultipleTableSchema,
    ModelLocationExtensionInsertSingleGetSchema,
    ModelLocationExtensionInsertMultipleGetSchema,
    ModelLocationExtensionInsertSingleTableSchema,
    ModelLocationExtensionInsertMultipleTableSchema,
    ModelLocationExtensionSelectOutSingleTableSchema,
    ModelLocationExtensionSelectInSingleTableSchema,
    ModelLocationExtension_sub_stmt,
)
from .ModelMmx import (
    ModelMmx,
    ModelMmxUpdateSingleGetSchema,
    ModelMmxUpdateMultipleGetSchema,
    ModelMmxUpdateSingleTableSchema,
    ModelMmxUpdateMultipleTableSchema,
    ModelMmxInsertSingleGetSchema,
    ModelMmxInsertMultipleGetSchema,
    ModelMmxInsertSingleTableSchema,
    ModelMmxInsertMultipleTableSchema,
    ModelMmxSelectOutSingleTableSchema,
    ModelMmxSelectInSingleTableSchema,
    ModelMmx_sub_stmt,
    ModelMmxData,
    ModelMmxDataUpdateSingleGetSchema,
    ModelMmxDataUpdateMultipleGetSchema,
    ModelMmxDataUpdateSingleTableSchema,
    ModelMmxDataUpdateMultipleTableSchema,
    ModelMmxDataInsertSingleGetSchema,
    ModelMmxDataInsertMultipleGetSchema,
    ModelMmxDataInsertSingleTableSchema,
    ModelMmxDataInsertMultipleTableSchema,
    ModelMmxDataSelectOutSingleTableSchema,
    ModelMmxDataSelectInSingleTableSchema,
    ModelMmxData_sub_stmt,
)
from .ModelRunningAccount import (
    ModelRunningAccount,
    ModelRunningAccountUpdateSingleGetSchema,
    ModelRunningAccountUpdateMultipleGetSchema,
    ModelRunningAccountUpdateSingleTableSchema,
    ModelRunningAccountUpdateMultipleTableSchema,
    ModelRunningAccountInsertSingleGetSchema,
    ModelRunningAccountInsertMultipleGetSchema,
    ModelRunningAccountInsertSingleTableSchema,
    ModelRunningAccountInsertMultipleTableSchema,
    ModelRunningAccountSelectOutSingleTableSchema,
    ModelRunningAccountSelectInSingleTableSchema,
    ModelRunningAccount_sub_stmt,
)
from .ModelTableInformation import (
    ModelTableInformation,
    ModelTableInformationUpdateSingleGetSchema,
    ModelTableInformationUpdateMultipleGetSchema,
    ModelTableInformationUpdateSingleTableSchema,
    ModelTableInformationUpdateMultipleTableSchema,
    ModelTableInformationInsertSingleGetSchema,
    ModelTableInformationInsertMultipleGetSchema,
    ModelTableInformationInsertSingleTableSchema,
    ModelTableInformationInsertMultipleTableSchema,
    ModelTableInformationSelectOutSingleTableSchema,
    ModelTableInformationSelectInSingleTableSchema,
    ModelTableInformation_sub_stmt,
)
from .ModelTypera import (
    ModelTypera,
    ModelTyperaUpdateSingleGetSchema,
    ModelTyperaUpdateMultipleGetSchema,
    ModelTyperaUpdateSingleTableSchema,
    ModelTyperaUpdateMultipleTableSchema,
    ModelTyperaInsertSingleGetSchema,
    ModelTyperaInsertMultipleGetSchema,
    ModelTyperaInsertSingleTableSchema,
    ModelTyperaInsertMultipleTableSchema,
    ModelTyperaSelectOutSingleTableSchema,
    ModelTyperaSelectInSingleTableSchema,
    ModelTypera_sub_stmt,
)
from .ModelUser import (
    ModelUser,
    ModelUserUpdateSingleGetSchema,
    ModelUserUpdateMultipleGetSchema,
    ModelUserUpdateSingleTableSchema,
    ModelUserUpdateMultipleTableSchema,
    ModelUserInsertSingleGetSchema,
    ModelUserInsertMultipleGetSchema,
    ModelUserInsertSingleTableSchema,
    ModelUserInsertMultipleTableSchema,
    ModelUserSelectOutSingleTableSchema,
    ModelUserSelectInSingleTableSchema,
    ModelUser_sub_stmt,
    ModelUserExtension,
    ModelUserExtensionUpdateSingleGetSchema,
    ModelUserExtensionUpdateMultipleGetSchema,
    ModelUserExtensionUpdateSingleTableSchema,
    ModelUserExtensionUpdateMultipleTableSchema,
    ModelUserExtensionInsertSingleGetSchema,
    ModelUserExtensionInsertMultipleGetSchema,
    ModelUserExtensionInsertSingleTableSchema,
    ModelUserExtensionInsertMultipleTableSchema,
    ModelUserExtensionSelectOutSingleTableSchema,
    ModelUserExtensionSelectInSingleTableSchema,
    ModelUserExtension_sub_stmt,
)
from .Session import (
    ModelSqlAlchemySession,
    ModelSqlAlchemySessionUpdateSingleGetSchema,
    ModelSqlAlchemySessionUpdateMultipleGetSchema,
    ModelSqlAlchemySessionUpdateSingleTableSchema,
    ModelSqlAlchemySessionUpdateMultipleTableSchema,
    ModelSqlAlchemySessionInsertSingleGetSchema,
    ModelSqlAlchemySessionInsertMultipleGetSchema,
    ModelSqlAlchemySessionInsertSingleTableSchema,
    ModelSqlAlchemySessionInsertMultipleTableSchema,
    ModelSqlAlchemySessionSelectOutSingleTableSchema,
    ModelSqlAlchemySessionSelectInSingleTableSchema,
)


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
    "ModelEquipment": {"delete_single_schema": DeleteSingleTableSchema,"delete_multiple_schema": DeleteMultipleTableSchema,"delete_single_get_schema": DeleteSingleGetSchema,"delete_multiple_get_schema": DeleteMultipleGetSchema,"update_single_schema": ModelEquipmentUpdateSingleTableSchema,"update_multiple_schema": ModelEquipmentUpdateMultipleTableSchema,"update_single_get_schema": ModelEquipmentUpdateSingleGetSchema,"update_multiple_get_schema": ModelEquipmentUpdateMultipleGetSchema,"insert_single_schema": ModelEquipmentInsertSingleTableSchema,"insert_multiple_schema": ModelEquipmentInsertMultipleTableSchema,"insert_single_get_schema": ModelEquipmentInsertSingleGetSchema,"insert_multiple_get_schema": ModelEquipmentInsertMultipleGetSchema,"select_single_schema": ModelEquipmentSelectInSingleTableSchema,"select_multiple_schema": ModelEquipmentSelectOutSingleTableSchema,"model": ModelEquipment,"service_sub_stmt": ModelEquipment_sub_stmt},
    "ModelLocation": {"delete_single_schema": DeleteSingleTableSchema,"delete_multiple_schema": DeleteMultipleTableSchema,"delete_single_get_schema": DeleteSingleGetSchema,"delete_multiple_get_schema": DeleteMultipleGetSchema,"update_single_schema": ModelLocationUpdateSingleTableSchema,"update_multiple_schema": ModelLocationUpdateMultipleTableSchema,"update_single_get_schema": ModelLocationUpdateSingleGetSchema,"update_multiple_get_schema": ModelLocationUpdateMultipleGetSchema,"insert_single_schema": ModelLocationInsertSingleTableSchema,"insert_multiple_schema": ModelLocationInsertMultipleTableSchema,"insert_single_get_schema": ModelLocationInsertSingleGetSchema,"insert_multiple_get_schema": ModelLocationInsertMultipleGetSchema,"select_single_schema": ModelLocationSelectInSingleTableSchema,"select_multiple_schema": ModelLocationSelectOutSingleTableSchema,"model": ModelLocation,"service_sub_stmt": ModelLocation_sub_stmt},
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
