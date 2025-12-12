from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from enum import Enum

from enum import Enum

class Material(Enum):
    STONE = "stone"
    CERAMIC = "ceramic"
    METAL = "metal"

@dataclass
class ArchaeologicalObject:
    code: str
    dating: str
    dimensions: str
    description: str
    materials: List[str]
    similar_to: List["ArchaeologicalObject"] = field(default_factory=list)

@dataclass
class Fragment(ArchaeologicalObject):
    parent_code: str = ""

@dataclass
class CompleteObject(ArchaeologicalObject):
    components: List[ArchaeologicalObject] = field(default_factory=list)
