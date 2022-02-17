"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-17 17:19:36
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Services/SchemaMmxData.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-17 17:36:10
# @Software         : Vscode
"""
from typing import List, Optional

from Models import ModelCurricula, ModelLocation, ModelUser
from pydantic import BaseModel, Field, create_model
from sqlalchemy import select
from sqlalchemy.orm import Session, aliased

from .PublicFunctions import (
    format_current_time,
    insert_exclude,
    nullable,
    select_in_exclude,
    select_out_exclude,
    sqlalchemy_to_pydantic,
    update_exclude,
)
