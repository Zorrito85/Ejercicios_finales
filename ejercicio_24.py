from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass
class Building:
    name: str
    uses: List["BuildingUse"] = field(default_factory=list)

@dataclass
class BuildingUse:
    kind: str
    start: date
    end: Optional[date] = None

def add_use(building: Building, use: BuildingUse):
    building.uses.append(use)
    return building
