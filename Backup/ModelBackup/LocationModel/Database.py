from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    OneToOneField,
    Index,
)
from ..UserModel.Database import UserModel
from ..Public.Database import BaseModel

class LocationModel(BaseModel):
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=128, blank=True
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="location_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cylocation"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["name"], name="name_index"),
            Index(fields=["id_parent"], name="id_parent_index"),
        ]
        ordering = ["id", "name"]


class LocationExtensionModel(BaseModel):
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="locationex_related_to_user",
        db_constraint=False,
    )
    id_location = OneToOneField(
        LocationModel,
        to_field="id",
        on_delete=CASCADE,
        primary_key=True,
        db_column="ID_Location",
        related_name="locationex_related_to_location",
        db_constraint=False,
    )
    attr = SmallIntegerField(default=0, null=True, db_column="Attr", blank=True)
    datebegin = IntegerField(default=0, null=True, db_column="DateBegin", blank=True)
    dateend = IntegerField(default=0, null=True, db_column="DateEnd", blank=True)
    moderun = IntegerField(default=0, null=True, db_column="ModeRun", blank=True)
    modeshangji = IntegerField(
        default=0, null=True, db_column="ModeShangJi", blank=True
    )
    enabledelaycharged = IntegerField(
        default=0, null=True, db_column="EnableDelayCharged", blank=True
    )
    delaycharged = IntegerField(
        default=0, null=True, db_column="DelayCharged", blank=True
    )
    enablelimityue_sj = IntegerField(
        default=0, null=True, db_column="EnableLimitYuE_SJ", blank=True
    )
    limityue_sj = IntegerField(
        default=0, null=True, db_column="LimitYuE_SJ", blank=True
    )
    enablelimityue_xj = IntegerField(
        default=0, null=True, db_column="EnableLimitYuE_XJ", blank=True
    )
    limityue_xj = IntegerField(
        default=0, null=True, db_column="LimitYuE_XJ", blank=True
    )
    enablelimittime_xj = IntegerField(
        default=0, null=True, db_column="EnableLimitTime_XJ", blank=True
    )
    limittime_xj = IntegerField(
        default=0, null=True, db_column="LimitTime_XJ", blank=True
    )
    enablewarnyue = IntegerField(
        default=0, null=True, db_column="EnableWarnYuE", blank=True
    )
    warnyue = IntegerField(default=0, null=True, db_column="WarnYuE", blank=True)
    enablewarntime = IntegerField(
        default=0, null=True, db_column="EnableWarnTime", blank=True
    )
    warntime = IntegerField(default=0, null=True, db_column="WarnTime", blank=True)
    enablemincost = IntegerField(
        default=0, null=True, db_column="EnableMinCost", blank=True
    )
    mincost = IntegerField(default=0, null=True, db_column="MinCost", blank=True)
    price = IntegerField(default=0, null=True, db_column="Price", blank=True)
    priceminute = IntegerField(
        default=0, null=True, db_column="PriceMinute", blank=True
    )
    getequname = IntegerField(default=0, null=True, db_column="GetEquName", blank=True)
    getequip = IntegerField(default=0, null=True, db_column="GetEquIp", blank=True)
    getequmac = IntegerField(default=0, null=True, db_column="GetEquMac", blank=True)

    class Meta:
        db_table = "t_cylocationex"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["attr"], name="attr_index"),
            Index(fields=["datebegin"],name="datebegin_index"),
            Index(fields=["dateend"], name="dateend_index")
        ]
        ordering = ["id", "attr", "datebegin", "dateend"]
