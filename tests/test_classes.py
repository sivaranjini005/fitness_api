# tests/test_classes.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app
from httpx import ASGITransport


@pytest.mark.asyncio
async def test_get_classes():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/classes/")
    assert response.status_code == status.HTTP_200_OK
