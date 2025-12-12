from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class Construction:
    name: str

@dataclass
class Building(Construction):
    pass

@dataclass
class BuiltGroup(Construction):
    components: List[Construction] = field(default_factory=list)

def add_component(group: BuiltGroup, c: Construction):
    group.components.append(c)
    return group
