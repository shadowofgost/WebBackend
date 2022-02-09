"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-01 16:09:31
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/Public.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-01 19:14:06
# @Software         : Vscode
"""
from sqlalchemy import table
from sqlalchemy.orm import Session
from typing import Container, Optional, Type
from ..Models import DeleteMultipleGetSchema,ORM,DeleteMultipleTableSchema,DeleteSingleTableSchema


def delete(
    session: Session, idmanager: int, model: str, schema: DeleteMultipleGetSchema
) -> Type[dict]:
    model_instance=ORM(model,session)
    if schema.n==1:
        try:
            table_dalete_schema=
