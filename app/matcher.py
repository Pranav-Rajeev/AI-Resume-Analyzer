def calculate_match(resume_skills, job_skills):

    if not job_skills:
        return {
            "match_score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    match_score = (len(matched_skills) / len(job_skills)) * 100

    return {
        "match_score": round(match_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }