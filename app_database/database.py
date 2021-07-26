from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


"""
DATABASE URL
"""

from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")

if config("DEBUG") == "1": 

    POSTGRES_USER = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
    POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
    POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
    POSTGRES_DB = config("POSTGRES_DB", cast=str)

    SQLALCHEMY_DATABASE_URL = config("DATABASE_URL", default= f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}")

else:
    
    url = config("DATABASE_URL")
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URL = url

        

engine = create_engine(
    SQLALCHEMY_DATABASE_URL 
)

#, connect_args={"check_same_thread": False}

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
