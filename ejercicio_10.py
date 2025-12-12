from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass
class Place:
    name: str
    coord_x: float
    coord_y: float

@dataclass
class Project:
    name: str
    start: Optional[date] = None
    end: Optional[date] = None
    participants: List["Person"] = field(default_factory=list)
    places: List[Place] = field(default_factory=list)

@dataclass
class Person:
    name: str
    surname: Optional[str] = None
    roles: List[str] = field(default_factory=list)

def participate(person: Person, project: Project):
    if person not in project.participants:
        project.participants.append(person)
    return project

def assign_place(project: Project, place: Place):
    if place not in project.places:
        project.places.append(place)
    return project
