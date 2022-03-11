# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Time             : 2022-01-13 23:22:46
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelMmx.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-03-11 14:22:57
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import BigInteger, Column, SmallInteger
from .PublicModel import ModelPublic


class ModelMmx(ModelPublic):
    __tablename__ = "t_cymmx"

    ID_Data = Column(
        BigInteger, index=True, comment="这是外键，媒体内容的ID", doc="这是外键，链接ModelMmxData媒体内容的ID"
    )
    ID_Type = Column(SmallInteger, index=True, comment="媒体类型", doc="媒体类型，1为PPT类型")
