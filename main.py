from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)


@app.get("/addresses/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db, skip=skip, limit=limit)
    return addresses


@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(
    address_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)
):
    return crud.update_address(db=db, address_id=address_id, address=address)


@app.delete("/addresses/{address_id}", response_model=schemas.Address)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    return crud.delete_address(db=db, address_id=address_id)


@app.post("/founders/", response_model=schemas.Founder)
def create_founder(founder: schemas.FounderCreate, db: Session = Depends(get_db)):
    return crud.create_founder(db=db, founder=founder)


@app.get("/founders/{founder_id}", response_model=schemas.Founder)
def read_founder(founder_id: int, db: Session = Depends(get_db)):
    db_founder = crud.get_founder(db, founder_id=founder_id)
    if db_founder is None:
        raise HTTPException(status_code=404, detail="Founder not found")
    return db_founder


@app.get("/founders/", response_model=List[schemas.Founder])
def read_founders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    founders = crud.get_founders(db, skip=skip, limit=limit)
    return founders


@app.put("/founders/{founder_id}", response_model=schemas.Founder)
def update_founder(
    founder_id: int, founder: schemas.FounderCreate, db: Session = Depends(get_db)
):
    return crud.update_founder(db=db, founder_id=founder_id, founder=founder)


@app.delete("/founders/{founder_id}", response_model=schemas.Founder)
def delete_founder(founder_id: int, db: Session = Depends(get_db)):
    return crud.delete_founder(db=db, founder_id=founder_id)


@app.post("/startups/", response_model=schemas.StartUp)
def create_startup(startup: schemas.StartUpCreate, db: Session = Depends(get_db)):
    return crud.create_startup(db=db, startup=startup)


@app.get("/startups/{startup_id}", response_model=schemas.StartUp)
def read_startup(startup_id: int, db: Session = Depends(get_db)):
    db_startup = crud.get_startup(db, startup_id=startup_id)
    if db_startup is None:
        raise HTTPException(status_code=404, detail="StartUp not found")
    return db_startup


@app.get("/startups/", response_model=List[schemas.StartUp])
def read_startups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    startups = crud.get_startups(db, skip=skip, limit=limit)
    return startups


@app.put("/startups/{startup_id}", response_model=schemas.StartUp)
def update_startup(
    startup_id: int, startup: schemas.StartUpCreate, db: Session = Depends(get_db)
):
    return crud.update_startup(db=db, startup_id=startup_id, startup=startup)


@app.delete("/startups/{startup_id}", response_model=schemas.StartUp)
def delete_startup(startup_id: int, db: Session = Depends(get_db)):
    return crud.delete


# Skill Endpoints
@app.post("/skills/", response_model=schemas.Skill)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_skill(db=db, skill=skill)


@app.get("/skills/{skill_id}", response_model=schemas.Skill)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = crud.get_skill(db, skill_id=skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill


@app.put("/skills/{skill_id}", response_model=schemas.Skill)
def update_skill(
    skill_id: int, skill: schemas.SkillCreate, db: Session = Depends(get_db)
):
    return crud.update_skill(db=db, skill_id=skill_id, skill=skill)


@app.delete("/skills/{skill_id}", response_model=schemas.Skill)
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    return crud.delete_skill(db=db, skill_id=skill_id)


@app.get("/skills/", response_model=List[schemas.Skill])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = crud.get_skills(db, skip=skip, limit=limit)
    return skills


# Education Endpoints
@app.post("/educations/", response_model=schemas.Education)
def create_education(education: schemas.EducationCreate, db: Session = Depends(get_db)):
    return crud.create_education(db=db, education=education)


@app.get("/educations/{education_id}", response_model=schemas.Education)
def read_education(education_id: int, db: Session = Depends(get_db)):
    db_education = crud.get_education(db, education_id=education_id)
    if db_education is None:
        raise HTTPException(status_code=404, detail="Education not found")
    return db_education


@app.put("/educations/{education_id}", response_model=schemas.Education)
def update_education(
    education_id: int, education: schemas.EducationCreate, db: Session = Depends(get_db)
):
    return crud.update_education(db=db, education_id=education_id, education=education)


@app.delete("/educations/{education_id}", response_model=schemas.Education)
def delete_education(education_id: int, db: Session = Depends(get_db)):
    return crud.delete_education(db=db, education_id=education_id)


@app.get("/educations/", response_model=List[schemas.Education])
def read_educations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    educations = crud.get_educations(db, skip=skip, limit=limit)
    return educations


# Experience Endpoints
@app.post("/experiences/", response_model=schemas.Experience)
def create_experience(
    experience: schemas.ExperienceCreate, db: Session = Depends(get_db)
):
    return crud.create_experience(db=db, experience=experience)


@app.get("/experiences/{experience_id}", response_model=schemas.Experience)
def read_experience(experience_id: int, db: Session = Depends(get_db)):
    db_experience = crud.get_experience(db, experience_id=experience_id)
    if db_experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    return db_experience


@app.put("/experiences/{experience_id}", response_model=schemas.Experience)
def update_experience(
    experience_id: int,
    experience: schemas.ExperienceCreate,
    db: Session = Depends(get_db),
):
    return crud.update_experience(
        db=db, experience_id=experience_id, experience=experience
    )


@app.delete("/experiences/{experience_id}", response_model=schemas.Experience)
def delete_experience(experience_id: int, db: Session = Depends(get_db)):
    return crud.delete_experience(db=db, experience_id=experience_id)


@app.get("/experiences/", response_model=List[schemas.Experience])
def read_experiences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    experiences = crud.get_experiences(db, skip=skip, limit=limit)
    return experiences


# Investor Endpoints
@app.post("/investors/", response_model=schemas.Investor)
def create_investor(investor: schemas.InvestorCreate, db: Session = Depends(get_db)):
    return crud.create_investor(db=db, investor=investor)


@app.get("/investors/{investor_id}", response_model=schemas.Investor)
def read_investor(investor_id: int, db: Session = Depends(get_db)):
    db_investor = crud.get_investor(db, investor_id=investor_id)
    if db_investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    return db_investor


@app.put("/investors/{investor_id}", response_model=schemas.Investor)
def update_investor(
    investor_id: int, investor: schemas.InvestorCreate, db: Session = Depends(get_db)
):
    return crud.update_investor(db=db, investor_id=investor_id, investor=investor)


@app.delete("/investors/{investor_id}", response_model=schemas.Investor)
def delete_investor(investor_id: int, db: Session = Depends(get_db)):
    return crud.delete_investor(db=db, investor_id=investor_id)


@app.get("/investors/", response_model=List[schemas.Investor])
def read_investors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    investors = crud.get_investors(db, skip=skip, limit=limit)
    return investors


# KPI Endpoints
@app.post("/kpis/", response_model=schemas.KPI)
def create_kpi(kpi: schemas.KPICreate, db: Session = Depends(get_db)):
    return crud.create_kpi(db=db, kpi=kpi)


@app.get("/kpis/{kpi_id}", response_model=schemas.KPI)
def read_kpi(kpi_id: int, db: Session = Depends(get_db)):
    db_kpi = crud.get_kpi(db, kpi_id=kpi_id)
    if db_kpi is None:
        raise HTTPException(status_code=404, detail="KPI not found")
    return db_kpi


@app.get("/kpis/", response_model=List[schemas.KPI])
def read_kpis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    kpis = crud.get_kpis(db, skip=skip, limit=limit)
    return kpis


@app.put("/kpis/{kpi_id}", response_model=schemas.KPI)
def update_kpi(kpi_id: int, kpi: schemas.KPICreate, db: Session = Depends(get_db)):
    return crud.update_kpi(db=db, kpi_id=kpi_id, kpi=kpi)


@app.delete("/kpis/{kpi_id}", response_model=schemas.KPI)
def delete_kpi(kpi_id: int, db: Session = Depends(get_db)):
    return crud.delete_kpi(db=db, kpi_id=kpi_id)


# FoundingRound Endpoints
@app.post("/foundingrounds/", response_model=schemas.FoundingRound)
def create_founding_round(
    founding_round: schemas.FoundingRoundCreate, db: Session = Depends(get_db)
):
    return crud.create_founding_round(db=db, founding_round=founding_round)


@app.get("/foundingrounds/{founding_round_id}", response_model=schemas.FoundingRound)
def read_founding_round(founding_round_id: int, db: Session = Depends(get_db)):
    db_founding_round = crud.get_founding_round(db, founding_round_id=founding_round_id)
    if db_founding_round is None:
        raise HTTPException(status_code=404, detail="Founding Round not found")
    return db_founding_round


@app.get("/foundingrounds/", response_model=List[schemas.FoundingRound])
def read_founding_rounds(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    founding_rounds = crud.get_founding_rounds(db, skip=skip, limit=limit)
    return founding_rounds


@app.put("/foundingrounds/{founding_round_id}", response_model=schemas.FoundingRound)
def update_founding_round(
    founding_round_id: int,
    founding_round: schemas.FoundingRoundCreate,
    db: Session = Depends(get_db),
):
    return crud.update_founding_round(
        db=db, founding_round_id=founding_round_id, founding_round=founding_round
    )


@app.delete("/foundingrounds/{founding_round_id}", response_model=schemas.FoundingRound)
def delete_founding_round(founding_round_id: int, db: Session = Depends(get_db)):
    return crud.delete_founding_round(db=db, founding_round_id=founding_round_id)


# Milestone Endpoints
@app.post("/milestones/", response_model=schemas.Milestone)
def create_milestone(milestone: schemas.MilestoneCreate, db: Session = Depends(get_db)):
    return crud.create_milestone(db=db, milestone=milestone)


@app.get("/milestones/{milestone_id}", response_model=schemas.Milestone)
def read_milestone(milestone_id: int, db: Session = Depends(get_db)):
    db_milestone = crud.get_milestone(db, milestone_id=milestone_id)
    if db_milestone is None:
        raise HTTPException(status_code=404, detail="Milestone not found")
    return db_milestone


@app.get("/milestones/", response_model=List[schemas.Milestone])
def read_milestones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    milestones = crud.get_milestones(db, skip=skip, limit=limit)
    return milestones


@app.put("/milestones/{milestone_id}", response_model=schemas.Milestone)
def update_milestone(
    milestone_id: int, milestone: schemas.MilestoneCreate, db: Session = Depends(get_db)
):
    return crud.update_milestone(db=db, milestone_id=milestone_id, milestone=milestone)


@app.delete("/milestones/{milestone_id}", response_model=schemas.Milestone)
def delete_milestone(milestone_id: int, db: Session = Depends(get_db)):
    return crud.delete_milestone(db=db, milestone_id=milestone_id)
