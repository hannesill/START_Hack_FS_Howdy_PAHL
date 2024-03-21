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


@app.get("/startups/{startup_name}", response_model=schemas.Startup)
def read_startup(startup_name: str, db: Session = Depends(get_db)):
    db_startup = crud.get_startup_by_name(db, name=startup_name)
    if db_startup is None:
        raise HTTPException(status_code=404, detail="Startup not found")
    return db_startup


@app.get("/founders/{founder_name}", response_model=schemas.Founder)
def read_founder(founder_name: str, db: Session = Depends(get_db)):
    db_founder = crud.get_founder_by_name(db, name=founder_name)
    if db_founder is None:
        raise HTTPException(status_code=404, detail="Founder not found")
    return db_founder


@app.get("/startups/", response_model=List[schemas.Startup])
def read_all_startups(db: Session = Depends(get_db)):
    startups = crud.get_all_startups(db)
    return startups


@app.get("/founders/", response_model=List[schemas.Founder])
def read_all_founders(db: Session = Depends(get_db)):
    founders = crud.get_all_founders(db)
    return founders


@app.post("/startups/", response_model=schemas.Startup)
def create_a_startup(startup: schemas.StartupCreate, db: Session = Depends(get_db)):
    return crud.create_startup(db, startup=startup)


@app.post("/founders/", response_model=schemas.Founder)
def create_a_founder(founder: schemas.FounderCreate, db: Session = Depends(get_db)):
    return crud.create_founder(db, founder=founder)


@app.put("/startups/{startup_name}", response_model=schemas.Startup)
def update_a_startup(
    startup_name: str, startup: schemas.StartupUpdate, db: Session = Depends(get_db)
):
    return crud.update_startup(db, startup_name=startup_name, updates=startup)


@app.put("/founders/{founder_name}", response_model=schemas.Founder)
def update_a_founder(
    founder_name: str, founder: schemas.FounderUpdate, db: Session = Depends(get_db)
):
    return crud.update_founder(db, founder_name=founder_name, updates=founder)


@app.delete("/startups/{startup_name}", response_model=schemas.Startup)
def delete_a_startup(startup_name: str, db: Session = Depends(get_db)):
    return crud.delete_startup(db, startup_name=startup_name)


@app.delete("/founders/{founder_name}", response_model=schemas.Founder)
def delete_a_founder(founder_name: str, db: Session = Depends(get_db)):
    return crud.delete_founder(db, founder_name)


@app.get("/events/", response_model=List[schemas.Events])
def get_all_events(db: Session = Depends(get_db)):
    return crud.get_all_events(db)


@app.get("/startups/no-update/{delta}", response_model=List[schemas.Startup])
def read_startups_no_update(delta: int, db: Session = Depends(get_db)):
    startups = crud.get_all_startups_with_no_update(db, delta)
    return startups


@app.get("/dashboard/summaries")
def get_dashboard_summaries(db: Session = Depends(get_db)):
    status_counts = [
        {"status": status, "count": count}
        for status, count in crud.get_status_counts(db)
    ]
    phase_counts = [
        {"phase": phase, "count": count} for phase, count in crud.get_phase_counts(db)
    ]

    avg_fte_grants_raw = crud.get_avg_fte_and_grants_by_phase(db)
    avg_fte_grants = (
        [
            {
                "phase": item[0],
                "avg_fte": item[1],
                "avg_equity_free_grants_chf": item[2],
            }
            for item in avg_fte_grants_raw
        ]
        if avg_fte_grants_raw
        else []
    )

    business_model_counts = [
        {"business_model_type": model, "count": count}
        for model, count in crud.get_business_model_counts(db)
    ]
    target_market_counts = [
        {"target_market": market, "count": count}
        for market, count in crud.get_target_market_counts(db)
    ]

    return {
        "status_counts": status_counts,
        "phase_counts": phase_counts,
        "avg_fte_grants": avg_fte_grants,
        "business_model_counts": business_model_counts,
        "target_market_counts": target_market_counts,
    }
