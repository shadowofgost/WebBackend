"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-27 14:16:12
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelUserExtension.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 18:05:03
# @Software         : Vscode
"""
from sqlalchemy import BigInteger,Column,LargeBinary,Unicode
from .PublicModel import ModelPublic


class ModelUserExtension(ModelPublic):
    __tablename__ = "t_cyuserex"
    NoUser = Column(
        Unicode(32), index=True, comment="账号（学工号）", doc="这是账号（学工号），不能超过15字符"
    )
    NoSfz = Column(BigInteger, index=True, comment="身份证号", doc="身份证号")
    FaceFearture = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo = Column(LargeBinary, comment="头像", doc="这是一个测试文档")
    Photo_dataF = Column(Unicode(2048), default="0")
