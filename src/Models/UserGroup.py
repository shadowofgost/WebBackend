# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-25 16:19:06
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/UserGroup.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 14:23:47
# @Software         : Vscode
"""
from sqlalchemy import Column,Integer,Unicode

from .PublicModel import ModelPublic


class ModelAuthUserGroups(ModelPublic):
    __tablename__ = "auth_user_groups"

    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)


class ModelAuthUserUserPermissions(ModelPublic):
    __tablename__ = "auth_user_user_permissions"

    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class ModelAuthGroup(ModelPublic):
    __tablename__ = "auth_group"

    name = Column(Unicode(150), nullable=False)


class ModelAuthGroupPermissions(ModelPublic):
    __tablename__ = "auth_group_permissions"

    group_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class ModelAuthPermission(ModelPublic):
    __tablename__ = "auth_permission"

    name = Column(Unicode(255), nullable=False)
    content_type_id = Column(Integer, nullable=False)
    codename = Column(Unicode(100), nullable=False)
