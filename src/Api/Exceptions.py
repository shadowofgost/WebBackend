"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-08 19:06:25
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Api/Exceptions.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-10 11:53:03
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
