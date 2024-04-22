import os
import typing as t

import fastapi
import mangum
import pydantic

from . import tools
from ..core.api import get_api
from ..core.models import Resources


app = fastapi.FastAPI(lifespan=tools.lifespan)


class Health(pydantic.BaseModel):
    """
    Health

    Data object used to describe the overall health of the aplication.
    """

    status: str
    version: str
    uptime: t.Union[int, float]


@app.get("/health")
def health() -> Health:
    """
    Health

    Endpoint for getting checking whether or not the service is healthy.
    """
    version = os.getenv("VERSION", "unknown")
    return Health(status="Healthy", version=version, uptime=tools.uptime())


@app.get("/resources")
def get_resources() -> Resources:
    """
    Get Resources

    Endpoint for getting resources.
    """
    api = app.extra.get("api") or get_api()
    resources = api.get_resources()
    return resources


handler = mangum.Mangum(app)
