from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    Index,
)
from ..UserModel.Database import UserModel
from ..LocationModel.Database import LocationModel
from ..Public.Database import BaseModel

class EquipmentModel(BaseModel):
    name = CharField(
        default="0", null=True, db_column="Name", max_length=128, blank=True
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="equipment_related_to_user",
        db_constraint=False,
    )
    id_user = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_User",
        related_name="equipment_related_to_user_use",
        db_constraint=False,
    )
    id_location = ForeignKey(
        LocationModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Location",
        related_name="equipment_related_to_location",
        db_constraint=False,
    )
    """
    state_choices = [
        (0,"正常空闲")，
        (1,"故障"),
        (2,"其他"),
        (3,"正常使用中"),
        (4,"开放")
    ]
    """
    """
    state = SmallIntegerField(default=0, null=True, db_column='State', blank=True,choices=state_choices)
    """
    state = SmallIntegerField(default=0, null=True, db_column="State", blank=True)
    ########state设备状态，0：正常空闲、1：故障、2：其它、3：正常使用中、4开放########
    """
    login_choices = [
        (0,"未登录"),
        (1,"已登录")
    ]
    """
    """
    login = SmallIntegerField(default=1, null=True, db_column='Login', blank=True,choices=login_choices)
    """
    login = SmallIntegerField(default=1, null=True, db_column="Login", blank=True)
    ########login登录状态，0：未登录、1：已经登录########
    """
    link_choices = [
        (0,"脱机"),
        (1,"在线")
    ]
    """
    """
    link = SmallIntegerField(default=1, null=True, db_column='Link', blank=True,choices=link_choices)
    """
    link = SmallIntegerField(default=1, null=True, db_column="Link", blank=True)
    # link网络状态，0：脱机、1：在线，
    ######## Field renamed because it was a Python reserved word.
    """
    class_field_choices = [
        (0,"pc设备"),
        (1,"刷卡设备")
    ]
    """
    """
    class_field = SmallIntegerField(default=0, null=True, db_column='Class', blank=True,choices=class_field_choices)
    """
    class_field = SmallIntegerField(default=1, null=True, db_column="Class", blank=True)
    ########class_field0：PC设备、2：刷卡设备，#######
    id_location_sn = SmallIntegerField(
        default=0, null=True, db_column="ID_Location_SN", blank=True
    )
    id_ip = CharField(
        default="0", null=True, db_column="ID_IP", max_length=16, blank=True
    )
    mac = CharField(default="0", null=True, db_column="MAC", max_length=24, blank=True)
    dx = IntegerField(default=0, null=True, db_column="Dx", blank=True)
    dy = IntegerField(default=0, null=True, db_column="Dy", blank=True)
    id_plan = IntegerField(default=0, null=True, db_column="ID_Plan", blank=True)
    itimebegin = IntegerField(default=0, null=True, db_column="iTimeBegin", blank=True)
    itimelogin = IntegerField(default=0, null=True, db_column="iTimeLogin", blank=True)
    whitelist = CharField(
        default="0", null=True, db_column="WhiteList", max_length=1024, blank=True
    )
    portlisten = IntegerField(default=0, null=True, db_column="PortListen", blank=True)
    type_field = IntegerField(default=0, null=True, db_column="Type", blank=True)
    timedelay = IntegerField(default=0, null=True, db_column="TimeDelay", blank=True)
    keycancel = SmallIntegerField(
        default=0, null=True, db_column="KeyCancel", blank=True
    )
    keyOk = SmallIntegerField(default=0, null=True, db_column="KeyOk", blank=True)
    keydel = SmallIntegerField(default=0, null=True, db_column="KeyDel", blank=True)
    keyf1 = SmallIntegerField(default=0, null=True, db_column="KeyF1", blank=True)
    onall = SmallIntegerField(default=0, null=True, db_column="OnAll", blank=True)
    rangeequs = CharField(
        default="0", null=True, db_column="RangeEqus", max_length=64, blank=True
    )
    listplaces = CharField(
        default="0", null=True, db_column="ListPlaces", max_length=64, blank=True
    )

    class Meta:
        db_table = "t_cyequipment"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["name"], name="name_index"),
            Index(fields=["login"], name="login_index"),
            Index(fields=["link"], name="link_index"),
            Index(fields=["state"], name="state_index"),
            Index(fields=["class_field"], name="class_field_index"),
        ]
        ordering = ["id", "name"]
