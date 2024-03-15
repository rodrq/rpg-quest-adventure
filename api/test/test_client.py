from typing import AsyncGenerator

import pytest
import pytest_asyncio
from async_asgi_testclient import TestClient

from src.main import app


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", "8000"
    scope = {"client": (host, port)}

    async with TestClient(app, scope=scope) as client:
        yield client


@pytest.mark.asyncio
async def test_create_user_no_user(client: TestClient):
    payload = {"username": "", "password": "123"}
    response = await client.post("/api/auth/user", json=payload)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_create_user_no_pw(client: TestClient):
    payload = {"username": "1233", "password": ""}
    response = await client.post("/api/auth/user", json=payload)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_create_user(client: TestClient):
    payload = {"username": "12333", "password": "123"}
    response = await client.post("/api/auth/user", json=payload)
    assert response.status_code == 201
