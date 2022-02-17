"""
# @Time             : 2022-01-13 23:22:21
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelLocation.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 17:43:48
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import BigInteger,Column,Unicode
from .PublicModel import ModelPublic


class ModelLocation(ModelPublic):
    __tablename__ = "t_cylocation"

    ID_Parent = Column(BigInteger, index=True, comment="上级位置ID", doc="这是上级位置ID，顶级位置值为0")
    Name = Column(Unicode(32), index=True, comment="位置名称", doc="这是位置名称，不能超过15字符")
