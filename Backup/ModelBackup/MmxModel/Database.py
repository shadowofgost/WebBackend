from django.db.models import (
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    OneToOneField,
    TextField,
    Index,
)
from ..UserModel.Database import UserModel
from ..Public.Database import BaseModel

class MmxModel(BaseModel):
    id_data = IntegerField(default=0, null=True, db_column="ID_Data", blank=True)
    """
    id_type_choices = [
            (1,"PPT")
        ]
    """
    """
    id_type = SmallIntegerField(default=1, null=True, db_column="ID_Type", blank=True,choices=id_type_choices)
    """
    id_type = SmallIntegerField(default=1, null=True, db_column="ID_Type", blank=True)
    ######id_type字段为媒体类型，1为PPT类型######
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="mmx_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cymmx"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["id_data"], name="id_data_index"),
            Index(fields=["id_type"], name="id_type_index"),
        ]
        ordering = ["id", "id_data","id_type"]


class MmxDataModel(BaseModel):
    id_mmxdata = OneToOneField(
        MmxModel,
        to_field="id_mmxdata",
        on_delete=CASCADE,
        primary_key=True,
        db_column="ID",
        related_name="mmxdata_related_to_mmx",
        db_constraint=False,
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="mmxdata_related_to_user",
        db_constraint=False,
    )
    data = TextField(db_column="Data", blank=True)

    class Meta:
        db_table = "t_cymmxdata"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["timeupdate"], name="timeupdate_index"),
        ]
        ordering = ["id"]
