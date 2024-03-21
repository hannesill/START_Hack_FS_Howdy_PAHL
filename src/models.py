import datetime
from sqlalchemy import (
    Column,
    Date,
    String,
    Integer,
    DateTime,
)

from src.database import Base


class Founder(Base):
    __tablename__ = "founder"
    name = Column(String(255), primary_key=True)
    image = Column(String(512))
    email = Column(String(255))
    phone = Column(String(255))
    linkedin = Column(String(255))
    address = Column(String(512))
    birthdate = Column(String(255))
    startup = Column(String(255))
    role = Column(String(255))
    skills = Column(String(512))
    education_degree = Column(String(255))
    education_school = Column(String(255))
    professional_experience_job = Column(String(255))
    professional_experience_company = Column(String(255))
    last_update = Column(String(255))


class Startup(Base):
    __tablename__ = "startup"
    name = Column(String(255), primary_key=True)
    logo = Column(String(512))
    description = Column(String(512))
    website = Column(String(255))
    linkedin = Column(String(255))
    address = Column(String(512))
    founding_date = Column(String(255))
    status = Column(String(255))
    phase = Column(String(255))
    fte = Column(Integer())
    equity_free_grants_chf = Column(Integer())
    business_model_type = Column(String(255))
    target_market = Column(String(255))
    last_update = Column(String(255))
    kpis = Column(String(512))
    last_funding_round = Column(String(512))
    last_milestone = Column(String(512))
    looking_for = Column(String(512))


class EventLog(Base):
    __tablename__ = "event_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    startup_name = Column(String(512), nullable=False)
    changed_field = Column(String(512), nullable=False)
    old_value = Column(String(512), nullable=True)
    new_value = Column(String(512), nullable=False)
    timestamp = Column(String(512), nullable=False)


