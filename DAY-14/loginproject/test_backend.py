import pytest
from app import app, db
from models import User

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_user_creation(client):
    with app.app_context():
        user = User(username="testuser", password="test123")
        db.session.add(user)
        db.session.commit()

        found = User.query.filter_by(username="testuser").first()
        assert found is not None
        assert found.password == "test123"
