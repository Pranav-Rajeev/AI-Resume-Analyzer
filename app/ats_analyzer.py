import re


def analyze_resume(resume_text):

    text = resume_text.lower()

    analysis = {}

    # Check email
    email_found = bool(
        re.search(r'[\w\.-]+@[\w\.-]+\.\w+', resume_text)
    )

    # Check phone number
    phone_found = bool(
        re.search(r'(\+?\d[\d\s\-]{8,}\d)', resume_text)
    )

    # Check important resume sections
    sections = {
        "education": [
            "education",
            "academic",
            "degree",
            "b.tech",
            "bachelor"
        ],

        "experience": [
            "experience",
            "work experience",
            "employment",
            "internship"
        ],

        "projects": [
            "projects",
            "project"
        ],

        "skills": [
            "skills",
            "technical skills",
            "technologies"
        ],

        "certifications": [
            "certification",
            "certifications",
            "certificate"
        ]
    }

    section_results = {}

    for section, keywords in sections.items():

        found = any(
            keyword in text
            for keyword in keywords
        )

        section_results[section] = found

    # Calculate ATS score
    score = 0

    if email_found:
        score += 15

    if phone_found:
        score += 15

    for found in section_results.values():

        if found:
            score += 14

    # Maximum score = 100
    score = min(score, 100)

    return {
        "ats_score": score,
        "email_found": email_found,
        "phone_found": phone_found,
        "sections": section_results
    }