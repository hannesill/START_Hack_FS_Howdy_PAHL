from __future__ import annotations
from typing import List, Literal
from pydantic import BaseModel


class Address(BaseModel):
    """Represent an address"""

    id: int
    street: str
    zip: str
    city: str
    country: str


class Skill(BaseModel):
    """Represents a skill"""

    id: int
    name: str


class Education(BaseModel):
    """Represents an education"""

    id: int
    name: str


class Experience(BaseModel):
    """Represents a professional experience"""

    id: int
    name: str


class Investor(BaseModel):
    """Represents an investor"""

    id: int
    name: str


class KPI(BaseModel):
    """Represents a key performance indicator"""

    id: int
    name: str
    value: str
    unit: str
    date: str
    is_northstar: bool


class FoundingRound(BaseModel):
    """Represents a founding round"""

    id: int
    number: int
    amount: int
    unit: str
    date: str
    investors: List[Investor]


class Milestone:
    """Represents a milestone"""

    id: int
    name: str
    description: str
    status: str


class StartUp(BaseModel):
    """Represents a startup"""

    id: int
    name: str
    description: str
    logo: str
    website: str
    linkedin: str
    address_id: int
    industry: str
    founding_date: str
    status: Literal["Working on it", "Crashed", "Exited"]
    phase: Literal["FFF", "Pre-Seed", "Seed", "Series A", "Series B", "Series C+"]
    fte: int
    equity_free_grants: int
    business_model: Literal["B2B", "B2C"]
    target_market: str
    # founders = List[Founder] = []  # type: ignore
    # kpis: List[KPI]
    # founding_rounds: List[FoundingRound]
    # milestones: List[Milestone]
    last_update: str


class Founder(BaseModel):
    """Represents a founder"""

    id: int
    name: str
    picture: str
    mail: str
    phone: str
    linkedin: str
    address_id: int
    birthdate: str
    # cofounders: List[Founder] = []  # type: ignore
    # skills: List[Skill]
    # educations: List[Education]
    # startups: List[StartUp]
    last_update: str
