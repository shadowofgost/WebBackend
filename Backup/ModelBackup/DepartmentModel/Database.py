from django.db.models import (
    CharField,
    IntegerField,
    Index
)
from ..Public.Database import BaseModel
# Create your models here.


class DepartmentModel(BaseModel):
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=32, blank=True
    )
    idmanager = IntegerField(default=0, null=True, db_column="IdManager", blank=True)

    class Meta:
        db_table = "t_cydept"
        indexes = [
            Index(fields=["id_parent"], name="id_parent_index"),
            Index(fields=["id"], name="id_index"),
            Index(fields=["name"], name="name_index"),
        ]
        ordering = ["id", "name", "id_parent"]
