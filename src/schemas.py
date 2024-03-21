from typing import List, Literal, Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    zip: str
    city: str
    country: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        from_attributes = True


class FounderBase(BaseModel):
    name: str
    picture: Optional[str] = None
    mail: str
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    address_id: int
    birthdate: str
    last_update: str


class FounderCreate(FounderBase):
    pass


class Founder(FounderBase):
    id: int

    class Config:
        from_attributes = True


class StartUpBase(BaseModel):
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
    last_update: str


class StartUpCreate(StartUpBase):
    pass


class StartUp(StartUpBase):
    id: int

    class Config:
        from_attributes = True


class SkillBase(BaseModel):
    name: str


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id: int

    class Config:
        from_attributes = True


class EducationBase(BaseModel):
    name: str


class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id: int

    class Config:
        from_attributes = True


class ExperienceBase(BaseModel):
    name: str


class ExperienceCreate(ExperienceBase):
    pass


class Experience(ExperienceBase):
    id: int

    class Config:
        from_attributes = True


class InvestorBase(BaseModel):
    name: str


class InvestorCreate(InvestorBase):
    pass


class Investor(InvestorBase):
    id: int

    class Config:
        from_attributes = True


class KPIBase(BaseModel):
    name: str
    value: str
    unit: str
    date: str
    is_northstar: bool


class KPICreate(KPIBase):
    pass


class KPI(KPIBase):
    id: int

    class Config:
        from_attributes = True


class FoundingRoundBase(BaseModel):
    number: int
    amount: int
    unit: str
    date: str


class FoundingRoundCreate(FoundingRoundBase):
    pass


class FoundingRound(FoundingRoundBase):
    id: int

    class Config:
        from_attributes = True


class MilestoneBase(BaseModel):
    name: str
    description: str
    status: str


class MilestoneCreate(MilestoneBase):
    pass


class Milestone(MilestoneBase):
    id: int

    class Config:
        from_attributes = True
