import pytest
from flask import Flask
from flask.testing import FlaskClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adjust import paths according to your project structure
# Assuming the application factory is named `create_app` in `app/__init__.py`
# and the SQLAlchemy Base and Student model are defined in `app/models.py`
# and the database module exposing `engine` and `SessionLocal` is `app/database.py`
from app import create_app
from app.models import Base, Student
import importlib

@pytest.fixture
def app() -> Flask:
    """Create and configure a new Flask app instance for each test."""
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    }
    app = create_app(test_config)

    # Set up a pure SQLAlchemy engine and sessionmaker
    engine = create_engine("sqlite:///:memory:", future=True, echo=False)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine, future=True)

    # Monkey‑patch the application's database module to use the test engine/session
    db_module = importlib.import_module("app.database")
    setattr(db_module, "engine", engine)
    setattr(db_module, "SessionLocal", SessionLocal)

    yield app

    # Teardown: drop all tables
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Provide a Flask test client."""
    return app.test_client()


def test_delete_student_redirect_and_removal(client: FlaskClient):
    # Import the SessionLocal that was patched onto the app's database module
    db_module = importlib.import_module("app.database")
    SessionLocal = getattr(db_module, "SessionLocal")

    # Insert a student record directly via SQLAlchemy
    with SessionLocal() as session:
        student = Student(name="Test Student", email="test@example.com")
        session.add(student)
        session.commit()
        student_id = student.id

    # Issue a GET request to the delete endpoint
    response = client.get(f"/delete?id={student_id}")

    # Verify the response is a redirect (302) to the index route
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")

    # Confirm the student record has been removed from the database
    with SessionLocal() as session:
        deleted_student = session.get(Student, student_id)
        assert deleted_student is None