from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Floor:
    number: int
    capacity: int

@dataclass
class Thematic:
    name: str

@dataclass
class Book:
    isbn: str
    title: str
    year: str
    languages: List[str] = field(default_factory=list)

@dataclass
class Copy:
    code: str
    book: Book
    editorial: str
    acquisition_year: str

@dataclass
class Reader:
    name: str
    id_number: str
    address: str

@dataclass
class Employee:
    name: str
    code: str

@dataclass
class Loan:
    copy: Copy
    borrower: Reader
    start_date: str
    due_date: str
    return_date: Optional[str] = None

@dataclass
class Library:
    name: str
    address: str
    phone: List[str]
    floors: List[Floor] = field(default_factory=list)
    thematics: List[Thematic] = field(default_factory=list)
    copies: List[Copy] = field(default_factory=list)
