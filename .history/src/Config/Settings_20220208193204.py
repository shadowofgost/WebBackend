"""
# @Time             : 2022-01-13 23:29:29
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Config/Settings.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-08 19:30:46
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
# sqlalchemy.url = mysql+pymysql://web:123456@101.132.135.180:3306/WebBackend?charset=utf8
# sqlalchemy.url = mysql+pymysql://web:123456@101.132.135.180:3306/Backup?charset=utf8
# sqlalchemy.url = mssql+pymssql://web:123456@localhost:2233/WebBackend?charset=utf8
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DefaultSettings(BaseSettings):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_MINUTES = 100
    TOKEN_LIFETIME = timedelta(hours=24)
    DEFAULT_DB_ABS_PATH = os.path.join(BASE_DIR, "database/sqlite.db")
    DEFAULT_DATABASE_URL = f"sqlite+aiosqlite:///{DEFAULT_DB_ABS_PATH}"
    # Set True if database is SQLite otherwise False
    RENDER_AS_BATCH = True
    LOGIN_URL = "/auth/login"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


class DevSetting(BaseSettings):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_MINUTES = 100
    TOKEN_LIFETIME = timedelta(hours=24)
    DATABASE_TYPE = "mysql"
    DATABASE_CONNECT = "pymysql"
    DATABASE_NAME = "WebBackend"
    DATABASE_USER_NAME = "web"
    DATABASE_USER_PASSWORD = "123456"
    DATABASE_HOST = "101.132.135.180"
    DATABASE_PORT = "3306"
    
    DEFAULT_DB_ABS_PATH = os.path.join(BASE_DIR, "database/sqlite.db")
    DEFAULT_DATABASE_URL = f"sqlite+aiosqlite:///{DEFAULT_DB_ABS_PATH}"
    # Set True if database is SQLite otherwise False
    RENDER_AS_BATCH = True
    LOGIN_URL = "/auth/login"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


class ProductionSetting(BaseSettings):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_MINUTES = 100
    TOKEN_LIFETIME = timedelta(hours=24)
    DEFAULT_DB_ABS_PATH = os.path.join(BASE_DIR, "database/sqlite.db")
    DEFAULT_DATABASE_URL = f"sqlite+aiosqlite:///{DEFAULT_DB_ABS_PATH}"
    # Set True if database is SQLite otherwise False
    RENDER_AS_BATCH = True
    LOGIN_URL = "/auth/login"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


@lru_cache()
def get_settings():
    return Settings()
