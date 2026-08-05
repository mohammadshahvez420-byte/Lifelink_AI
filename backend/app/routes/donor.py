from fastapi import APIRouter

router = APIRouter()

@router.get("/donors")
def get_donors():
    return {
        "message": "List of donors will appear here"
    }






from fastapi import APIRouter
from app.models.donor import Donor

router = APIRouter()

@router.get("/")
def get_donors():
    return {
        "message": "List of donors will appear here"
    }

@router.post("/register")
def register_donor(donor: Donor):
    return {
        "message": "Donor registered successfully",
        "donor": donor
    }