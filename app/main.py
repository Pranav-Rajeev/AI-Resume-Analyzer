from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse

import shutil
import os

from app.resume_parser import extract_text_from_pdf
from app.skill_extractor import extract_skills
from app.matcher import calculate_match
from app.semantic_matcher import calculate_semantic_similarity
from app.score_calculator import calculate_overall_score
from app.ats_analyzer import analyze_resume as ats_analyze
from app.recommendations import generate_recommendations


# ============================================================
# CREATE FASTAPI APP
# ============================================================

app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered Resume Analyzer and Job Matcher",
    version="1.0"
)


# ============================================================
# FRONTEND
# ============================================================

@app.get("/app")
def frontend():

    return FileResponse(
        "frontend/index.html"
    )


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "AI Resume Analyzer is running!"
    }


# ============================================================
# UPLOAD RESUME
# ============================================================

@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    # Check file type

    if not file.filename.lower().endswith(".pdf"):

        return {
            "message": "Please upload a PDF resume."
        }


    # Create uploads folder

    upload_folder = "uploads"

    if not os.path.exists(upload_folder):

        os.makedirs(upload_folder)


    # Create file path

    file_path = os.path.join(
        upload_folder,
        file.filename
    )


    # Save uploaded file

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    # Extract text from PDF

    resume_text = extract_text_from_pdf(
        file_path
    )


    # Extract skills

    skills = extract_skills(
        resume_text
    )


    return {
        "message": "Resume uploaded successfully!",
        "filename": file.filename,
        "resume_text": resume_text,
        "skills": skills
    }


# ============================================================
# JOB DESCRIPTION
# ============================================================

@app.post("/job-description")
async def job_description(
    description: str = Form(...)
):

    # Extract required skills

    job_skills = extract_skills(
        description
    )


    return {
        "message": "Job description received successfully!",
        "job_description": description,
        "job_skills": job_skills
    }


# ============================================================
# BASIC SKILL MATCHING
# ============================================================

@app.post("/match-resume")
async def match_resume(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):

    # Extract resume skills

    resume_skills = extract_skills(
        resume_text
    )


    # Extract job skills

    job_skills = extract_skills(
        job_description
    )


    # Calculate skill match

    result = calculate_match(
        resume_skills,
        job_skills
    )


    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "match_score": result["match_score"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"]
    }


# ============================================================
# AI SEMANTIC MATCHING
# ============================================================

@app.post("/semantic-match")
async def semantic_match(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):

    # Calculate semantic similarity

    semantic_score = calculate_semantic_similarity(
        resume_text,
        job_description
    )


    return {
        "semantic_match_score": semantic_score
    }


# ============================================================
# COMPLETE RESUME ANALYSIS
# ============================================================

@app.post("/analyze")
async def analyze_resume(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):

    # --------------------------------------------------------
    # 1. Extract resume skills
    # --------------------------------------------------------

    resume_skills = extract_skills(
        resume_text
    )


    # --------------------------------------------------------
    # 2. Extract job skills
    # --------------------------------------------------------

    job_skills = extract_skills(
        job_description
    )


    # --------------------------------------------------------
    # 3. Calculate skill matching
    # --------------------------------------------------------

    skill_result = calculate_match(
        resume_skills,
        job_skills
    )


    skill_score = skill_result["match_score"]


    # --------------------------------------------------------
    # 4. AI semantic matching
    # --------------------------------------------------------

    semantic_score = calculate_semantic_similarity(
        resume_text,
        job_description
    )


    # --------------------------------------------------------
    # 5. Calculate overall score
    # --------------------------------------------------------

    overall_score = calculate_overall_score(
        skill_score,
        semantic_score
    )


    # --------------------------------------------------------
    # 6. ATS analysis
    # --------------------------------------------------------

    # IMPORTANT:
    # We use ats_analyze here to avoid the
    # analyze_resume naming conflict.

    ats_result = ats_analyze(
        resume_text
    )


    # --------------------------------------------------------
    # 7. Generate recommendations
    # --------------------------------------------------------

    recommendations = generate_recommendations(
        skill_result["missing_skills"],
        ats_result,
        skill_score,
        semantic_score
    )


    # --------------------------------------------------------
    # 8. Return complete analysis
    # --------------------------------------------------------

    return {

        "overall_match_score": overall_score,

        "skill_match_score": skill_score,

        "semantic_match_score": semantic_score,

        "ats_score": ats_result["ats_score"],

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "matched_skills":
            skill_result["matched_skills"],

        "missing_skills":
            skill_result["missing_skills"],

        "recommendations":
            recommendations
    }


# ============================================================
# ATS ANALYSIS ONLY
# ============================================================

@app.post("/ats-analysis")
async def ats_analysis(
    resume_text: str = Form(...)
):

    # Run ATS analyzer

    result = ats_analyze(
        resume_text
    )


    return result