from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    OneToOneField,
    BinaryField,
    EmailField,
    Index,
)
from ..DepartmentModel.Database import DepartmentModel
from ..Public.Database import BaseModel

class UserModel(BaseModel):
    deptid = ForeignKey(
        DepartmentModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="Deptid",
        related_name="related_to_department",
        db_constraint=False,
    )
    """
    sex_choices=[
        (0,"女"),
        (1,"男"),
    ]
    """
    """
    sex = SmallIntegerField(default=1, null=True, db_column="Sex",choices=sex_choices)
    """
    sex = SmallIntegerField(default=1, null=True, db_column="Sex")
    ##########sex 的值只能为0（女）或者1（男）##########
    """
    attr_choices=[
        (0,"超级管理员"),
        (1,"管理员"),
        (2,"教务处管理员"),
        (3,"老师"),
        (4,"学生"),
        (5,"普通用户"),
        (6,"辅导员"),
    ]
    """
    """
    attr = SmallIntegerField(default=1, null=True, db_column="Attr",choices=attr_choices)
    """
    attr = SmallIntegerField(default=5, null=True, db_column="Attr")
    ##########attr 用户管理权限， 0普通用户、1管理员、2超级管理员（可对管理员进行管理）##########
    attrjf = SmallIntegerField(default=0, null=True, db_column="AttrJf")
    ##########机房管理权限， 0普通用户、1管理员、2超级管理员（可对管理员进行管理）##########
    nocard = CharField(default="0", null=True, db_column="Nocard", max_length=32)
    nouser = CharField(default="0", null=True, db_column="NoUser", max_length=32,unique=True)
    name = CharField(default="0", null=True, db_column="Name", max_length=32)
    psw = CharField(default="0", null=True, db_column="Psw", max_length=32)
    yue = IntegerField(default=0, null=True, db_column="Yue", blank=True)
    ##用户余额1，单位为分；（默认）##
    yue2 = IntegerField(default=0, null=True, db_column="Yue2", blank=True)
    ##用户余额2，单位为分；（扩展于特殊需求）##
    email = EmailField(
        default=None, null=True, db_column="Email", max_length=254, blank=True
    )
    phone = IntegerField(default=0, null=True, db_column="Phone", blank=True)
    idmanager = IntegerField(default=0, null=True, db_column="IdManager", blank=True)
    localid = CharField(
        default="0", null=True, db_column="LocalID", max_length=1024, blank=True
    )


    class Meta:
        db_table = "t_cyuser"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["nocard"], name="nocard_index"),
            Index(fields=["nouser"], name="nouser_index"),
            Index(fields=["name"], name="name_index"),
            Index(fields=["psw"], name="psw_index"),
            Index(fields=["deptid"], name="deptid_index"),
            Index(fields=["sex"], name="sex_index"),
            Index(fields=["attr"], name="attr_index"),
            Index(fields=["email"], name="email_index"),
            Index(fields=["phone"], name="phone_index"),
        ]
        ordering = ["id", "nocard", "nouser", "name"]


class UserExtensionModel(BaseModel):
    id_user = OneToOneField(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        primary_key=True,
        db_column="ID",
        related_name="userex_related_to_user_information",
        db_constraint=False,
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="userex_related_to_user",
        db_constraint=False,
    )
    photo = BinaryField(db_column="FaceFearture", blank=True)


    class Meta:
        db_table = "t_cyuserex"
        indexes = [
            Index(fields=["id"], name="id_index"),
        ]
        ordering = ["id"]
