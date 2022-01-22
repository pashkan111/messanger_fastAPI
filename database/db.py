from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import databases

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5433/test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()