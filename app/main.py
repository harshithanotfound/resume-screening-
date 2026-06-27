import os
import joblib
from pathlib import Path

try:
    from fastapi import FastAPI, HTTPException
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import FileResponse
except ImportError as exc:
    raise ImportError("FastAPI is not installed. Install it with 'pip install fastapi'.") from exc

from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="AI Resume Screening System",
    description="Resume analyzer with ML role prediction and ATS score.",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model not found. Please run: python train_model.py")

model = joblib.load(MODEL_PATH)

SKILLS = [
    "python", "java", "sql", "mysql", "postgresql", "mongodb",
    "html", "css", "javascript", "react", "angular", "vue",
    "flask", "django", "fastapi", "spring boot", "node.js", "express",
    "machine learning", "deep learning", "tensorflow", "pytorch",
    "scikit-learn", "nlp", "computer vision",
    "pandas", "numpy", "power bi", "tableau", "excel",
    "docker", "git", "github", "aws", "rest api", "microservices"
]


class ResumeInput(BaseModel):
    resume_text: str = Field(..., min_length=10)
    job_description: str = Field(..., min_length=10)


@app.get("/")
def home():
    return FileResponse("app/static/index.html")


@app.get("/health")
def health_check():
    return {
        "status": "running",
        "model_loaded": True
    }


@app.post("/analyze")
def analyze_resume(data: ResumeInput):
    resume_text = data.resume_text.lower().strip()
    job_description = data.job_description.lower().strip()

    if not resume_text or not job_description:
        raise HTTPException(
            status_code=400,
            detail="Resume text and job description are required."
        )

    predicted_role = model.predict([resume_text])[0]
    confidence = round(float(max(model.predict_proba([resume_text])[0])) * 100, 2)

    required_skills = sorted([
        skill for skill in SKILLS if skill in job_description
    ])

    resume_skills = sorted([
        skill for skill in SKILLS if skill in resume_text
    ])

    matched_skills = sorted(list(set(required_skills) & set(resume_skills)))
    missing_skills = sorted(list(set(required_skills) - set(resume_skills)))

    if required_skills:
        ats_score = round((len(matched_skills) / len(required_skills)) * 100, 2)
    else:
        ats_score = confidence

    if ats_score >= 80:
        recommendation = "Excellent match. Your resume is strong for this role."
    elif ats_score >= 60:
        recommendation = "Good match. Add the missing skills to improve your resume."
    else:
        recommendation = "Needs improvement. Add more job-related skills and relevant projects."

    return {
        "predicted_role": predicted_role,
        "confidence": confidence,
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation
    }