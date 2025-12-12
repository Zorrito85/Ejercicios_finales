from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Structure:
    code: str
    dating: Optional[str]
    materials: List[str]
    substructures: List["Structure"] = field(default_factory=list)

def add_substructure(parent: Structure, child: Structure):
    parent.substructures.append(child)
    return parent
