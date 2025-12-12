from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class City:
    name: str
    province: str
    country: str
    open_spaces: List["OpenSpace"] = field(default_factory=list)

@dataclass
class OpenSpace:
    name: str
    type: str
    buildings: List["Building"] = field(default_factory=list)

@dataclass
class Building:
    number: str
    elements: List["Element"] = field(default_factory=list)

@dataclass
class Element:
    type: str
    description: str
