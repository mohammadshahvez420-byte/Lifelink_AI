from fastapi import APIRouter
from app.models.donor import Donor

router = APIRouter()

# Temporary donor storage
donors = []

@router.get("/")
def get_donors():
    return donors

@router.post("/register")
def register_donor(donor: Donor):
    donors.append(donor)
    return {
        "message": "Donor registered successfully",
        "donor": donor
    }