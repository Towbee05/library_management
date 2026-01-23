import pytest 

from httpx import AsyncClient, ASGITransport
from app.main import app

from faker import Faker

fake= Faker()
@pytest.mark.anyio
async def test_signup():
    payload = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "is_admin": fake.boolean(),
        "lastLogin": fake.date_time_this_year().isoformat()
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/auth/signup", json=payload)
    assert response.status_code == 201
    