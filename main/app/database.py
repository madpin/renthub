from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.ext.asyncio.session import AsyncSession
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/renthub"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, future=True, echo=True,
    connect_args={
    })
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# Base = declarative_base()

# Dependency
# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
