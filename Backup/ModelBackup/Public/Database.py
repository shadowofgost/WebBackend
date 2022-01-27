from django.db.models import (
    Model,
    CharField,
    IntegerField,
    BigAutoField,
)

class BaseModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True, unique=True, blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64, blank=True)
    introduction = CharField(default="0", null=True, max_length=254, blank=True, db_column = "Introduction")
    imark = IntegerField(default=0, null=True, db_column="IMark", blank=True)
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up3 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up4 = IntegerField(default=0, blank=True, null=True)
    back_up5 = IntegerField(default=0, null=True, blank=True)
    back_up6 = IntegerField(default=0, null=True, blank=True)
    class Meta:
        abstract = True
