from __future__ import annotations
import datetime
from typing import List, Literal
from pydantic import BaseModel, Field


class Address(BaseModel):
    """Represent an address"""

    street: str
    zip: int
    city: str
    country: str


class Skill(BaseModel):
    """Represents a skill"""

    name: str


class Education(BaseModel):
    """Represents an education"""

    name: str


class Experience(BaseModel):
    """Represents a professional experience"""

    name: str


class Investor(BaseModel):
    """Represents an investor"""

    name: str


class KPI(BaseModel):
    """Represents a key performance indicator"""

    name: str
    value: str
    unit: str
    date: datetime.datetime
    is_northstar: bool


class FoundingRound(BaseModel):
    """Represents a founding round"""

    number: int
    amount: int
    unit: str
    date: datetime.date
    investors: List[Investor]


class Milestone:
    """Represents a milestone"""

    name: str
    description: str
    status: str


class StartUp(BaseModel):
    """Represents a startup"""

    id: int
    name: str
    description: str
    logo: str = "Not defined"
    website: str
    linkedin: str
    address: Address
    industry: str
    founding_date: datetime.date
    status: Literal["Working on it", "Crashed", "Exited"]
    phase: Literal["FFF", "Pre-Seed", "Seed", "Series A", "Series B", "Series C+"]
    fte: int
    equity_free_grants: int
    business_model: Literal["B2B", "B2C"]
    target_market: str
    # founders = List[Founder] = []  # type: ignore
    kpis: List[KPI]
    founding_rounds: List[FoundingRound]
    # milestones: List[Milestone]
    last_update: datetime.datetime = datetime.datetime.now()


class Founder(BaseModel):
    """Represents a founder"""

    id: int
    name: str
    picture: str = "Not defined"
    mail: str
    phone: str
    linkedin: str
    address: Address
    birthdate: datetime.date
    # cofounders: List[Founder] = []  # type: ignore
    skills: List[Skill]
    educations: List[Education]
    startups: List[StartUp]
    last_update: datetime.datetime
