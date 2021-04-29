import pytest
from molten import testing

from app import app


@pytest.fixture(scope="session")
def client():
    return testing.TestClient(app)


def test_can_create_todos(client: object) -> object:
    response = client.post(
        app.reverse_uri("create_todo"),
        json={"description": "example todo"},
    )

    assert response.status_code == 200
    assert response.json()["description"] == "example todo"
