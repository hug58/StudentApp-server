from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


"""
DATABASE URL
"""

from starlette.config import Config
from starlette.datastructures import Secret

"""
config = Config(".env")


POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

if int(config('DEBUG')) == 1:
    SQLALCHEMY_DATABASE_URL = config("DATABASE_URL", default= f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}")
else:
    pass
"""

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL',"postgres://uzwuwzbmynwxmn:8211f8291dfca7cef7522a35e645df5b4e8f1a91263efa01c9c06b9473f5437c@ec2-52-1-20-236.compute-1.amazonaws.com:5432/dfsvdh03geanmd")



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
