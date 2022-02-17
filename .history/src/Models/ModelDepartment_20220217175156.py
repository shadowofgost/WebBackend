"""
# @Time             : 2022-01-13 23:21:37
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelDepartment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 17:50:59
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import BigInteger, Column, Unicode
from .PublicModel import ModelPublic


class ModelDepartment(ModelPublic):
    __tablename__ = "t_cydept"

    ID_Parent = Column(BigInteger, index=True, comment="父级部门ID", doc="顶级部门值为0")
    Name = Column(Unicode(32), index=True, comment="部门名称", doc="部门的名称")
    Name2 = Column(Unicode(32), index=True, comment="部门名称的简写", doc="部门的名称的简写")
