import falcon
from falcon import testing
import pytest
from webscraper import app

@pytest.fixture
def client():
    return testing.TestClient(app)