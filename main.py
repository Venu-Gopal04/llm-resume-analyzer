from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
from openai import OpenAI

from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles

from database import Base, engine, SessionLocal
from models import Profile

# ✅ LOAD ENV + INIT OPENAI (PASTE HERE)
load_dotenv()
print("DEBUG OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
client = OpenAI()

app = FastAPI(title="Me API Playground")
# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/profile")
def create_profile(profile: dict):
    db = SessionLocal()
    new_profile = Profile(**profile)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    db.close()
    return {"message": "Profile saved successfully"}


@app.get("/profile")
def get_profile():
    db = SessionLocal()
    profiles = db.query(Profile).all()
    db.close()
    return profiles


@app.get("/projects")
def search_projects(skill: str):
    db = SessionLocal()
    results = db.query(Profile).filter(Profile.skills.contains(skill)).all()
    db.close()
    return results
from fastapi import UploadFile, File

@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode(errors="ignore").lower()

    skills_db = [
        "python", "fastapi", "sql", "machine learning",
        "deep learning", "ai", "llm", "nlp"
    ]

    found_skills = [skill for skill in skills_db if skill in text]

    score = min(len(found_skills) * 20 + (10 if "python" in found_skills else 0), 100)


    summary = (
        "Excellent AI/ML profile"
        if score >= 70
        else "Good backend / AI foundation"
        if score >= 40
        else "Needs more AI/ML keywords"
    )

    return {
        "skills_found": found_skills,
        "resume_score": score,
        "summary": summary
    }
@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode(errors="ignore").lower()

    skills_db = [
        "python", "fastapi", "sql", "machine learning",
        "deep learning", "ai", "llm", "nlp"
    ]

    found_skills = [skill for skill in skills_db if skill in text]

    score = min(len(found_skills) * 15 + (10 if "python" in found_skills else 0), 100)

    summary = (
        "Excellent AI/ML profile"
        if score >= 70
        else "Good AI/ML foundation"
        if score >= 40
        else "Needs more AI/ML keywords"
    )

    return {
        "skills_found": found_skills,
        "resume_score": score,
        "summary": summary
    }










