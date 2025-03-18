import pytest
from httpx import AsyncClient
from chat_room.main import app

@pytest.mark.anyio
async def test_send_message():
  async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.post("/send", json={"text": "Hello"})
        assert response.status_code == 200
        assert response.json()["text"] == "Hello"

@pytest.mark.anyio
async def test_get_history():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:

        response = await client.get("/history")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
