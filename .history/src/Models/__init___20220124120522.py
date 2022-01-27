"""
# @Time             : 2022-01-14 20:41:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-24 11:55:22
# @LastAuthor       : Albert Wang
"""
from .ModelCurricula import ModelCurricula
from .ModelDepartment import ModelDepartment
from .ModelEquipment import ModelEquipment
from .ModelLocation import ModelLocation, ModelLocationExtension
from .ModelMmx import ModelMmx, ModelMmxData
from .ModelCoursePlan import ModelCoursePlan
from .ModelRunningAccount import ModelRunningAccount
from .ModelTableInformation import ModelTableInformation
from .ModelTypera import ModelTypera
from .ModelUser import ModelUser, ModelUserExtension
from .ModelPublic import Base, ModelPublic
from .ModelPublic import ModelPublic, exclude, nullable, sqlalchemy_to_pydantic
from .ORM import ORM, single_delete,single_delete_physical,single_table_multiple_require_select,single_table_condition_select,single_table_name_select,single_insert,single_update,execution,multiple_delete,multiple_delete_physical,multiple_insert,multiple_update
