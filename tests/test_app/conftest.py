import os

from fastapi.testclient import TestClient
from pytest import fixture

from app.app import app
from app.core import get_api


@fixture()
def client():
    os.environ["VERSION"] = "TEST"
    app.api = get_api()
    yield TestClient(app)
