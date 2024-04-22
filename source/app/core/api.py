from __future__ import annotations

import dataclasses
import functools

from .store import Store, LocalStore
from .models import Resources


@functools.lru_cache()
def get_api() -> API:
    """
    Get API

    Create default API instance.
    """
    store = LocalStore.new()
    api = API(store=store)
    return api


@dataclasses.dataclass()
class API:
    store: Store

    def get_resources(self) -> Resources:
        """
        Get Resources

        Get project resources.
        """
        raw = self.store.get_resources()
        resources = Resources(**raw)
        return resources
