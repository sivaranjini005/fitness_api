"""
Script to seed initial fitness classes into the database with IST timezone-aware start times.
"""

import asyncio
from datetime import datetime, timedelta, time
import pytz
import logging

from app.database import async_session
from app.models import Class

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set IST timezone
IST = pytz.timezone("Asia/Kolkata")


def get_ist_datetime(days_from_now: int, hour: int) -> datetime:
    """
    Returns a timezone-aware datetime object in IST,
    'days_from_now' days ahead, at 'hour' o'clock.

    Args:
        days_from_now (int): Number of days ahead of current UTC date.
        hour (int): Hour of the day (24-hour format).

    Returns:
        datetime: Timezone-aware IST datetime.
    """
    future_date = (datetime.utcnow() + timedelta(days=days_from_now)).date()
    naive_datetime = datetime.combine(future_date, time(hour=hour, minute=0))
    ist_datetime = IST.localize(naive_datetime)
    return ist_datetime


async def seed_classes():
    """
    Insert sample class data into the database.
    Uses asynchronous session to add multiple Class records.
    """
    try:
        async with async_session.begin() as session:
            class_data = [
                Class(
                    name="Yoga",
                    instructor="Aarav",
                    start_time=get_ist_datetime(1, 9),  # Tomorrow 9 AM IST
                    available_slots=1,
                ),
                Class(
                    name="Zumba",
                    instructor="Meera",
                    start_time=get_ist_datetime(2, 7),  # Day after tomorrow 7 AM IST
                    available_slots=15,
                ),
                Class(
                    name="HIIT",
                    instructor="Roshan",
                    start_time=get_ist_datetime(3, 6),  # 3 days from now 6 AM IST
                    available_slots=12,
                ),
            ]

            session.add_all(class_data)

        logger.info("Seed data inserted successfully.")
    except Exception as e:
        logger.error(f"Failed to insert seed data: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(seed_classes())
