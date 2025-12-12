from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Project:
    name: str
    interventions: List["Intervention"] = field(default_factory=list)

@dataclass
class Intervention:
    name: str
    project: Optional[Project] = None
    participants: List["Person"] = field(default_factory=list)

@dataclass
class Role:
    pass

@dataclass
class Responsible(Role):
    directs: Optional[Project] = None

@dataclass
class Technician(Role):
    participates_in_projects: List[Project] = field(default_factory=list)
    participates_in_interventions: List[Intervention] = field(default_factory=list)

@dataclass
class Person:
    name: str
    roles: List[Role] = field(default_factory=list)
