from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Location:
    code: str
    name: str
    open_to_public: bool = False

@dataclass
class Restoration:
    date: str
    description: str
    techniques: List[str]

@dataclass
class Collection:
    name: str
    description: str
    temporal_start: Optional[str] = None
    temporal_end: Optional[str] = None

@dataclass
class Building:
    name: str
    address: str
    floors: List["Floor"] = field(default_factory=list)

@dataclass
class Floor:
    number: int

@dataclass
class ArchaeologicalObject:
    code: str
    name: str
    author: str
    creation_date: str
    description: str
    origin: str
    state: str
    themes: List[str]
    location: Optional[Location] = None
    restorations: List[Restoration] = field(default_factory=list)

def record_restoration(obj: ArchaeologicalObject, rest: Restoration):
    obj.restorations.append(rest)
    return obj
