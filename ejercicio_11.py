from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Place:
    institution: str
    city: str
    country: str

@dataclass
class Painting:
    title: Optional[str]
    chronology: Optional[str]
    technique: Optional[str]
    subtechnique: Optional[str]
    material: Optional[str]
    author: Optional[str]
    conservation_state: Optional[str]
    location: Optional[Place] = None
    original: Optional["Painting"] = None
    replicas: List["Painting"] = field(default_factory=list)

def add_replica(original: Painting, replica: Painting):
    replica.original = original
    original.replicas.append(replica)
    return replica
