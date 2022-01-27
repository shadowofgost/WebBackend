from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql://root:123456@localhost:3306/fastapi_db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8', echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)

Base = declarative_base(bind=engine, name='Base')