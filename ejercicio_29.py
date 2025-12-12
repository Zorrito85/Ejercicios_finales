from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Document:
    title: str
    doc_type: Optional[str]
    publication_date: Optional[str]

@dataclass
class Event:
    name: str
    moment: str
    description: Optional[str] = None

@dataclass
class Occupation:
    name: str
    from_date: Optional[str] = None
    to_date: Optional[str] = None

@dataclass
class Place:
    name: str
    address: Optional[str] = None

@dataclass
class Person:
    given_name: str
    family_name: str
    title: Optional[str] = None
    birth_date: Optional[str] = None
    birth_place: Optional[str] = None
    death_date: Optional[str] = None
    death_place: Optional[str] = None
    occupations: List[Occupation] = field(default_factory=list)
    contacts: List["Person"] = field(default_factory=list)
    visits: List[dict] = field(default_factory=list)
    reads: List[Document] = field(default_factory=list)
    events: List[Event] = field(default_factory=list)

def add_occupation(person: Person, occ: Occupation):
    person.occupations.append(occ)
    return person

def add_visit(person: Person, place: Place, from_date: str, to_date: Optional[str] = None):
    person.visits.append({"place": place, "from": from_date, "to": to_date})
    return person
