"""
# @Time             : 2022-01-13 15:35:38
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Api/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-15 17:00:12
# @LastAuthor       : Albert Wang
"""
import sys  # 即添加包名的搜索路径
import os

sys.path.append(os.getcwd())
from .ApiBase import app