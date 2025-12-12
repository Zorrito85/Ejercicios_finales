from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Site:
    name: str

@dataclass
class Excavation:
    site: Site
    start_date: str
    end_date: Optional[str] = None
    found_objects: List["ArchaeologicalObject"] = field(default_factory=list)

@dataclass
class ArchaeologicalObject:
    code: str
    dating: Optional[str]
    dimensions: Optional[str]
    description: Optional[str]
    materials: List[str]
    similar_to: List["ArchaeologicalObject"] = field(default_factory=list)

@dataclass
class Fragment(ArchaeologicalObject):
    parent: Optional[ArchaeologicalObject] = None

@dataclass
class CompleteObject(ArchaeologicalObject):
    usage: List[str] = field(default_factory=list)
    components: List[ArchaeologicalObject] = field(default_factory=list)
