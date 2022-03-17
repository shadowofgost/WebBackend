# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Time             : 2022-01-13 23:23:28
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTableInformation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-03-17 15:47:23
# @LastAuthor       : Albert Wang
"""
from pydoc import doc
from sqlalchemy import Column, Unicode

from .PublicModel import ModelPublic


class ModelTableInformation(ModelPublic):
    __tablename__ = "t_cytableinfo"

    Name = Column(Unicode(50), index=True, comment="用户名", doc="用户名，不能超过15字符，必须有值；")
    NameTable = Column(Unicode(50), index=True, comment="对应表的名称，必须有值；")
