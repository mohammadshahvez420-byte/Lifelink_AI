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