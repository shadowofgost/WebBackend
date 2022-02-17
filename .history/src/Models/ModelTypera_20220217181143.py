"""
# @Time             : 2022-01-13 23:23:40
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelTypera.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 18:01:43
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import BigInteger,Column,Unicode

from .PublicModel import ModelPublic


class ModelTypera(ModelPublic):
    __tablename__ = "t_cytypera"

    ID_Parent = Column(BigInteger, index=True, comment="上级类型的ID", doc="上级类型的ID，顶级类型值为0")
    Name = Column(Unicode(128), index=True, comment="类型名称", doc="这是类型名称，不能超过15字符")
