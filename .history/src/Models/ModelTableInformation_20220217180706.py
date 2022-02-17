"""
# @Time             : 2022-01-13 23:23:28
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTableInformation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 17:57:06
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import Column,Unicode

from .PublicModel import ModelPublic


class ModelTableInformation(ModelPublic):
    __tablename__ = "t_cytableinfo"

    Name = Column(Unicode(50), index=True)
    NameTable = Column(Unicode(50), index=True)
