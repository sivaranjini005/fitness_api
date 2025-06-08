"""Test module for retrieving class data from the API."""

import sys
import os

# Extend the system path to include the app directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from app.main import app


@pytest.mark.asyncio
async def test_get_classes():
    """
    Test case: Retrieve the list of available classes.

    Sends a GET request to the /classes/ endpoint and
    verifies the response status code is 200 OK.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/classes/")

    assert response.status_code == status.HTTP_200_OK
