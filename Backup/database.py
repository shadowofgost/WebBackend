from sqlalchemy import Boolean, Column, Identity, Integer, LargeBinary, SmallInteger, Table, Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

()
metadata = Base.metadata


t_T_DeptWzII = Table(
    'T_DeptWzII', metadata,
    Column('ID', Integer),
    Column('ORGCODE', Unicode(254)),
    Column('PARENTCODE', Unicode(254)),
    Column('ORGNAME', Unicode(254)),
    Column('iTimeCreate', Integer),
    Column('iTimeUpdate', Integer)
)


t_T_UserWzII = Table(
    'T_UserWzII', metadata,
    Column('ID', Integer),
    Column('USERNUM', Unicode(254)),
    Column('USERNAME', Unicode(254)),
    Column('CARDUID', Unicode(254)),
    Column('CERTNUM', Unicode(254)),
    Column('iSex', Integer),
    Column('iDept', Integer),
    Column('iTimeCreate', Integer),
    Column('iTimeUpdate', Integer)
)


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


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    password = Column(Unicode(128), nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    username = Column(Unicode(150), nullable=False)
    first_name = Column(Unicode(30), nullable=False)
    last_name = Column(Unicode(150), nullable=False)
    email = Column(Unicode(254), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DATETIME2, nullable=False)
    last_login = Column(DATETIME2)


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


class CaptchaCaptchastore(Base):
    __tablename__ = 'captcha_captchastore'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    challenge = Column(Unicode(32), nullable=False)
    response = Column(Unicode(32), nullable=False)
    hashkey = Column(Unicode(40), nullable=False)
    expiration = Column(DATETIME2, nullable=False)


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    action_time = Column(DATETIME2, nullable=False)
    object_repr = Column(Unicode(200), nullable=False)
    action_flag = Column(SmallInteger, nullable=False)
    change_message = Column(Unicode, nullable=False)
    user_id = Column(Integer, nullable=False)
    object_id = Column(Unicode)
    content_type_id = Column(Integer)


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    app_label = Column(Unicode(100), nullable=False)
    model = Column(Unicode(100), nullable=False)


class DjangoMigrations(Base):
    __tablename__ = 'django_migrations'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    app = Column(Unicode(255), nullable=False)
    name = Column(Unicode(255), nullable=False)
    applied = Column(DATETIME2, nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(Unicode(40), primary_key=True)
    session_data = Column(Unicode, nullable=False)
    expire_date = Column(DATETIME2, nullable=False)


class TCycurricula(Base):
    __tablename__ = 't_cycurricula'

    ID = Column(Integer, primary_key=True)
    ID_Location = Column(Integer, nullable=False)
    ID_Speaker = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Name = Column(Unicode(32))
    TimeBegin = Column(Integer)
    TimeEnd = Column(Integer)
    Attr = Column(Integer)
    Charge = Column(Integer)
    PwAccess = Column(Integer)
    PwContinuous = Column(Integer)
    PwDirection = Column(Integer)
    DoorOpen = Column(Integer)
    TimeBeginCheckBegin = Column(Integer)
    TimeBeginCheckEnd = Column(Integer)
    TimeEndCheckBegin = Column(Integer)
    TimeEndCheckEnd = Column(Integer)
    RangeUsers = Column(Unicode(1024))
    ListDepts = Column(Unicode(1024))
    RangeEqus = Column(Unicode(1024))
    ListPlaces = Column(Unicode(1024))
    MapUser2Equ = Column(Unicode(1024))
    AboutSpeaker = Column(Unicode(1024))
    Rem = Column(Unicode(1024))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    bakc_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)


class TCydept(Base):
    __tablename__ = 't_cydept'

    ID = Column(Integer, primary_key=True)
    ID_Parent = Column(Integer)
    Name = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IdManager = Column(Integer)
    IMark = Column(Integer)
    bakc_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)


class TCyequipment(Base):
    __tablename__ = 't_cyequipment'

    ID = Column(Integer, primary_key=True)
    ID_Location = Column(Integer, nullable=False)
    ID_User = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Name = Column(Unicode(32))
    ID_Location_SN = Column(Integer)
    ID_IP = Column(Unicode(16))
    MAC = Column(Unicode(24))
    State = Column(Integer)
    Login = Column(Integer)
    Link = Column(Integer)
    Class = Column(Integer)
    Dx = Column(Integer)
    Dy = Column(Integer)
    iTimeBegin = Column(Integer)
    iTimeLogin = Column(Integer)
    WhiteList = Column(Unicode(1024))
    Rem = Column(Unicode(1024))
    TimeUpdate = Column(Integer)
    PortListen = Column(Integer)
    Type = Column(Integer)
    TimeDelay = Column(Integer)
    KeyCancel = Column(Integer)
    KeyDel = Column(Integer)
    KeyF1 = Column(Integer)
    OnAll = Column(Integer)
    RangeEqus = Column(Unicode(64))
    ListPlaces = Column(Unicode(64))
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    ID_Plan = Column(Integer)
    KeyOk = Column(Integer)


class TCylocation(Base):
    __tablename__ = 't_cylocation'

    ID = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    ID_Parent = Column(Integer)
    Name = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    Rem = Column(Unicode(1024))


class TCylocationex(Base):
    __tablename__ = 't_cylocationex'

    ID_Location = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    Attr = Column(Integer)
    DateBegin = Column(Integer)
    DateEnd = Column(Integer)
    ModeRun = Column(Integer)
    ModeShangJi = Column(Integer)
    EnableDelayCharged = Column(Integer)
    DelayCharged = Column(Integer)
    EnableLimitYuE_SJ = Column(Integer)
    LimitYuE_SJ = Column(Integer)
    EnableLimitYuE_XJ = Column(Integer)
    LimitYuE_XJ = Column(Integer)
    EnableLimitTime_XJ = Column(Integer)
    LimitTime_XJ = Column(Integer)
    EnableWarnYuE = Column(Integer)
    WarnYuE = Column(Integer)
    EnableWarnTime = Column(Integer)
    WarnTime = Column(Integer)
    EnableMinCost = Column(Integer)
    MinCost = Column(Integer)
    Price = Column(Integer)
    PriceMinute = Column(Integer)
    GetEquName = Column(Integer)
    GetEquIp = Column(Integer)
    GetEquMac = Column(Integer)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)


class TCymmx(Base):
    __tablename__ = 't_cymmx'

    ID = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    ID_Data = Column(Integer)
    ID_Type = Column(Integer)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)


class TCymmxdata(Base):
    __tablename__ = 't_cymmxdata'

    ID = Column(Integer, primary_key=True)
    Data = Column(Unicode, nullable=False)
    IdManager = Column(Integer, nullable=False)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)


class TCyplan(Base):
    __tablename__ = 't_cyplan'

    ID = Column(Integer, primary_key=True)
    ID_Curricula = Column(Integer, nullable=False)
    ID_Location = Column(Integer, nullable=False)
    ID_Speaker = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    TimeBegin = Column(Integer)
    TimeEnd = Column(Integer)
    Attr = Column(Integer)
    Charge = Column(Integer)
    PwAccess = Column(Integer)
    PwContinuous = Column(Integer)
    PwDirection = Column(Integer)
    DoorOpen = Column(Integer)
    TimeBeginCheckBegin = Column(Integer)
    imeBeginCheckEnd = Column(Integer)
    TimeEndCheckBegin = Column(Integer)
    TimeEndCheckEnd = Column(Integer)
    RangeUsers = Column(Unicode(1024))
    ListDepts = Column(Unicode(1024))
    RangeEqus = Column(Unicode(1024))
    ListPlaces = Column(Unicode(1024))
    MapUser2Equ = Column(Unicode(1024))
    AboutSpeaker = Column(Unicode(1024))
    Rem = Column(Unicode(1024))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Unicode(254))
    back_up3 = Column(Integer)
    back_up4 = Column(Integer)


class TCyrunningaccount(Base):
    __tablename__ = 't_cyrunningaccount'

    ID = Column(Integer, primary_key=True)
    Param2 = Column(Integer, nullable=False)
    ID_User = Column(Integer, nullable=False)
    IdManager = Column(Integer, nullable=False)
    Time = Column(Integer)
    Type = Column(Integer)
    Money = Column(Integer)
    Param1 = Column(Integer)
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)


class TCytableinfo(Base):
    __tablename__ = 't_cytableinfo'

    ID = Column(Integer, primary_key=True)
    Name = Column(Unicode(50))
    NameTable = Column(Unicode(50))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)
    back_up3 = Column(Integer)
    IdManager = Column(Integer)


class TCytypera(Base):
    __tablename__ = 't_cytypera'

    ID = Column(Integer, primary_key=True)
    IdManager = Column(Integer, nullable=False)
    ID_Parent = Column(Integer)
    Name = Column(Unicode(32))
    TimeUpdate = Column(Integer)
    IMark = Column(Integer)
    back_up1 = Column(Unicode(254))
    back_up2 = Column(Integer)


class TCyuser(Base):
    __tablename__ = 't_cyuser'

    ID = Column(Integer, primary_key=True)
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


t_test_user = Table(
    'test_user', metadata,
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
