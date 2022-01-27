"""
# @Time             : 2022-01-13 23:23:54
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Model/UserModel.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-14 01:23:40
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

Base = declarative_base()


class TCyuser(Base):
    __tablename__ = 't_cyuser'

    ID = Column(Integer, primary_key=True,)
    Deptid = Column(Integer, nullable=False)
    Nocard = Column(Unicode(32))
    NoUser = Column(Unicode(32))
    Name = Column(Unicode(32))
    Psw = Column(Unicode(32))
    Sex = Column(Integer)
    Attr = Column(Integer)
    AttrJf = Column(Integer)
    Yue = Column(Integer)
    Yue2 = Column(Integer)
    TimeUpdate = Column(Integer)
    IdManager = Column(Integer)
    LocalID = Column(Unicode(1024))
    IMark = Column(Integer)
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    back_up1 = Column(Unicode(254))


class TCyuserex(Base):
    __tablename__ = 't_cyuserex'

    ID = Column(Integer, primary_key=True)
    Photo = Column(LargeBinary, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Rem = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    Photo_dataF = Column(Unicode)
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    back_up1 = Column(Unicode(254))

class AuthUserGroups(Base):
    __tablename__ = 'auth_user_groups'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)


class AuthUserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)

    class AuthGroup(Base):
        __tablename__ = 'auth_group'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    name = Column(Unicode(150), nullable=False)


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    group_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class AuthPermission(Base):
    __tablename__ = 'auth_permission'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    name = Column(Unicode(255), nullable=False)
    content_type_id = Column(Integer, nullable=False)
    codename = Column(Unicode(100), nullable=False)


PydanticUser = sqlalchemy_to_pydantic(User)
