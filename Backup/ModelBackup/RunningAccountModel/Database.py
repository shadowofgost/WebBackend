from django.db.models import (
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    DecimalField,
    Index,
)
from ..UserModel.Database import UserModel
from ..CoursePlanModel.Database import CoursePlanModel
from ..Public.Database import BaseModel

class RunningAccountModel(BaseModel):
    param2 = ForeignKey(
        CoursePlanModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="Param2",
        related_name="runningaccount_related_to_plan",
        db_constraint=False,
    )
    ######param2取消交易记录的ID： Type=0x106,讲座、课程编号： Type = 0x201、0x1001######
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="runningaccount_related_to_user",
        db_constraint=False,
    )
    id_user = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_User",
        related_name="runningaccount_related_to_user_use",
        db_constraint=False,
    )
    """
    time_choices = [
        (0,"缺席"),
        (1,"签到"),
        (2,"签退"),
    ]
    """
    """
    time = IntegerField(default=1, null=True, db_column="Time", blank=True,choices=time_choices)
    """
    # 0表示缺席，1表示签到，2表示签退
    time = IntegerField(default=0, null=True, db_column="Time", blank=True)
    """
    type_choices = [
        (0,"交费，存款"),
        (1,"赠费"),
        (2,"退费，取款"),
        (3,"扣费、罚款"),
        (4,"纠错，取消缴费，赠费"),
        (5,"上机费"),
        (6,"考勤"),
    ]
    """
    """
    type_field = SmallIntegerField(default=0, null=True, db_column="Type", blank=True,choices=type_choices)
    """
    type_field = SmallIntegerField(default=0, null=True, db_column="Type", blank=True)
    ######type例如：交费、存款：0x101，赠费： 0x102，退费、取款：0x103，扣费、罚款：0x104，纠错，取消某次缴费、赠费等：0x106，上机费： 0x201,考勤： 0x1001######
    money = DecimalField(default=0, null=True, db_column="Money", blank=True)
    ######money发生的费用，单位为分#####
    param1 = IntegerField(default=0, null=True, db_column="Param1", blank=True)
    ######param1收费管理员的ID：Type=0x101、0x102、0x103、0x104、0x106,上机机位编号： Type = 0x201,门禁考勤机编号：Type = 0x1001######

    class Meta:
        db_table = "t_cyrunningaccount"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["id_user"], name="id_user_index"),
            Index(fields=["param1"], name="param1_index"),
            Index(fields=["param2"], name="param2_index"),
            Index(fields=["time"], name="time_index"),
            Index(fields=["type_field"], name="type_field_index"),
        ]
        ordering = ["id", "id_user","param1", "param2", "time", "type_field"]
