# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Time             : 2022-01-13 15:35:16
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Services/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-03-11 14:24:27
# @LastAuthor       : Albert Wang
"""
from .ServiceCurricula import get_curricula
from .ServiceCoursePlan import get_course_plan
from .ServiceUser import get_user_id, get_user_nouser, SchemaUserPydantic
from .ServiceRunningAccount import get_running_account,RunningAccountSchema
from .PublicValuesAndSchemas import (
    DeleteMultipleGetSchema,
    DeleteMultipleTableSchema,
    DeleteSingleGetSchema,
    DeleteSingleTableSchema,
    import_models_schemas,
    model_dict,
    name_column_model_dict,
    Execution,
)
from .PublicService import (
    service_select,
    service_insert,
    service_update,
    service_delete,
)
locals_data = import_models_schemas()
globals().update(locals_data)

from .ORM import (
    ORM,
    single_delete,
    single_delete_physical,
    single_table_multiple_require_select,
    single_table_condition_select,
    single_table_name_select,
    single_insert,
    single_update,
    execution,
    multiple_delete,
    multiple_delete_physical,
    multiple_insert,
    multiple_update,
)
from .SchemaCoursePlan import (
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
from .SchemaCurricula import (
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
from .SchemaDepartment import (
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
from .SchemaEquipment import (
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
from .SchemaLocation import (
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
)
from .SchemaLocationExtension import (
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
from .SchemaMmx import (
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
)
from .SchemaMmxData import (
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
from .SchemaRunningAccount import (
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
from .SchemaTableInformation import (
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
from .SchemaTypera import (
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
from .SchemaUser import (
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
)
from .SchemaUserExtension import (
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
from .SchemaSqlAlchemySession import (
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
