from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Dimension:
    name: str
    measure: float
    unit: str

@dataclass
class Place:
    name: str
    province: str
    country: str

@dataclass
class ArchaeologicalEntity:
    name: str
    chronology: Optional[str]
    location: Place
    dimensions: List[Dimension] = field(default_factory=list)

@dataclass
class Site(ArchaeologicalEntity):
    site_type: str

@dataclass
class ArchaeologicalComplex(ArchaeologicalEntity):
    components: List[ArchaeologicalEntity] = field(default_factory=list)
