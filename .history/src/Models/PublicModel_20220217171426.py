"""
# @Time             : 2022-01-13 23:23:00
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/PublicModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 17:04:25
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Identity,
    Integer,
    Unicode,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ModelPublic(Base):
    __abstract__ = True
    ID = Column(
        BigInteger,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False,
        index=True,
        comment="这是数据库id",
        doc="数据库ID字段，表示数据库唯一的值",
    )
    Rem = Column(Unicode(64), comment="备注", doc="备注,一般情况下备注为空")
    Introduction = Column(Unicode(254), comment="简介", doc="简介,一般是介绍表内容的")
    TimeUpdate = Column(
        BigInteger,
        index=True,
        comment="更新时间",
        doc="更新时间,记录最后更新时间；（2000-1-1 0:0:0 经过的秒）",
    )
    IdManager = Column(BigInteger, index=True, comment="最后操作的人的id", doc="最后操作的人的id")
    IMark = Column(
        Integer, index=True, comment="存在标记", doc="存在标记,表示记录是否删除一般删除是1,没删除是0  "
    )
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Unicode(254))
    back_up3 = Column(Unicode(254))
    back_up4 = Column(Integer)
    back_up5 = Column(Integer)
    back_up6 = Column(Integer)
