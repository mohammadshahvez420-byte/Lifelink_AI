from pydantic import BaseModel

class Donor(BaseModel):
    name: str
    age: int
    blood_group: str
    city: str
    phone: str