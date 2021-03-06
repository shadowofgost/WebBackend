# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Time             : 2022-01-13 23:19:45
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Models/ModelCoursePlan.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-03-17 15:52:40
# @LastAuthor       : Albert Wang
"""
from sqlalchemy import BigInteger, Column, Integer, SmallInteger, Unicode
from .PublicModel import ModelPublic


class ModelCoursePlan(ModelPublic):
    __tablename__ = "t_cyplan"
    ID_Curricula = Column(
        BigInteger,
        index=True,
        comment="课程ID,外键",
        doc="这是课程的id序列号，同时连接curricula表的外键字段，连接的是id",
    )
    ID_Location = Column(
        BigInteger,
        index=True,
        comment="地点ID，外键",
        doc="这是地点的id序列号，同时连接location表的外键字段，连接的是id",
    )
    ID_Speaker = Column(
        BigInteger,
        index=True,
        comment="主讲人ID，外键",
        doc="这是主讲人的id序列号，同时连接user表的外键字段，连接的是id",
    )
    TimeBegin = Column(
        Integer, index=True, comment="开始时间", doc="这是开始时间,单位是秒，每一天0时0分0秒开始的秒数"
    )
    TimeEnd = Column(Integer, index=True, comment="结束时间", doc="这是结束时间,单位是秒")
    Attr = Column(
        SmallInteger,
        index=True,
        comment="类型判断",
        doc="1代表实验类型、2代表普通上课类型、3讲座考勤类型，0或NULL同T_CyCurricula 实验类型：奇数刷卡派位，偶数刷卡下机，并记录派位编号 上课考勤类型：刷卡记录刷卡机编号 讲座考勤类型：刷卡记录刷卡机编号 ",
    )
    Charge = Column(SmallInteger, index=True, comment="收费类型字段", doc="免费0、收费1、开放2，NULL")
    PwAccess = Column(
        SmallInteger, index=True, comment="派位字段", doc="不派位0、刷卡派位1（派位指用户刷卡时系统指定座位）"
    )
    PwContinuous = Column(
        SmallInteger, index=True, comment="是否连续排位字段", doc="连续派位0、随机派位1"
    )
    PwDirection = Column(
        SmallInteger, index=True, comment="排位顺序字段", doc="顺序派位0、逆序派位1（当设置为随机派位时本功能无效）"
    )
    DoorOpen = Column(SmallInteger, index=True, comment="是否开门字段", doc="开门0、不开门1")
    TimeBeginCheckBegin = Column(
        Integer, comment="考勤开始的时刻表", doc="安排考勤开始的最早时间（单位为分钟，0代表无效）"
    )
    TimeBeginCheckEnd = Column(
        Integer, comment="考勤开始的时刻表", doc="安排考勤开始的最晚时间（单位为分钟，0代表无效）"
    )
    TimeEndCheckBegin = Column(
        Integer, comment="考勤结束的时刻表", doc="安排考勤结束的最早时间（单位为分钟，0代表无效）"
    )
    TimeEndCheckEnd = Column(
        Integer, comment="考勤开始的最早时刻表", doc="安排考勤结束的最早时间（单位为分钟，0代表无效）"
    )
    RangeUsers = Column(Unicode(4096), comment="学生学号列表", doc="学生学号列表，以逗号分隔")
    ListDepts = Column(Unicode(1024), comment="部门列表", doc="参加安排的部门列表，以逗号分隔")
    RangeEqus = Column(Unicode(1024), comment="座位范围列表", doc="课程使用的座位范围列表")
    ListPlaces = Column(Unicode(1024), comment="地点列表", doc="课程使用的地点列表")
    MapUser2Equ = Column(Unicode(4096), comment="对应列表", doc="学生和课程的对应表")
    AboutSpeaker = Column(Unicode(1024), comment="主讲人信息", doc="主讲人信息")
