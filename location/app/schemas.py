import os
from typing import List, Optional
# import datetime

from pydantic import BaseModel


class Point(BaseModel):
    lat: float
    long: float


class Location(BaseModel):
    point: Point
    name: str
    tags: Optional[List[str]]

class RouteSummary(BaseModel):
    walking_distance: int
    total_distance: int
    total_time: int
    public_transport_count: int

class InterestPoint(Point):
    name: str
    address: str
    distance: int
    website: Optional[str]
    website_domain: Optional[str]
    chain_name: Optional[str]
