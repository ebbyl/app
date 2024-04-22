import contextlib
import time
import typing as t

import fastapi

from ..core.api import get_api


UPTIME = time.time()


@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI) -> t.AsyncIterator[None]:
    """
    Lifespan (startup/shutdown)

    Hooks for performing opertions on startup/shutdown.
    """
    global UPTIME

    # Set value used to calculate uptime.
    UPTIME = time.time()

    # Initialize API
    app.extra["api"] = get_api()

    yield


def uptime() -> float:
    """
    Uptime

    Get the amount of time the app has been up for (seconds)
    """
    return time.time() - UPTIME
