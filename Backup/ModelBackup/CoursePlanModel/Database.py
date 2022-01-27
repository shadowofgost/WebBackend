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
from ..CurriculaModel.Database import CurriculaModel
from ..LocationModel.Database import LocationModel
from ..Public.Database import BaseModel

class CoursePlanModel(BaseModel):
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="plan_related_to_user",
        db_constraint=False,
    )
    id_curricula = ForeignKey(
        CurriculaModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Curricula",
        related_name="id_curricula",
        db_constraint=False,
    )
    id_location = ForeignKey(
        LocationModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Location",
        related_name="plan_related_to_location",
        db_constraint = False,
    )
    id_speaker = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Speaker",
        related_name="plan_related_to_user_speaker",
        db_constraint=False,
    )
    timebegin = IntegerField(default=0, null=True, db_column="TimeBegin", blank=True)
    timeend = IntegerField(default=0, null=True, db_column="TimeEnd", blank=True)
    attr = SmallIntegerField(default=0, db_column="Attr", blank=True,null=True)
    charge = SmallIntegerField(default=0, db_column="Charge", blank=True,null=True)
    pwaccess = SmallIntegerField(default=0, db_column="PwAccess", blank=True,null=True)
    pwcontinuous = SmallIntegerField(
        default=0, db_column="PwContinuous", blank=True,null=True
    )
    pwdirection = SmallIntegerField(
        default=0, db_column="PwDirection", blank=True,null=True
    )
    dooropen = SmallIntegerField(default=0, db_column="DoorOpen", blank=True,null=True)
    timebegincheckbegin = IntegerField(
        default=0, db_column="TimeBeginCheckBegin", blank=True,null=True
    )
    timebegincheckend = IntegerField(
        default=0, db_column="imeBeginCheckEnd", blank=True,null=True
    )
    timeendcheckbegin = IntegerField(
        default=0, db_column="TimeEndCheckBegin", blank=True,null=True
    )
    timeendcheckend = IntegerField(
        default=0, db_column="TimeEndCheckEnd", blank=True,null=True
    )
    rangeusers = CharField(
        default=0, null=True, db_column="RangeUsers", max_length=1024, blank=True
    )
    listdepts = CharField(
        default=0, null=True, db_column="ListDepts", max_length=1024, blank=True
    )
    rangeequs = CharField(
        default=0, null=True, db_column="RangeEqus", max_length=1024, blank=True
    )
    listplaces = CharField(
        default=0, null=True, db_column="ListPlaces", max_length=1024, blank=True
    )
    mapuser2equ = CharField(
        default=0, null=True, db_column="MapUser2Equ", max_length=1024, blank=True
    )
    aboutspeaker = CharField(
        default=0, null=True, db_column="AboutSpeaker", max_length=1024, blank=True
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="plan_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cyplan"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["id_curricula"], name="id_curricula"),
            Index(fields=["id_speaker"], name="id_speaker_index"),
            Index(fields=["timebegin"], name="timebegin_index"),
            Index(fields=["timeend"], name="timeend_index")
        ]
        ordering = ["id", "id_curricula","id_speaker","timebegin","timeend"]
