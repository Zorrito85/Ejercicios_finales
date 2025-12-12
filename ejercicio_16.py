from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Person:
    given_name: str
    family_name: str
    second_family_name: Optional[str] = None
    birth_date: Optional[str] = None
    sex: Optional[str] = None
    id_number: Optional[str] = None
    spouse: Optional["Person"] = None
    parents: List["Person"] = field(default_factory=list)
    children: List["Person"] = field(default_factory=list)

def marry(a: Person, b: Person):
    a.spouse = b
    b.spouse = a
    return a, b

def add_child(parent: Person, child: Person):
    parent.children.append(child)
    child.parents.append(parent)
    return child
