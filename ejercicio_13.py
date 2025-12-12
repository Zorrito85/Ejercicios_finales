from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Polygon:
    points: List[Point] = field(default_factory=list)

def make_polygon(pts: List[Point]) -> Polygon:
    return Polygon(points=pts)
