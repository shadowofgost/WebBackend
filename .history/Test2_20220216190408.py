"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-09 15:52:14
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/Test2.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-16 18:55:41
# @Software         : Vscode
"""
import os
import time
LOG_DIR = os.path.join(os.getcwd(), f'{time.strftime("%Y-%m-%d")+"_info"}.log')
print(LOG_DIR)
