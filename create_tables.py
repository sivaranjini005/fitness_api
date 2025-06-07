#temporary script to create tables
import asyncio
from app.database import Base, engine
from app.models import Class, Booking

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("database initialized")

asyncio.run(init_db())