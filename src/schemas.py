from datetime import date, datetime
from pydantic import BaseModel
from typing import List, Optional


class FounderBase(BaseModel):
    name: str
    image: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    address: Optional[str] = None
    birthdate: Optional[str] = None
    startup: Optional[str] = None
    role: Optional[str] = None
    skills: Optional[str] = None
    education_degree: Optional[str] = None
    education_school: Optional[str] = None
    professional_experience_job: Optional[str] = None
    professional_experience_company: Optional[str] = None


class FounderCreate(FounderBase):
    pass


class FounderUpdate(FounderBase):
    pass


class Founder(FounderBase):
    last_update: Optional[str]
    co_founders: List[FounderBase] = []

    class Config:
        from_attributes = True


class StartupBase(BaseModel):
    name: str
    logo: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    linkedin: Optional[str] = None
    address: Optional[str] = None
    founding_date: Optional[str] = None
    status: Optional[str] = None
    phase: Optional[str] = None
    fte: Optional[int] = None
    equity_free_grants_chf: Optional[int] = None
    business_model_type: Optional[str] = None
    target_market: Optional[str] = None
    kpis: Optional[str] = None
    last_funding_round: Optional[str] = None
    last_milestone: Optional[str] = None
    looking_for: Optional[str] = None


class StartupCreate(StartupBase):
    pass


class StartupUpdate(StartupBase):
    pass


class Startup(StartupBase):
    last_update: Optional[str]
    founders: List[FounderBase] = (
        []
    ) 

    class Config:
        from_attributes = True


class Events(BaseModel):
    id: int
    startup_name: str
    changed_field: str
    old_value: str
    new_value: str
    timestamp: str
