from __future__ import annotations

from annotated_types import Ge, Le, Predicate
import re
import typing as t

from pydantic import BaseModel


def is_area(value: str) -> bool:
    """
    Is Area

    Check if the given string represents an area.
    """
    pattern = "(?P<value>\d+)\s(?P<unit>m2)"
    match = re.match(pattern, value)
    return bool(match)


Location = str
Capacity = t.Annotated[int, Ge(0), Le(100)]
Hours = int
Area = t.Annotated[str, Predicate(is_area)]


class Resources(BaseModel):
    """
    Resources

    Value object used to represent resources.
    """

    assets: t.List[Asset]
    collaborating_organizations: t.List[str]


class Asset(BaseModel):
    """
    Asset

    Value object used to represent an asset.
    """

    location: Location
    operating_capacity: Capacity
    operating_hours: Hours
    footprint: Area
