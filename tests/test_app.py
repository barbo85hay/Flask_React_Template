"""Module docstring."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
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
