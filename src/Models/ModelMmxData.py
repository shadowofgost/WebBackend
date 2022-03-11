# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-27 14:15:56
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelMmxData.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 14:23:04
# @Software         : Vscode
"""
from sqlalchemy import Column,Unicode
from .PublicModel import ModelPublic


class ModelMmxData(ModelPublic):
    __tablename__ = "t_cymmxdata"

    Data = Column(Unicode(1024), comment="媒体的内容", doc="媒体的内容")
