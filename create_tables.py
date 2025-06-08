"""
Temporary script to initialize the database by creating all tables.
Drops existing tables before creating new ones.
"""

import asyncio
import logging

from app.database import Base, engine
from app.models import Class, Booking

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init_db():
    """
    Drops all existing tables and creates new tables based on the models' metadata.
    """
    try:
        async with engine.begin() as conn:
            logger.info("Dropping all tables...")
            await conn.run_sync(Base.metadata.drop_all)
            logger.info("Creating tables...")
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(init_db())
