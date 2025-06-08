"""Test module for class booking API functionality."""

import sys
import os

# Setting path for app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from httpx import AsyncClient
from sqlalchemy import delete
import pytest_asyncio
from datetime import datetime
from app.main import app
from app.database import async_session
from app.models import Class


@pytest_asyncio.fixture(autouse=True)
async def setup_class_data():
    """
    Fixture to set up a clean test environment before each test.

    - Clears the `Class` table.
    - Adds a sample class with known values for predictable testing.
    """
    async with async_session() as db:
        # Delete all classes (async style)
        await db.execute(delete(Class))
        await db.commit()

        # Add sample class with known ID (for test predictability)
        sample_class = Class(
            id=1,
            name="Yoga",
            instructor="vasant",
            start_time=datetime(2025, 6, 10, 10, 0, 0),
            available_slots=2,
        )
        db.add(sample_class)
        await db.commit()


@pytest.mark.asyncio
async def test_successful_booking():
    """
    Test case: Book a class successfully via the API.

    Sends a POST request to the booking endpoint with valid data
    and asserts that the response status code is 201 (Created).
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "client_name": "Manoj",
            "client_email": "manoj@gmail.com",
            "class_id": 1,
        }
        response = await ac.post("/bookings/book/", json=payload)
        assert response.status_code == 201
