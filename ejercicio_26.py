from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class ApseForm(Enum):
    SEMICIRCULAR = "semicircular"
    IN_CROWN = "en_corona"

class CrossingType(Enum):
    WITHOUT_ARMS = "sin_brazos"
    WITH_ARMS = "con_brazos"

@dataclass
class Window:
    width: float
    height: float
    double_arch: bool = False
    decorated: bool = False
    close_technique: Optional[str] = None

@dataclass
class Nave:
    surface: float

@dataclass
class Apse:
    form: ApseForm

@dataclass
class Church:
    name: str
    order: Optional[str] = None
    type: str = "rural"
    naves: int = 1
    nave: Optional[Nave] = None
    apses: List[Apse] = field(default_factory=list)
    windows: List[Window] = field(default_factory=list)
