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

class RouteSumary(BaseModel):
    waking_distance: int
    total_distance: int
    total_time: int
    public_transport_count: int
