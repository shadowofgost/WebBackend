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
from fastapi import HTTPException, status

CredentialsError = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)  ## 没有登录出现的报错

UserNotFound = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="User With this username not found"
)

IncorrectPassword = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Incorrect password"
)

InvalidData = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="Invalid data provided",
)

notAuthenticated = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Not authenticated",
    headers={"WWW-Authenticate": "Bearer"},
)  ## 没有权限出现的报错

inactiveUser = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Inactive user",
)
error_service_validation = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="Service Validation Error,Service层数据严重失败",
)
error_service_null = HTTPException(
    status_code=status.HTTP_412_PRECONDITION_FAILED,
    detail="Service Null Error,所调用的service不存在",
)
error_database_execution = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Model Database execution error,model层查询数据库出现异常",
)
error_schema_validation = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="Model Schema validation error,model层传输数据模型验证失败",
)
error_fuction_not_implemented = HTTPException(
    status_code=status.HTTP_412_PRECONDITION_FAILED,
    detail="Model function error,model层传输数据出现数据缺失",
)
success_execution = {"message": "成功执行"}
