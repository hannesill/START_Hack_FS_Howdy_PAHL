from datetime import date
from typing import List

# Mock data generation for the models

# KPIs
kpis = [
    {
        "name": "Monthly Active Users",
        "value": 12000.0,
        "unit": "users",
        "description": "The number of unique users who engage with our product in a month",
        "is_north_star": True,
    },
    {
        "name": "Customer Acquisition Cost",
        "value": 30.0,
        "unit": "USD",
        "description": "The cost associated with convincing a customer to buy a product/service",
        "is_north_star": False,
    },
]

# Social Media
social_media = [
    {"name": "Twitter", "link": "https://twitter.com/OurStartup"},
    {"name": "LinkedIn", "link": "https://www.linkedin.com/company/OurStartup"},
]

# Address
address = {
    "street": "123 Innovation Drive",
    "city": "Techville",
    "state": "CA",
    "zip": "94016",
    "country": "USA",
}

# Founding Rounds
founding_rounds = [
    {"date": date(2020, 1, 1), "round": "Seed"},
    {"date": date(2021, 6, 15), "round": "Series A"},
]

# FTEs
ftes = [
    {"country": "USA", "number_of_employees": 50},
    {"country": "Canada", "number_of_employees": 10},
]

# Founder
founder = {
    "name": "Alex Smith",
    "email": "alex@ourstartup.com",
    "phone": "+1234567890",
    "address": address,
    "birthday": date(1985, 7, 4),
    "skills": [{"name": "Leadership"}, {"name": "Programming"}],
    "education": ["BS in Computer Science", "MBA"],
    "professional_experience": [
        "Software Developer at TechCorp",
        "CTO at InnovateStartup",
    ],
}

# Startup
startup = {
    "name": "OurStartup",
    "description": "We offer innovative solutions to common problems.",
    "adress": address,
    "website": "https://ourstartup.com",
    "social_media": social_media,
    "target_market": "Tech Enthusiasts",
    "milestones": ["Launched MVP", "Reached 10K users"],
    "challenges": ["Scaling infrastructure", "User acquisition"],
    "intellectual_properties": "Patents in AI and machine learning algorithms",
    "industry": "Technology",
    "founding_rounds": founding_rounds,
    "kpis": kpis,
    "fs_acceleator_participation": date(2019, 9, 1),
    "fs_incubator_participation": date(2019, 3, 1),
    "fs_acceleator_participation_type": "Full-time",
    "status": "Working on it",
    "phase": "Series A",
    "founding_date": date(2018, 5, 15),
    "ftes": ftes,
    "business_model": "B2C",
    "equity_free_grants": 50000.0,
}
