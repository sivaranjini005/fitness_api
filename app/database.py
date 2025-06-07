import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from collections.abc import AsyncGenerator
from dotenv import load_dotenv

load_dotenv() #ensure environment variables load first

#Get the database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./fitness.db")

#create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

#creating async session factory
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

#Base class for database models
Base = declarative_base()

#Dependency to get a session which is used later in routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

