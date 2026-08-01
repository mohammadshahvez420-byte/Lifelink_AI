from fastapi import FastAPI

app = FastAPI(
    title="LifeLink AI",
    description="AI-Powered Blood Donor Search System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to LifeLink AI 🚑"
    }  



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="LifeLink AI",
    description="AI-Powered Blood Donor Search System",
    version="1.0.0"
)

class Donor(BaseModel):
    name: str
    age: int
    blood_group: str
    city: str
    phone: str

@app.get("/")
def home():
    return {
        "message": "Welcome to LifeLink AI 🚑"
    }

@app.post("/donors/register")
def register_donor(donor: Donor):
    return {
        "message": "Donor registered successfully",
        "donor": donor
    }