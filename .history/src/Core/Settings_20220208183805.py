"""
# @Time             : 2022-01-13 23:29:29
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Core/Settings.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-08 18:32:16
# @LastAuthor       : Albert Wang
"""
import os
from datetime import timedelta
from functools import lru_cache

from pydantic import BaseModel, BaseSettings
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.Models import Base as user_base

Base = user_base
SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://web:123456@101.132.135.180:3306/WebBackend?charset=utf8"
)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



class Settings(BaseSettings):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 100
    TOKEN_LIFETIME = timedelta(hours=24)

    DB_ABS_PATH = os.path.join(BASE_DIR, "database/sqlite.db")
    DATABASE_URL = f"sqlite+aiosqlite:///{DB_ABS_PATH}"

    # Set True if database is SQLite otherwise False
    RENDER_AS_BATCH = True

    LOGIN_URL = "/auth/login"

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


@lru_cache()
def get_settings():
    return Settings()
