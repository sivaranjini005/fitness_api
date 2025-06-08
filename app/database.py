"""
Database configuration and session management for the Fitness Studio Booking API.
Uses SQLAlchemy's asynchronous engine and session maker.
"""

import os
from collections.abc import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# Load environment variables from a .env file
load_dotenv()

# Get the database URL from environment or fallback to SQLite for development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./fitness.db")

# Create an asynchronous SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Define an asynchronous session factory
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,  # Avoids expiring objects after commit
    class_=AsyncSession,
)

# Declarative base class for models
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to provide a database session.

    Yields:
        AsyncSession: An active SQLAlchemy session for a request lifecycle.
    """
    async with async_session() as session:
        yield session
