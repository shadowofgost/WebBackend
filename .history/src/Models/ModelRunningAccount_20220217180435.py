"""
# @Time             : 2022-01-13 23:23:15
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelRunningAccount.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-17 17:54:34
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import BigInteger, Column, Integer, SmallInteger
from .PublicModel import ModelPublic


class ModelRunningAccount(ModelPublic):
    __tablename__ = "t_cyrunningaccount"

    ID_User = Column(BigInteger, index=True, comment="这是外键用户ID", doc="这是外键，链接User的用户ID")
    Time = Column(
        BigInteger, index=True, comment="生成记录的时间", doc="生成记录（发生费用）的时间，从2000-1-1日计秒"
    )
    Type_field = Column(
        SmallInteger,
        index=True,
        name="Type",
        comment="这是外键，记录的类型",
        doc="这是记录的类型，其值定义如下：参见T_CyTypeRA表每一个功能的id，例如：考勤：4097，这是T_CyTypeRA表的id和外键",
    )
    Money = Column(Integer, comment="发生的费用", doc="发生的费用，单位为分")
    Param1 = Column(
        BigInteger,
        index=True,
        comment="考勤机编号",
        doc="这是考勤机编号，例如：收费管理员的ID：1910007,此时Type=0x101，上机机位编号：556678 此时Type=0x201，门禁考勤机编号：11111 此时Type=0x1001",
    )
    Param2 = Column(
        BigInteger,
        index=True,
        comment="这是外键安排编号",
        doc="这是外键，安排编号，例如：讲座、课程的编号：也就是对应Plan的id此时Type=4097；取消交易记录的ID：Type=0x106，这是连接Plan表的id",
    )
