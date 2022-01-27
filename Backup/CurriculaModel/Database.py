from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    Index,
    BigAutoField,
)
from ..UserModel.Database import UserModel
from ..LocationModel.Database import LocationModel
from ..Public.Database import BaseModel

class CurriculaModel(BaseModel):
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="curricula_related_to_user",
        db_constraint=False,
    )
    id_location = ForeignKey(
        LocationModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Location",
        related_name="curricula_related_to_location",
    )
    id_speaker = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Speaker",
        related_name="curricula_related_to_user_speaker",
        db_constraint=False,
    )
    """
    attr_choices = [
        (1,"实验课程"),
        (2,"普通上课课程"),
        (3,"讲座课程"),
        (4,"考勤课程")
    ]
    """

    """
    attr = SmallIntegerField(
        default=2, null=True, db_column='Attr', blank=True, choices = attr_choices)
    """
    attr = SmallIntegerField(default=2, null=True, db_column="Attr", blank=True)
    #####attr1代表实验类型、2代表普通上课类型、3讲座考勤类型，必须有值实验类型：奇数刷卡派位，偶数刷卡下机，并记录派位编号上课考勤类型：刷卡记录刷卡机编号讲座考勤类型：刷卡记录刷卡机编号######
    """
    charge_choices = [
        (0,"免费"),
        (1,"收费"),
        (2,"开放")
    ]
    """
    """
    charge = SmallIntegerField(
        default=0, null=True, db_column='Charge', blank=True,choices = charge_choices)
    """
    charge = SmallIntegerField(default=0, null=True, db_column="Charge", blank=True)
    ######charge免费0、收费1、开放2，必须有值######
    """
    pwaaccess_choices = [
        (0,"不派位"),
        (1,"派位")
    ]
    """
    """
    pwaaccess = SmallIntegerField(
        default=1, null=True, db_column='PwAccess', blank=True,choices = pwaaccess_choices)
    """
    pwaaccess = SmallIntegerField(
        default=1, null=True, db_column="PwAccess", blank=True
    )
    ######pwaccess不派位0、刷卡派位1（派位指用户刷卡时系统指定座位）######
    """'
    pwcontinuous_choices = [
        (0,"连续派位"),
        (1,"随机派位")
    ]
    """
    """
    pwcontinuous = SmallIntegerField(
        default=1, null=True,db_column='PwContinuous', blank=True,choices = pwcontinuous_choices)
    """
    pwcontinuous = SmallIntegerField(
        default=1, null=True, db_column="PwContinuous", blank=True
    )
    ######pwcontinuous连续派位0、随机派位1######
    """
    pwdirection_choices = [
        (0,"顺序派位"),
        (1,"逆序派位")
    ]
    """
    """
    pwdirection = SmallIntegerField(
        default=1, null=True,db_column='PwDirection', blank=True,choices = pwdirection_choices)
    """
    pwdirection = SmallIntegerField(
        default=1, null=True, db_column="PwDirection", blank=True
    )
    # pwdirection顺序派位0、逆序派位1（当设置为随机派位时本功能无效）######@
    """
    dooropen_choices = [
        (0,"开门"),
        (1,"不开门")
    ]
    """
    """
    dooropen = SmallIntegerField(
        default=1, null=True, db_column='DoorOpen', blank=True,choices = dooropen_choices)
    """
    dooropen = SmallIntegerField(default=0, null=True, db_column="DoorOpen", blank=True)
    ######dooropen匹配的用户刷卡是否开门，0开门，1不开门######
    name = CharField(
        default="0", null=True, db_column="Name", max_length=32, blank=True
    )
    timebegin = IntegerField(default=0, null=True, db_column="TimeBegin", blank=True)
    timeend = IntegerField(default=0, null=True, db_column="TimeEnd", blank=True)
    timebegincheckbegin = IntegerField(
        default=0, null=True, db_column="TimeBeginCheckBegin", blank=True
    )
    ######0代表无效######
    timebegincheckend = IntegerField(
        default=0, null=True, db_column="TimeBeginCheckEnd", blank=True
    )
    ######0代表无效######
    timeendcheckbegin = IntegerField(
        default=0, null=True, db_column="TimeEndCheckBegin", blank=True
    )
    ######0代表无效######
    timeendcheckend = IntegerField(
        default=0, null=True, db_column="TimeEndCheckEnd", blank=True
    )
    ######0代表无效######
    rangeusers = CharField(
        default="0", null=True, db_column="RangeUsers", max_length=1024, blank=True
    )
    listdepts = CharField(
        default="0", null=True, db_column="ListDepts", max_length=1024, blank=True
    )
    rangeequs = CharField(
        default="0", null=True, db_column="RangeEqus", max_length=1024, blank=True
    )
    listplaces = CharField(
        default="0", null=True, db_column="ListPlaces", max_length=1024, blank=True
    )
    mapuser2equ = CharField(
        default="0", null=True, db_column="MapUser2Equ", max_length=1024, blank=True
    )
    aboutspeaker = CharField(
        default="0", null=True, db_column="AboutSpeaker", max_length=1024, blank=True
    )


    class Meta:
        db_table = "t_cycurricula"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["name"], name="name_index"),
            Index(fields=["id_speaker"], name="id_speaker_index"),
            Index(fields=["id_manager"], name="id_manager_index"),
            Index(fields=["timebegin"], name="timebegin_index"),
            Index(fields=["timeend"], name="timeend_index"),
        ]
        ordering = ["id", "name", "id_speaker"]
