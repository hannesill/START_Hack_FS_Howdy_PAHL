from datetime import datetime
import random
import requests


# Sample names for mock data
names = [
    "TechWave",
    "GreenInnovate",
    "EduSmart",
    "HealthBridge",
    "FinTechRev",
    "AgriNet",
    "BioSustain",
    "CloudStream",
    "DataSecure",
    "QuantumLeap",
]

startup_template = {
    "name": "",
    "logo": "",
    "description": "",
    "website": "",
    "linkedin": "",
    "address": "",
    "founding_date": "2024-03-21",
    "status": "",
    "phase": "",
    "fte": 0,
    "equity_free_grants_chf": 0,
    "business_model_type": "",
    "target_market": "",
    "kpis": "",
    "last_funding_round": "",
    "last_milestone": "",
    "looking_for": "",
    "last_update": "",
}

# Generate updated mock data with new fields
mock_data_updated = []
for i, name in enumerate(names):
    startup = startup_template.copy()
    startup["name"] = name
    startup["logo"] = (
        f"https://github.com/pigment/fake-logos/blob/gh-pages/logos/medium/color/{i + 1}.png?raw=true"
    )
    startup["description"] = (
        f"{name} is revolutionizing its field through innovative solutions."
    )
    startup["website"] = f"https://{name.lower()}.com"
    startup["linkedin"] = f"https://linkedin.com/company/{name.lower()}"
    startup["address"] = f"1234 {name} Street, Tech City, TC 12345"
    startup["status"] = random.choice(["Working on it", "Crashed", "Exited"])
    startup["phase"] = random.choice(
        ["FFF", "Pre-Seed", "Seed", "Series A", "Series B", "Series C+"]
    )
    startup["fte"] = i * 10 + 5
    startup["equity_free_grants_chf"] = i * 10000
    startup["business_model_type"] = "B2B" if i % 2 == 0 else "B2C"
    startup["target_market"] = "Global" if i % 4 == 0 else "Local"
    startup["kpis"] = f"KPIs related to {startup['phase']} phase"
    startup["last_funding_round"] = f"Series {chr(65+i%3)}"
    startup["last_milestone"] = f"Reached {i*10}% of target market"
    startup["looking_for"] = "Investment" if i % 2 == 0 else "Partnerships"
    startup["last_update"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    mock_data_updated.append(startup)

# Endpoint to post the data to
url = "http://localhost:8000/startups"

# Loop through each item in the mock data list and post it to the endpoint
for data in mock_data_updated:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Successfully posted data for {data['name']}.")
    else:
        print(
            f"Failed to post data for {data['name']}. Response code: {response.status_code}, Message: {response.text}"
        )

# Define sample data for generating founder information
first_names = [
    "Alex",
    "Jordan",
    "Taylor",
    "Morgan",
    "Casey",
    "Riley",
    "Jamie",
    "Avery",
    "Reese",
    "Blake",
]
last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
]
roles = ["CEO", "CTO", "COO", "CFO", "CMO"]
skills = [
    "Leadership",
    "Technical",
    "Business Development",
    "Marketing",
    "Finance",
    "Product Management",
]
education_degrees = ["B.Sc.", "M.Sc.", "Ph.D.", "MBA"]
education_schools = [
    "MIT",
    "Stanford University",
    "Harvard University",
    "University of Cambridge",
    "ETH Zurich",
]
professional_jobs = [
    "Software Engineer",
    "Product Manager",
    "Marketing Specialist",
    "Financial Analyst",
    "Research Scientist",
]
professional_companies = ["Google", "Amazon", "Facebook", "Apple", "Microsoft", "Tesla"]


# Function to generate a random birthdate
def generate_birthdate(start_year=1960, end_year=1995):
    return datetime(
        random.randint(start_year, end_year),
        random.randint(1, 12),
        random.randint(1, 28),
    ).strftime("%Y-%m-%d")


# Generate founder data
founders = []
for i, startup in enumerate(names):
    for _ in range(2):  # 2 founders per startup
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        founder = {
            "name": f"{first_name} {last_name}",
            "image": f"https://randomuser.me/api/portraits/men/{i + 10}.jpg",
            "email": f"{first_name.lower()}.{last_name.lower()}@{startup.lower()}.com",
            "phone": f"+{random.randint(1000000000, 9999999999)}",
            "linkedin": f"https://linkedin.com/in/{first_name.lower()}{last_name.lower()}",
            "address": f"{random.randint(100, 9999)} {random.choice(last_names)} Street, City, Country",
            "birthdate": generate_birthdate(),
            "startup": startup,
            "role": random.choice(roles),
            "skills": random.choice(skills),
            "education_degree": random.choice(education_degrees),
            "education_school": random.choice(education_schools),
            "professional_experience_job": random.choice(professional_jobs),
            "professional_experience_company": random.choice(professional_companies),
        }
        founders.append(founder)


url = "http://localhost:8000/founders"

# Loop through each item in the mock data list and post it to the endpoint
for data in founders:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Successfully posted data for {data['name']}.")
    else:
        print(
            f"Failed to post data for {data['name']}. Response code: {response.status_code}, Message: {response.text}"
        )
