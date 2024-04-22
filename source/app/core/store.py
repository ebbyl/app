from __future__ import annotations

import abc
import dataclasses
import pathlib
import typing as t
import yaml


Data = t.Mapping[str, t.Any]


@dataclasses.dataclass()
class Store(abc.ABC):
    """
    Store

    This is an abstract class which cannot be directly instatiated. It
    defines the interface for all concrete storage implementations.
    """

    @classmethod
    @abc.abstractmethod
    def new(cls) -> Store:
        """
        New Store

        Factory method for creating a new instance of the store.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_resources(self) -> Data:
        """
        Get Resources

        Get all resources in the data store.
        """
        raise NotImplementedError


# ---------------------------------------------------------------------
# Local Store
# ---------------------------------------------------------------------


@dataclasses.dataclass()
class LocalStore(Store):
    """
    Local Store

    This store holds data in local memory (not shared between
    instances of the application).
    """

    data: Data

    @classmethod
    def new(cls, data: t.Optional[Data] = None) -> LocalStore:
        """
        New Store

        Factory method for creating a new instance of the store
        with the given data. If no data is given, it will be
        automatically loaded from a local YAML file.
        """
        if data is None:
            root = pathlib.Path(__file__).parent.parent
            path = root.joinpath("data", "ebbcarbon.yaml")
            text = path.read_text()
            data = yaml.safe_load(text)

        return cls(data=data)

    def get_resources(self) -> Data:
        """
        Get Resources

        Get all resources in the data store.
        """
        return self.data.get("resources") or {}
