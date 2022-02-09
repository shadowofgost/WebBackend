from ..Models import (
ORM,
ModelTyperaUpdateMultipleGetSchema,
ModelTyperaUpdateSingleTableSchema,
ModelTyperaUpdateMultipleTableSchema,
ModelTyperaInsertMultipleGetSchema,
ModelTyperaInsertSingleTableSchema,
ModelTyperaInsertMultipleTableSchema,
ModelTyperaSelectInSingleTableSchema,
PublicValuesAndSchemas
)
from sqlalchemy.orm import Session



def update(model : str, schema : ModelTyperaUpdateMultipleGetSchema, session : Session,
           id):
    model_instance = ORM(model, session)
    if schema.n == 1:
        try:
            update_table_schema = ModelTyperaUpdateSingleTableSchema(IdManager=id)
            result = model_instance.update(update_table_schema)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
    else:
        try:
            update_table_schema = ModelTyperaUpdateMultipleTableSchema(**schema.dict())
            result = model_instance.update(update_table_schema, multiple=True)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
    return result

def insert(model : str, schema : ModelTyperaInsertMultipleGetSchema, session : Session,
           id):
    model_instance = ORM(model, session)
    if schema.n == 1:
        try:
            insert_table_schema = ModelTyperaInsertSingleTableSchema(Idmanager=id)
            result = model_instance.update(insert_table_schema)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
    else:
        try:
            insert_table_schema = ModelTyperaInsertMultipleTableSchema(**schema.dict())
            result = model_instance.update(insert_table_schema, multiple=True)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
    return result

def service_select(
    session : Session, id_manager: int, model: str, service_type: int,
    schema = None
):
    """
    service_type : int
        [根据输入数据判断服务类型,0表示查询所有的数据，1表示查询的是通过id查询数据，2表示通过name查询数据，3表示通过schema查询特定值的数据，4表示通过学号/序列号查询账户]

    Returns
    -------
    dict[str,str]
        [description]
    """
    model_instance = ORM(model, session)
    if service_type == 0:
        return model_instance.condition_select()
    elif service_type == 1:
        select_in_schema = PublicValuesAndSchemas.model_dict[model]["select_single_schema"]
        try:
            table_schema = select_in_schema(ID=schema.id)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.multiple_require_select(table_schema)
    elif service_type == 2:
        try:
            name = schema.Name
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.name_select(name)
    elif service_type == 3:
        select_in_schema = PublicValuesAndSchemas.model_dict[model]["select_single_schema"]
        try:
            table_schema = select_in_schema(**schema.dict())
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.multiple_require_select(table_schema)
    elif service_type == 4:
        select_in_schema = PublicValuesAndSchemas.model_dict[model]["select_single_schema"]
        try:
            table_schema = select_in_schema(ID=schema.Nouser)
        except Exception as e:
            return PublicValuesAndSchemas.error_schema_validation
        return model_instance.multiple_require_select(table_schema)
    else:
        pass
