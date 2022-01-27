"""
# @Time             : 2022-01-14 20:41:20
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Core/__init__.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 20:51:07
# @LastAuthor       : Albert Wang
"""
import sys # 即添加包名的搜索路径
from os.path import dirname, abspath
sys.path.append("Model")
root = dirname(dirname(abspath(__file__)))
sys.path.append(root)
print(sys.path)
print(root)
