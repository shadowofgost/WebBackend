"""
# @Time             : 2022-01-13 15:35:16
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Services/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-09 23:57:20
# @LastAuthor       : Albert Wang
"""
from .ServiceCurricula import get_curricula
from .PublicService import service_select,service_insert,service_update,service_delete
from .ServiceUser import get_user_id,get_user_nouser
