import app
from app.core.models import Resources, Asset


class TestGetResources:
    """
    Test Get Resources

    Test getting resources from the core API.
    """

    def test_api_returns_expected_data(self):
        api = app.get_api()

        resources = api.get_resources()

        assert resources == Resources(
            assets=[
                Asset(
                    location="sequim",
                    operating_capacity=100,
                    operating_hours=680,
                    footprint="600 m2",
                ),
                Asset(
                    location="burlingame",
                    operating_capacity=100,
                    operating_hours=300,
                    footprint="650 m2",
                ),
            ],
            collaborating_organizations=["PNNL", "NOAA", "WHOI", "Scripps"],
        )
