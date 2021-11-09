# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/renthub"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={
        # "check_same_thread": False
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Dependency


def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
