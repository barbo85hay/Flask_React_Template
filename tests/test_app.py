"""Module docstring."""

import pytest
from backend.app import app


@pytest.fixture
def client():
    """Docstring."""
    with app.test_client() as client:
        yield client


def test_home(client):
    """Docstring."""
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Hello World!" in rv.data
