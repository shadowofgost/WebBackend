# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Time             : 2022-01-13 15:36:30
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/main.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-03-27 00:54:26
# @LastAuthor       : Albert Wang
"""
from Base import app
import uvicorn
from Config import logger_config

logger = logger_config.init_logging()
if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=9001,
        reload=True,
        access_log=True,
    )
