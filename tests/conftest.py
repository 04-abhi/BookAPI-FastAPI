import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient

from main import app, get_session
from models import User
from auth import hash_password

# Create test database
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

SQLModel.metadata.create_all(engine)

# Override dependency
def get_test_session():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_test_session

@pytest.fixture(name="client")
def client_fixture():
    return TestClient(app)

@pytest.fixture
def create_user():
    with Session(engine) as session:
        user = User(
            username="testuser",
            hashed_password=hash_password("password"),
            role="admin"
        )
        session.add(user)
        session.commit()
        return user