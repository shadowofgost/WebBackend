"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 22:19:24
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/ServiceCoursePlan.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 16:56:02
# @Software         : Vscode
"""
from .PublicService import (
    service_delete,
    service_insert,
    service_update,
    service_select,
    error_service_null,
    error_service_validation,
)
from sqlalchemy.orm import Session
from pydantic import BaseModel
from Models import (
    ModelCoursePlanSelectInSingleTableSchema,
    ModelCoursePlanSelectOutSingleTableSchema,
    ModelCoursePlan,
    ModelUser,
    ModelLocation,
)
from typing import List, Optional
from sqlalchemy import select
ModelCoursePlanUpdateSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelCoursePlan, update_exclude
)
ModelCoursePlanUpdateSingleGetSchemaBase = create_model(
    "ModelCoursePlanUpdateSingleGetSchemaBase",
    __base__=ModelCoursePlanUpdateSingleGetSchemaBase,
)


class ModelCoursePlanUpdateSingleGetSchema(ModelCoursePlanUpdateSingleGetSchemaBase):
    ID_Speaker_NoUser: int

    class Config:
        orm_mode = True


class ModelCoursePlanUpdateMultipleGetSchema(BaseModel):
    data: List[ModelCoursePlanUpdateSingleGetSchema]
    n: int


class ModelCoursePlanUpdateSingleTableSchema(ModelCoursePlanUpdateSingleGetSchemaBase):
    TimeUpdate: int = format_current_time()
    IdManager: int


class ModelCoursePlanUpdateMultipleTableSchema(BaseModel):
    data: List[ModelCoursePlanUpdateSingleTableSchema]
    n: int


ModelCoursePlanInsertSingleGetSchemaBase = sqlalchemy_to_pydantic(
    ModelCoursePlan, insert_exclude, ModelCoursePlan_nullable_columns
)
ModelCoursePlanInsertSingleGetSchemaBase = create_model(
    "ModelCoursePlanInsertSingleGetSchemaBase",
    __base__=ModelCoursePlanInsertSingleGetSchemaBase,
)


class ModelCoursePlanInsertSingleGetSchema(ModelCoursePlanInsertSingleGetSchemaBase):
    ID_Speaker_NoUser: int

    class Config:
        orm_mode = True


class ModelCoursePlanInsertMultipleGetSchema(BaseModel):
    data: List[ModelCoursePlanInsertSingleGetSchema]
    n: int


class ModelCoursePlanInsertSingleTableSchema(ModelCoursePlanInsertSingleGetSchemaBase):
    TimeUpdate: int = format_current_time()
    Idmanager: int


class ModelCoursePlanInsertMultipleTableSchema(BaseModel):
    data: List[ModelCoursePlanInsertSingleTableSchema]
    n: int


ModelCoursePlanSelectOutSingleTableSchemaBase = sqlalchemy_to_pydantic(
    ModelCoursePlan, select_out_exclude
)
ModelCoursePlanSelectOutSingleTableSchemaBase = create_model(
    "ModelCoursePlanSelectOutSingleTableSchemaBase",
    __base__=ModelCoursePlanSelectOutSingleTableSchemaBase,
)


class ModelCoursePlanSelectOutSingleTableSchema(
    ModelCoursePlanSelectOutSingleTableSchemaBase
):
    ID_Curricula_Name: Optional[str] = Field(
        default=None, title="课程名称", description="这是这节课程安排课对应的课程名称"
    )
    ID_Location_Name: Optional[str] = Field(
        default=None, title="地点名称", description="这是这节课程安排课对应的地点名称"
    )
    ID_Speaker_Name: Optional[str] = Field(
        default=None, title="老师名称", description="这是这节课程安排课对应的上课老师的姓名"
    )
    ID_Speaker_NoUser: Optional[int] = Field(
        default=None, title="老师/演讲者的教职工号", description="这是这节课程安排课对应的老师/演讲者的教职工号"
    )
    ID_Manager_Name: Optional[str] = Field(
        default=None, title="修改者的姓名", description="这次课程信息最新一次修改的修改者姓名"
    )

    class Config:
        orm_mode = True


ModelCoursePlanSelectInSingleTableSchema = sqlalchemy_to_pydantic(
    ModelCoursePlan, select_in_exclude, []
)
ModelCoursePlanSelectInSingleTableSchema = create_model(
    "ModelCoursePlanSelectInSingleTableSchema",
    __base__=ModelCoursePlanSelectInSingleTableSchema,
)
##TODO:修改sql查询语句因为超过三个join使得mysql的性能会大幅下降。
user1 = aliased(ModelUser)
ModelCoursePlan_sub_stmt = (
    select(
        ModelCoursePlan,
        ModelCurricula.Name.label("ID_Curricula_Name"),
        ModelLocation.Name.label("ID_Location_Name"),
        ModelUser.Name.label("ID_Speaker_Name"),
        ModelUser.NoUser.label("ID_Speaker_NoUser"),
        user1.Name.label("ID_Manager_Name"),
    )
    .join(
        ModelCurricula,
        ModelCurricula.ID == ModelCoursePlan.ID_Curricula,
        isouter=True,
    )
    .join(ModelUser, ModelUser.ID == ModelCurricula.ID_Speaker, isouter=True)
    .join(
        ModelLocation,
        ModelLocation.ID == ModelCoursePlan.ID_Location,
        isouter=True,
    )
    .join(user1, user1.ID == ModelCoursePlan.IdManager, isouter=True)
).subquery()


def get_courseplan(
    session: Session,
    id_manager: int,
    attr: int,
    service_type: int,
    schema: ModelCoursePlanSelectInSingleTableSchema,
    extra_attr: int = 0,
):
    """
    get_courseplan _summary_

    _extended_summary_

    Parameters
    ----------
    session : Session
        [description]
    id_manager : intint
        [description]
    attr : int
        [默认是使用0，用户，1，管理员，2，超级管理员]
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过Nouser进行查询]
    schema : [type], optional
        [description], by default None
        [description], by default None
    extra_attr : int, optional
        [额外的权限，用于service层用户的角色的判断,0表示学生，1表示老师], by default 0

    Returns
    -------
    [type]
        [description]
    """
    model_name="ModelCoursePlan"
    if attr == 1 or 2:
        return service_select(
            session, id_manager, model_name, service_type, schema
        )
    elif attr == 0:
        if extra_attr == 0:
            return orm_for_student(session, id_manager, service_type, schema)
        elif extra_attr == 1:
            schema.ID_Speaker = id_manager
            if service_type == 0:
                return service_select(session, id_manager, model_name, 3, schema)
            else:
                return service_select(
                    session, id_manager, model_name, service_type, schema
                )
