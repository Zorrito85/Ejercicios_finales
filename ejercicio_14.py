from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Triangle:
    p1: Point
    p2: Point
    p3: Point

# example two triangles sharing a side
pt1 = Point(-10, 10)
pt2 = Point(10, 10)
pt3 = Point(-10, -10)
pt4 = Point(10, -10)

t1 = Triangle(pt1, pt2, pt3)
t2 = Triangle(pt2, pt4, pt3)
