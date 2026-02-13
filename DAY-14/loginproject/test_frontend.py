import pytest
from app import app, db
from models import User

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        user = User(username="admin", password="1234")
        db.session.add(user)
        db.session.commit()

        yield app.test_client()
        db.drop_all()

def test_login_success(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "1234"
    })
    assert b"Login Successful" in response.data

def test_login_failure(client):
    response = client.post("/login", data={
        "username": "wrong",
        "password": "wrong"
    })
    assert b"Invalid Credentials" in response.data

def test_login_page_load(client):
    response = client.get("/login")
    assert response.status_code == 200
