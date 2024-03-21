from sqlalchemy.orm import Session
from src import models, schemas


def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Address).offset(skip).limit(limit).all()


def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def update_address(db: Session, address_id: int, address: schemas.AddressCreate):
    db_address = (
        db.query(models.Address).filter(models.Address.id == address_id).first()
    )
    if db_address:
        for var, value in vars(address).items():
            setattr(db_address, var, value) if value else None
        db.commit()
        db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int):
    db_address = (
        db.query(models.Address).filter(models.Address.id == address_id).first()
    )
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address


def get_founder(db: Session, founder_id: int):
    return db.query(models.Founder).filter(models.Founder.id == founder_id).first()


def get_founders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Founder).offset(skip).limit(limit).all()


def create_founder(db: Session, founder: schemas.FounderCreate):
    db_founder = models.Founder(**founder.dict())
    db.add(db_founder)
    db.commit()
    db.refresh(db_founder)
    return db_founder


def update_founder(db: Session, founder_id: int, founder: schemas.FounderCreate):
    db_founder = (
        db.query(models.Founder).filter(models.Founder.id == founder_id).first()
    )
    if db_founder:
        for var, value in vars(founder).items():
            setattr(db_founder, var, value) if value else None
        db.commit()
        db.refresh(db_founder)
    return db_founder


def delete_founder(db: Session, founder_id: int):
    db_founder = (
        db.query(models.Founder).filter(models.Founder.id == founder_id).first()
    )
    if db_founder:
        db.delete(db_founder)
        db.commit()
    return db_founder


def get_startup(db: Session, startup_id: int):
    return db.query(models.StartUp).filter(models.StartUp.id == startup_id).first()


def get_startups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StartUp).offset(skip).limit(limit).all()


def create_startup(db: Session, startup: schemas.StartUpCreate):
    db_startup = models.StartUp(**startup.dict())
    db.add(db_startup)
    db.commit()
    db.refresh(db_startup)
    return db_startup


def update_startup(db: Session, startup_id: int, startup: schemas.StartUpCreate):
    db_startup = (
        db.query(models.StartUp).filter(models.StartUp.id == startup_id).first()
    )
    if db_startup:
        for var, value in vars(startup).items():
            setattr(db_startup, var, value) if value else None
        db.commit()
        db.refresh(db_startup)
    return db_startup


def delete_startup(db: Session, startup_id: int):
    db_startup = (
        db.query(models.StartUp).filter(models.StartUp.id == startup_id).first()
    )
    if db_startup:
        db.delete(db_startup)
        db.commit()
    return db_startup


def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skill(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()


# Education CRUD Operations
def create_education(db: Session, education: schemas.EducationCreate):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education


def get_education(db: Session, education_id: int):
    return (
        db.query(models.Education).filter(models.Education.id == education_id).first()
    )


def get_educations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()


# Experience CRUD Operations
def create_experience(db: Session, experience: schemas.ExperienceCreate):
    db_experience = models.Experience(**experience.dict())
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience


def get_experience(db: Session, experience_id: int):
    return (
        db.query(models.Experience)
        .filter(models.Experience.id == experience_id)
        .first()
    )


def get_experiences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Experience).offset(skip).limit(limit).all()


# Investor CRUD Operations
def create_investor(db: Session, investor: schemas.InvestorCreate):
    db_investor = models.Investor(**investor.dict())
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor


def get_investor(db: Session, investor_id: int):
    return db.query(models.Investor).filter(models.Investor.id == investor_id).first()


def get_investors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Investor).offset(skip).limit(limit).all()


# KPI CRUD Operations
def create_kpi(db: Session, kpi: schemas.KPICreate):
    db_kpi = models.KPI(**kpi.dict())
    db.add(db_kpi)
    db.commit()
    db.refresh(db_kpi)
    return db_kpi


def get_kpi(db: Session, kpi_id: int):
    return db.query(models.KPI).filter(models.KPI.id == kpi_id).first()


def get_kpis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.KPI).offset(skip).limit(limit).all()


# FoundingRound CRUD Operations
def create_founding_round(db: Session, founding_round: schemas.FoundingRoundCreate):
    db_founding_round = models.FoundingRound(**founding_round.dict())
    # Handle Many-to-Many relationship for investors if necessary here
    db.add(db_founding_round)
    db.commit()
    db.refresh(db_founding_round)
    return db_founding_round


def get_founding_round(db: Session, founding_round_id: int):
    return (
        db.query(models.FoundingRound)
        .filter(models.FoundingRound.id == founding_round_id)
        .first()
    )


def get_founding_rounds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FoundingRound).offset(skip).limit(limit).all()


# Milestone CRUD Operations
def create_milestone(db: Session, milestone: schemas.MilestoneCreate):
    db_milestone = models.Milestone(**milestone.dict())
    db.add(db_milestone)
    db.commit()
    db.refresh(db_milestone)
    return db_milestone


def get_milestone(db: Session, milestone_id: int):
    return (
        db.query(models.Milestone).filter(models.Milestone.id == milestone_id).first()
    )


def get_milestones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Milestone).offset(skip).limit(limit).all()


# Skill Update and Delete Operations
def update_skill(db: Session, skill_id: int, skill: schemas.SkillCreate):
    db_skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if db_skill:
        for key, value in skill.dict().items():
            setattr(db_skill, key, value)
        db.commit()
        db.refresh(db_skill)
    return db_skill


def delete_skill(db: Session, skill_id: int):
    db_skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if db_skill:
        db.delete(db_skill)
        db.commit()
    return db_skill


# Education Update and Delete Operations
def update_education(
    db: Session, education_id: int, education: schemas.EducationCreate
):
    db_education = (
        db.query(models.Education).filter(models.Education.id == education_id).first()
    )
    if db_education:
        for key, value in education.dict().items():
            setattr(db_education, key, value)
        db.commit()
        db.refresh(db_education)
    return db_education


def delete_education(db: Session, education_id: int):
    db_education = (
        db.query(models.Education).filter(models.Education.id == education_id).first()
    )
    if db_education:
        db.delete(db_education)
        db.commit()
    return db_education


# Experience Update and Delete Operations
def update_experience(
    db: Session, experience_id: int, experience: schemas.ExperienceCreate
):
    db_experience = (
        db.query(models.Experience)
        .filter(models.Experience.id == experience_id)
        .first()
    )
    if db_experience:
        for key, value in experience.dict().items():
            setattr(db_experience, key, value)
        db.commit()
        db.refresh(db_experience)
    return db_experience


def delete_experience(db: Session, experience_id: int):
    db_experience = (
        db.query(models.Experience)
        .filter(models.Experience.id == experience_id)
        .first()
    )
    if db_experience:
        db.delete(db_experience)
        db.commit()
    return db_experience


# Investor Update and Delete Operations
def update_investor(db: Session, investor_id: int, investor: schemas.InvestorCreate):
    db_investor = (
        db.query(models.Investor).filter(models.Investor.id == investor_id).first()
    )
    if db_investor:
        for key, value in investor.dict().items():
            setattr(db_investor, key, value)
        db.commit()
        db.refresh(db_investor)
    return db_investor


def delete_investor(db: Session, investor_id: int):
    db_investor = (
        db.query(models.Investor).filter(models.Investor.id == investor_id).first()
    )
    if db_investor:
        db.delete(db_investor)
        db.commit()
    return db_investor


# KPI Update and Delete Operations
def update_kpi(db: Session, kpi_id: int, kpi: schemas.KPICreate):
    db_kpi = db.query(models.KPI).filter(models.KPI.id == kpi_id).first()
    if db_kpi:
        for key, value in kpi.dict().items():
            setattr(db_kpi, key, value)
        db.commit()
        db.refresh(db_kpi)
    return db_kpi


def delete_kpi(db: Session, kpi_id: int):
    db_kpi = db.query(models.KPI).filter(models.KPI.id == kpi_id).first()
    if db_kpi:
        db.delete(db_kpi)
        db.commit()
    return db_kpi


# FoundingRound Update and Delete Operations
def update_founding_round(
    db: Session, founding_round_id: int, founding_round: schemas.FoundingRoundCreate
):
    db_founding_round = (
        db.query(models.FoundingRound)
        .filter(models.FoundingRound.id == founding_round_id)
        .first()
    )
    if db_founding_round:
        for key, value in founding_round.dict().items():
            setattr(db_founding_round, key, value)
        # Handle investors update if necessary
        db.commit()
        db.refresh(db_founding_round)
    return db_founding_round


def delete_founding_round(db: Session, founding_round_id: int):
    db_founding_round = (
        db.query(models.FoundingRound)
        .filter(models.FoundingRound.id == founding_round_id)
        .first()
    )
    if db_founding_round:
        db.delete(db_founding_round)
        db.commit()
    return db_founding_round


# Milestone Update and Delete Operations
def update_milestone(
    db: Session, milestone_id: int, milestone: schemas.MilestoneCreate
):
    db_milestone = (
        db.query(models.Milestone).filter(models.Milestone.id == milestone_id).first()
    )
    if db_milestone:
        for key, value in milestone.dict().items():
            setattr(db_milestone, key, value)
        db.commit()
        db.refresh(db_milestone)
    return db_milestone


def delete_milestone(db: Session, milestone_id: int):
    db_milestone = (
        db.query(models.Milestone).filter(models.Milestone.id == milestone_id).first()
    )
    if db_milestone:
        db.delete(db_milestone)
        db.commit()
    return db_milestone
