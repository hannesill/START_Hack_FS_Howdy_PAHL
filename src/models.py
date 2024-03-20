import datetime
from typing import List, Literal, Optional
from pydantic import BaseModel


class KPI(BaseModel):
    """Key Performance Indicator"""

    name: Optional[str] = None
    value: Optional[float] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    is_north_star: Optional[bool] = False


class Investor(BaseModel):
    """Investor"""

    name: Optional[str] = None


class FoundingRound(BaseModel):
    """Founding Round"""

    date: Optional[datetime.date] = None
    round: Optional[str] = None


class InvestorContributions(BaseModel):
    """Investor Contributions"""

    investor: Optional[Investor] = None
    founding_round: Optional[FoundingRound] = None
    amount: Optional[float] = None
    currency: Optional[str] = "USD"


class SocialMedia(BaseModel):
    """Social Media"""

    name: Optional[str] = None
    link: Optional[str] = None


class Address(BaseModel):
    """Address"""

    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None


class FTEPerCountry(BaseModel):
    """Full Time Employees Per Country"""

    country: Optional[str] = None
    number_of_employees: Optional[int] = None


class Startup(BaseModel):
    """Startup"""

    name: Optional[str] = None
    description: Optional[str] = None
    adress: Optional[Address] = None
    website: Optional[str] = None
    social_media: List[SocialMedia] = []
    target_market: Optional[str] = None
    milestones: List[str] = []
    challenges: List[str] = []
    intellectual_properties: Optional[str] = None
    industry: Optional[str] = None
    founding_rounds: List[FoundingRound] = []
    kpis: List[KPI] = []
    fs_acceleator_participation: Optional[datetime.date] = None
    fs_incubator_participation: Optional[datetime.date] = None
    fs_acceleator_participation_type: Optional[str] = None
    status: Optional[Literal["Working on it", "Crashed", "Exited"]] = None
    phase: Optional[
        Literal["FFF", "Pre-Seed", "Seed", "Series A", "Series B", "Series C+"]
    ] = None
    founding_date: Optional[datetime.date] = None
    ftes: List[FTEPerCountry] = []
    business_model: Optional[Literal["B2B", "B2C"]] = None
    equity_free_grants: Optional[float] = None


class Skill(BaseModel):
    """Skill"""

    name: Optional[str] = None


class Founder(BaseModel):
    """Founder"""

    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[Address] = None
    birthday: Optional[datetime.date] = None
    skills: List[Skill] = None
    education: List[str] = []
    professional_experience: List[str] = []
