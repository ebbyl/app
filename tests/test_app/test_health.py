import pytest


class TestHealth:
    """
    Test Health

    Test health check.
    """

    def test_client_returns_healthy(self, client):
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json() == {
            "status": "Healthy", 
            "uptime": pytest.approx(1, 5),
            "version": "TEST"
        }
