"""
# @Time             : 2022-01-14 20:41:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 21:07:50
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
from .Public import Base,ModelPublic
Base=Base.metadata
