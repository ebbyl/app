class TestGetResources:
    """
    Test Get Resources

    Test getting resources from the HTTP API.
    """

    def test_client_returns_expected_data(self, client):
        response = client.get("/resources")

        assert response.status_code == 200
        assert response.json() == {
            "assets": [
                {
                    "location": "sequim",
                    "operating_capacity": 100,
                    "operating_hours": 680,
                    "footprint": "600 m2",
                },
                {
                    "location": "burlingame",
                    "operating_capacity": 100,
                    "operating_hours": 300,
                    "footprint": "650 m2",
                },
            ],
            "collaborating_organizations": ["PNNL", "NOAA", "WHOI", "Scripps"],
        }
