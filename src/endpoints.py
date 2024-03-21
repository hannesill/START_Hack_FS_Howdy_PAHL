from fastapi import FastAPI, HTTPException
from src.database import Neo4jConnection
from src.models import TestFounder

app = FastAPI()
db = Neo4jConnection()


@app.post("/founders/")
async def create_founder(founder: TestFounder):
    founder.birthdate = str(founder.birthdate)
    founder.last_update = str(founder.last_update)
    query = """
    CREATE (f:Founder {id: $id, name: $name, picture: $picture, mail: $mail, phone: $phone, linkedin: $linkedin, birthdate: $birthdate, last_update: $last_update})
    RETURN f
    """
    result = db.query(query, parameters=founder.dict())
    if result:
        return {"message": "Founder created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create founder")


@app.put("/founders/{founder_id}")
async def update_founder(founder_id: int, founder: TestFounder):
    founder.birthdate = str(founder.birthdate)
    founder.last_update = str(founder.last_update)
    query = """
    MATCH (f:Founder {id: $id})
    SET f.name = $name, f.picture = $picture, f.mail = $mail, f.phone = $phone, f.linkedin = $linkedin, f.birthdate = $birthdate, f.last_update = $last_update
    RETURN f
    """
    result = db.query(query, parameters={"id": founder_id, **founder.dict()})
    if result:
        return {"message": "Founder updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Founder not found")


@app.delete("/founders/{founder_id}")
async def delete_founder(founder_id: int):
    query = "MATCH (f:Founder {id: $id}) DELETE f"
    result = db.query(query, parameters={"id": founder_id})
    if result:
        return {"message": "Founder deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Founder not found")
