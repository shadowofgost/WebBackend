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
from ..Public.Database import BaseModel

class TyperaModel(BaseModel):
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=128, blank=True
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="typera_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cytypera"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["id_parent"],name="id_parent_index"),
            Index(fields=["name"], name="name_index"),
        ]
        ordering = ["id", "id_parent","name"]
