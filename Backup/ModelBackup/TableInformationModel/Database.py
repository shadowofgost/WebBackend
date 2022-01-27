from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    ForeignKey,
    Index,
)
from ..UserModel.Database import UserModel
from ..Public.Database import BaseModel

class TableInformationModel(BaseModel):
    name = CharField(default="0", null=True, db_column="Name", max_length=50,blank=True)
    nametable = CharField(default="0", null=True, db_column="NameTable", max_length=50,blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="kaoqin_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cytableinfo"
        indexes = [
            Index(fields=["id"],name="id_index"),
            Index(fields=["name"],name="name_index"),
            Index(fields=["nametable"],name="nametable_index"),
        ]
        ordering = ["id", "name"]
