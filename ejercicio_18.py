from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Shape:
    color: str

@dataclass
class Quadrilateral(Shape):
    length: float

@dataclass
class Rectangle(Quadrilateral):
    width: float

@dataclass
class Square(Rectangle):
    pass

@dataclass
class Conic(Shape):
    pass

@dataclass
class Circle(Conic):
    diameter: float

@dataclass
class Ellipse(Conic):
    major_axis: float
    minor_axis: float
