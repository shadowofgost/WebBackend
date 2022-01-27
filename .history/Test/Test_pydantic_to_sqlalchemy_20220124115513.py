"""
# @Time             : 2022-01-24 11:45:11
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/Test/Test_pydantic_to_sqlalchemy.py
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-24 11:45:12
# @LastAuthor       : Albert Wang
"""
from src.Models import ModelUserExtension,
PydanticUserex = sqlalchemy_to_pydantic(
    db_model=ModelUserExtension, exclude=exclude, nullable=nullable
)
print(PydanticUserex.__dict__)
