from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class GeoEntity:
    code: str
    name: str

@dataclass
class Point(GeoEntity):
    x: float
    y: float
    z: float = 0.0

@dataclass
class Line(GeoEntity):
    points: List[Point] = field(default_factory=list)

@dataclass
class Area(GeoEntity):
    points: List[Point] = field(default_factory=list)
