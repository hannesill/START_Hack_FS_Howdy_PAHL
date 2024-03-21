import datetime
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import func


def get_startup_by_name(db: Session, name: str):
    startup = db.query(models.Startup).filter(models.Startup.name == name).first()
    if startup:
        startup.founders = (
            db.query(models.Founder).filter(models.Founder.startup == name).all()
        )
    return startup


def get_founder_by_name(db: Session, name: str):
    founder = db.query(models.Founder).filter(models.Founder.name == name).first()
    if founder and founder.startup:
        founder.co_founders = (
            db.query(models.Founder)
            .filter(
                models.Founder.startup == founder.startup, models.Founder.name != name
            )
            .all()
        )
    return founder


def get_all_startups(db: Session):
    return db.query(models.Startup).all()


def get_all_startups_with_no_update(db: Session, delta: int):
    threshold_date = datetime.datetime.now() - datetime.timedelta(days=delta)

    startups_no_update = []

    all_startups = db.query(models.Startup).all()

    for startup in all_startups:
        last_update_dt = datetime.datetime.strptime(
            startup.last_update, "%d/%m/%Y, %H:%M:%S"
        )

        if last_update_dt < threshold_date:
            startups_no_update.append(startup)

    return startups_no_update


def get_all_events(db: Session):
    return db.query(models.EventLog).order_by("timestamp").all()


def get_all_founders(db: Session):
    return db.query(models.Founder).all()


def create_startup(db: Session, startup: schemas.StartupCreate):
    db_startup = models.Startup(**startup.dict())
    db_startup.last_update = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    db.add(db_startup)
    db.commit()
    db.refresh(db_startup)
    return db_startup


def create_founder(db: Session, founder: schemas.FounderCreate):
    db_founder = models.Founder(**founder.dict())
    db_founder.last_update = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    db.add(db_founder)
    db.commit()
    db.refresh(db_founder)
    return db_founder


def update_startup(db: Session, startup_name: str, updates: schemas.StartupUpdate):
    db_startup = (
        db.query(models.Startup).filter(models.Startup.name == startup_name).first()
    )

    if db_startup:
        for var, new_value in vars(updates).items():
            if (
                new_value
            ):  
                old_value = getattr(db_startup, var, None)
                if old_value != new_value:
                    setattr(db_startup, var, new_value)
                    event = models.EventLog(
                        startup_name=startup_name,
                        changed_field=var,
                        old_value=str(
                            old_value
                        ), 
                        new_value=str(new_value),
                        timestamp=datetime.datetime.now().strftime(
                            "%d/%m/%Y, %H:%M:%S"
                        ),
                    )
                    db.add(event)

        setattr(
            db_startup,
            "last_update",
            datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        )

        db.commit()
        db.refresh(db_startup)

    return db_startup


def update_founder(db: Session, founder_name: str, updates: schemas.FounderUpdate):
    db_founder = (
        db.query(models.Founder).filter(models.Founder.name == founder_name).first()
    )
    if db_founder:
        for var, value in vars(updates).items():
            setattr(db_founder, var, value) if value else None
        setattr(
            db_founder,
            "last_update",
            datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        )
        db.commit()
        db.refresh(db_founder)
    return db_founder


def delete_startup(db: Session, startup_name: str):
    db_startup = (
        db.query(models.Startup).filter(models.Startup.name == startup_name).first()
    )
    if db_startup:
        db.delete(db_startup)
        db.commit()
    return db_startup


def delete_founder(db: Session, founder_name: str):
    db_founder = (
        db.query(models.Founder).filter(models.Founder.name == founder_name).first()
    )
    if db_founder:
        db.delete(db_founder)
        db.commit()
    return db_founder


def get_status_counts(db: Session):
    return (
        db.query(
            models.Startup.status, func.count(models.Startup.status).label("count")
        )
        .group_by(models.Startup.status)
        .all()
    )


def get_phase_counts(db: Session):
    return (
        db.query(models.Startup.phase, func.count(models.Startup.phase).label("count"))
        .group_by(models.Startup.phase)
        .all()
    )


def get_avg_fte_and_grants_by_phase(db: Session):
    results = (
        db.query(
            models.Startup.phase,
            func.avg(models.Startup.fte).label("avg_fte"),
            func.avg(models.Startup.equity_free_grants_chf).label(
                "avg_equity_free_grants"
            ),
        )
        .group_by(models.Startup.phase)
        .all()
    )


def get_business_model_counts(db: Session):
    return (
        db.query(
            models.Startup.business_model_type,
            func.count(models.Startup.business_model_type).label("count"),
        )
        .group_by(models.Startup.business_model_type)
        .all()
    )


def get_target_market_counts(db: Session):
    return (
        db.query(
            models.Startup.target_market,
            func.count(models.Startup.target_market).label("count"),
        )
        .group_by(models.Startup.target_market)
        .all()
    )
