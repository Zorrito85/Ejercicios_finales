from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class PrintForm(Enum):
    MANUSCRIPT = "manuscript"
    PRINTED = "printed"

class BindingTechnique(Enum):
    SEWN = "sewn"
    BOUND = "bound"

@dataclass
class Book:
    number_of_pages: int
    form: PrintForm
    binding: BindingTechnique

@dataclass
class Sample:
    fraction: float
    extraction_method: str
