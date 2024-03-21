from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from src.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String(255), index=True)
    zip = Column(String(20), index=True)
    city = Column(String(100), index=True)
    country = Column(String(100), index=True)


class Founder(Base):
    __tablename__ = "founders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    picture = Column(String(255))
    mail = Column(String(255))
    phone = Column(String(25))
    linkedin = Column(String(255))
    address_id = Column(Integer, ForeignKey("addresses.id"))
    birthdate = Column(String(10))
    last_update = Column(String(20))

    address = relationship("Address")


class StartUp(Base):
    __tablename__ = "startups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(Text)  # Assuming potentially long text
    logo = Column(String(255))
    website = Column(String(255))
    linkedin = Column(String(255))
    address_id = Column(Integer, ForeignKey("addresses.id"))
    industry = Column(String(255))
    founding_date = Column(String(10))  # Assuming date in 'YYYY-MM-DD'
    status = Column(String(255))
    phase = Column(String(255))
    fte = Column(Integer)
    equity_free_grants = Column(Integer)
    business_model = Column(String(255))
    target_market = Column(String(255))
    last_update = Column(String(20))  # Adjust based on your datetime format

    address = relationship("Address")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)


class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)


class Investor(Base):
    __tablename__ = "investors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)


class KPI(Base):
    __tablename__ = "kpis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    value = Column(String(255))
    unit = Column(String(255))
    date = Column(String(10))  # Assuming date in 'YYYY-MM-DD'
    is_northstar = Column(Boolean)


class FoundingRound(Base):
    __tablename__ = "founding_rounds"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    amount = Column(Integer)
    unit = Column(String(255))
    date = Column(String(10))  # Assuming date in 'YYYY-MM-DD'


class Milestone(Base):
    __tablename__ = "milestones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)
    status = Column(String(255))
