"""
# @Time             : 2022-01-14 20:41:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-01 20:07:04
# @LastAuthor       : Albert Wang
"""
from .PublicValuesAndSchemas import (
    DeleteMultipleGetSchema,
    DeleteMultipleTableSchema,
    DeleteSingleGetSchema,
    DeleteSingleTableSchema,
    import_models_schemas,
    model_dict,
    name_column_model_dict
)

locals_data = import_models_schemas()
globals().update(locals_data)

from .PublicModel import ModelPublic, exclude, nullable, sqlalchemy_to_pydantic, Base
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
)
from .ModelLocationExtension import (
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
)
from .ModelMmxData import (
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
)
from .ModelUserExtension import (
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
from .ModelSqlAlchemySession import (
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
