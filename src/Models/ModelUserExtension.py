# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-27 14:16:12
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Models/ModelUserExtension.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-22 22:16:39
# @Software         : Vscode
"""
from sqlalchemy import BigInteger, Column, LargeBinary, Unicode
from .PublicModel import ModelPublic


class ModelUserExtension(ModelPublic):
    __tablename__ = "t_cyuserex"
    NoUser = Column(
        Unicode(32), index=True, comment="账号（学工号）", doc="这是账号（学工号），不能超过15字符"
    )
    NoSfz = Column(BigInteger, index=True, comment="身份证号", doc="身份证号")
    FaceFeature = Column(LargeBinary, comment="图片", doc="人脸特征码；（二进制格式）")
    Photo = Column(LargeBinary, comment="上传的照片", doc="上传的图片")
