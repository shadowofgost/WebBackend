# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-08 19:06:25
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Components/Exceptions.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 14:21:38
# @Software         : Vscode
"""
from .Exceptions import CredentialsError,UserNotFound,IncorrectPassword,InvalidData,notAuthenticated,inactiveUser,error_service_validation,error_service_null,error_database_execution,error_schema_validation,error_fuction_not_implemented,success_execution
