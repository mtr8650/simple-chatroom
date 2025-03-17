from fastapi.testclient import TestClient
from main import app  # Import FastAPI app with routes included

client = TestClient(app)  # Create a test client for API testing

def test_send_message():
    """Test sending a message to the chat"""
    response = client.post("/send", json={"text": "Hello, pytest!"})
    assert response.status_code == 200
    assert response.json() == {"message": "Message received"}

def test_chat_history():
    """Test retrieving chat history"""
    response = client.get("/history")  # Using GET instead of POST for history
    assert response.status_code == 200
    assert "history" in response.json()
    assert isinstance(response.json()["history"], list)
