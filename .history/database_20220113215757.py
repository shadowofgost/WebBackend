"""
# @Time             : 2022-01-13 20:56:12
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/database.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-13 21:47:57
# @LastAuthor       : Albert Wang
"""
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Table, Unicode,CHAR,String,DateTime,Boolean,ForeignKey,create_engine,BigInteger
from sqlalchemy.dialects.mssql import NTEXT

metadata = MetaData()


t_T_CyCurricula = Table(
    'T_CyCurricula', metadata,
    Column('ID', Integer),
    Column('Name', Unicode(254)),
    Column('TimeBegin', Integer),
    Column('TimeEnd', Integer),
    Column('ID_Location', Integer),
    Column('ID_Speaker', Integer),
    Column('Attr', Integer),
    Column('Charge', Integer),
    Column('PwAccess', Integer),
    Column('PwContinuou', Integer),
    Column('PwDirection', Integer),
    Column('DoorOpen', Integer),
    Column('TimeBeginCh', Integer),
    Column('TimeBeginCh1', Integer),
    Column('TimeEndChec', Integer),
    Column('TimeEndChec1', Integer),
    Column('RangeUsers', Unicode(254)),
    Column('ListDepts', Unicode(254)),
    Column('RangeEqus', Unicode(254)),
    Column('ListPlaces', Unicode(254)),
    Column('MapUser2Equ', Unicode(254)),
    Column('AboutSpeake', Unicode(254)),
    Column('Rem', Unicode(254)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyDept = Table(
    'T_CyDept', metadata,
    Column('ID', Integer),
    Column('ID_Parent', Integer),
    Column('Name', Unicode(254)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyEquipment = Table(
    'T_CyEquipment', metadata,
    Column('ID', Integer),
    Column('Name', Unicode(254)),
    Column('ID_LOCATION', Integer),
    Column('ID_LOCATION1', Integer),
    Column('ID_IP', Unicode(254)),
    Column('MAC', Unicode(254)),
    Column('State', Integer),
    Column('Login', Integer),
    Column('Link', Integer),
    Column('CLass', Integer),
    Column('Dx', Integer),
    Column('Dy', Integer),
    Column('ID_User', Integer),
    Column('ID_Plan', Integer),
    Column('iTimeBegin', Integer),
    Column('iTimeLogin', Integer),
    Column('WhiteList', Unicode(254)),
    Column('Rem', Unicode(254)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('PortListen', Integer),
    Column('Type', Integer),
    Column('TimeDelay', Integer),
    Column('KeyCancel', Integer),
    Column('KeyOk', Integer),
    Column('KeyDel', Integer),
    Column('KeyF1', Integer),
    Column('OnAll', Integer),
    Column('RangeEqus', Unicode(254)),
    Column('ListPlaces', Unicode(254)),
    Column('iMark', Integer)
)


t_T_CyLocation = Table(
    'T_CyLocation', metadata,
    Column('ID', Integer),
    Column('ID_Parent', Integer),
    Column('Name', Unicode(254)),
    Column('Rem', Unicode(254)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyLocationEx = Table(
    'T_CyLocationEx', metadata,
    Column('ID_LOCATION', Integer),
    Column('Attr', Integer),
    Column('DateBegin', Integer),
    Column('DateEnd', Integer),
    Column('ModeRun', Integer),
    Column('ModeShangJi', Integer),
    Column('EnableDelay', Integer),
    Column('DelayCharge', Integer),
    Column('EnableLimit', Integer),
    Column('LimitYuE_SJ', Integer),
    Column('EnableLimit1', Integer),
    Column('LimitYuE_XJ', Integer),
    Column('EnableLimit2', Integer),
    Column('LimitTime_X', Integer),
    Column('EnableWarnY', Integer),
    Column('WarnYuE', Integer),
    Column('EnableWarnT', Integer),
    Column('WarnTime', Integer),
    Column('EnableMinCo', Integer),
    Column('MinCost', Integer),
    Column('Price', Integer),
    Column('PriceMinute', Integer),
    Column('GetEquName', Integer),
    Column('GetEquIp', Integer),
    Column('GetEquMac', Integer),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyMmx = Table(
    'T_CyMmx', metadata,
    Column('ID', Integer),
    Column('ID_Data', Integer),
    Column('ID_Type', Integer),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyMmxData = Table(
    'T_CyMmxData', metadata,
    Column('ID', Integer),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('Data', NTEXT(1073741823)),
    Column('iMark', Integer)
)


t_T_CyPlan = Table(
    'T_CyPlan', metadata,
    Column('ID', Integer),
    Column('ID_Curricul', Integer),
    Column('TimeBegin', Integer),
    Column('TimeEnd', Integer),
    Column('ID_Location', Integer),
    Column('ID_Speaker', Integer),
    Column('Attr', Integer),
    Column('Charge', Integer),
    Column('PwAccess', Integer),
    Column('PwContinuou', Integer),
    Column('PwDirection', Integer),
    Column('DoorOpen', Integer),
    Column('TimeBeginCh', Integer),
    Column('TimeBeginCh1', Integer),
    Column('TimeEndChec', Integer),
    Column('TimeEndChec1', Integer),
    Column('RangeUsers', Unicode(254)),
    Column('ListDepts', Unicode(254)),
    Column('RangeEqus', Unicode(254)),
    Column('ListPlaces', Unicode(254)),
    Column('MapUser2Equ', Unicode(254)),
    Column('AboutSpeake', Unicode(254)),
    Column('Rem', Unicode(254)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyRunningAccount = Table(
    'T_CyRunningAccount', metadata,
    Column('ID', Integer),
    Column('ID_USER', Integer),
    Column('Time', Integer),
    Column('Type', Integer),
    Column('Money', Integer),
    Column('Param1', Integer),
    Column('Param2', Integer),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyTableInfo = Table(
    'T_CyTableInfo', metadata,
    Column('ID', Integer),
    Column('Name', Unicode(254)),
    Column('NameTable', Unicode(254)),
    Column('TimeUpdate', Integer)
)


t_T_CyTypeRA = Table(
    'T_CyTypeRA', metadata,
    Column('ID', Integer),
    Column('ID_Parent', Integer),
    Column('Name', Unicode(254)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)


t_T_CyUser = Table(
    'T_CyUser', metadata,
    Column('ID', Integer),
    Column('NoCard', Unicode(254)),
    Column('NoUser', Unicode(254)),
    Column('Name', Unicode(254)),
    Column('Psw', Unicode(254)),
    Column('DeptId', Integer),
    Column('Sex', Integer),
    Column('Attr', Integer),
    Column('AttrJf', Integer),
    Column('Yue', Integer),
    Column('Yue2', Integer),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('LocalID', Unicode(254)),
    Column('iMark', Integer)
)


t_T_CyUserEx = Table(
    'T_CyUserEx', metadata,
    Column('ID', Integer),
    Column('Rem', Unicode(254)),
    Column('Photo', NTEXT(1073741823)),
    Column('TimeUpdate', Integer),
    Column('IdManager', Integer),
    Column('iMark', Integer)
)
