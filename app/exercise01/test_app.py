from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)


def test_read_all_with_no_post():
    """
    Test if read all is working,
    even without any post.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() is not None


def test_create():
    """Check if create method is working"""
    response = client.post("/message?message=apple")
    assert response.status_code == 201


def test_read_all():
    """Test if read all is working"""
    client.post("/message?message=watermelon")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() is not None


def test_read():
    """Test if read by id is working"""
    response = client.get("/message/0")
    assert response.status_code == 200
    assert response.json() is not None
    assert "Hello, World!" in response.json()


def test_update():
    """
    Test if a message with the passed id 
    will be update
    """
    response = client.put("/message/0?message=Hallo, Welt!")
    read = client.get("/")
    assert response.status_code == 200
    assert "Hello, World!" not in response.json()
    assert read.json().get("message_0") == "Hallo, Welt!"


def test_delete():
    """
    Test if the message with the passed id 
    will be deleted
    """
    client.post("/message?message=lemon")
    response = client.delete("/message/0")
    assert response.status_code == 200
    assert response.json() is not None
    assert not "message_0" in response.json()


def test_kill_them_all():
    """
    Test if all messages except the first
    will be deleted
    """
    client.post("/message?message=lemon")
    client.post("/message?message=orange")
    response = client.delete("/")
    assert response.status_code == 200
    assert response.json() is not None
    assert not "message_0" in response.json()
