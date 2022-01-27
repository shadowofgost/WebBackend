"""
# @Time             : 2022-01-13 23:21:52
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Model/ModelEquipment.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-16 14:45:43
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import (
    Boolean,
    Column,
    Identity,
    Integer,
    LargeBinary,
    SmallInteger,
    Table,
    Unicode,
    BigInteger,
)
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.ext.declarative import declarative_base
from Public import ModelPublic,exclude,nullable


class ModelEquipment(ModelPublic):
    __tablename__ = 't_cyequipment'

    ID_Location = Column(BigInteger,index=True,comment="设备所在地ID",doc="设备所在地ID")
    ID_User = Column(BigInteger, index=True,comment="设备拥有者ID",doc="设备拥有者ID")
    Name = Column(Unicode(32),index=True,comment="设备名称",doc="设备名称")
    ID_Location_SN = Column(BigInteger,index=True, comment="位置内编号",doc="位置内编号")
    ID_IP = Column(Unicode(16),index=True,comment="IP地址",doc="IP地址")
    MAC = Column(Unicode(24),comment="MAC地址",doc="MAC地址")
    State = Column(SmallInteger,index=True,comment="设备状态",doc="0：正常空闲、1：故障、2：其它、3：正常使用中、4开放，必须有值")
    Login = Column(SmallInteger,index=True,comment="登陆状态",doc="登录状态，0：未登录、1：已经登录 ")
    Link = Column(SmallInteger,index=True,comment="网络状态",doc="网络状态，0：脱机、1：在线")
    Class_field = Column(SmallInteger,index=True,name="Class",comment="设备种类",doc="设备种类，0：PC设备、2：刷卡门禁设备，11：服务器设备必须有值")
    Dx = Column(Integer,doc="Layout显示坐标位置x（单位像素），必须有值",comment="Dx")
    Dy = Column(Integer,doc="Layout显示坐标位置y（单位像素），必须有值",comment="Dy")
    iTimeBegin = Column(Integer)
    iTimeLogin = Column(Integer)
    WhiteList = Column(Unicode(1024),doc="白名单",comment="白名单")
    PortListen = Column(Integer,comment="接受数据端口",doc="接收数据端口,默认:1234，必须有值")
    Type = Column(Integer,comment="刷卡器类型",doc="刷卡器类型,默认:31，必须有值")
    TimeDelay = Column(Integer,comment="门禁延迟时间",doc="门禁开门延时,默认:5秒，必须有值")
    KeyCancel = Column(Integer)
    KeyDel = Column(Integer)
    KeyF1 = Column(Integer)
    OnAll = Column(Integer)
    RangeEqus = Column(Unicode(64))
    ListPlaces = Column(Unicode(64))
    ID_Plan = Column(BigInteger,comment="计划ID",index=True)
    KeyOk = Column(Integer)
