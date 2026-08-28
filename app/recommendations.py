# ============================================================
# AI RESUME ANALYZER
# RECOMMENDATION SYSTEM
# ============================================================


def generate_recommendations(
    missing_skills,
    ats_result=None,
    skill_score=0,
    semantic_score=0
):

    recommendations = []


    # ========================================================
    # SKILL-SPECIFIC RECOMMENDATIONS
    # ========================================================

    skill_recommendations = {

        "python":
            "Strengthen your Python experience by adding practical Python projects and measurable achievements to your resume.",

        "fastapi":
            "FastAPI: Add a backend/API project using FastAPI to demonstrate practical API development experience.",

        "sql":
            "SQL: Add database-related projects demonstrating SQL queries, database design, joins, and data management.",

        "machine learning":
            "Machine Learning: Add a machine-learning project describing the dataset, model used, evaluation results, and your contribution.",

        "tensorflow":
            "TensorFlow: Build or add a TensorFlow deep-learning project and mention the model, dataset, and results in your resume.",

        "aws":
            "AWS: Deploy one of your projects using an AWS service such as EC2, S3, or Lambda and mention the deployment experience.",

        "docker":
            "Docker: Containerize one of your projects and mention Docker-based deployment or development experience.",

        "git":
            "Git: Use Git/GitHub for your projects and mention version control, branching, commits, and collaborative development experience.",

        "java":
            "Java: Add a Java-based project or describe your Java development experience with specific technologies and results.",

        "c":
            "C: Include a C programming project or relevant systems/programming experience to demonstrate practical C knowledge.",

        "html":
            "HTML: Add a web-development project demonstrating your HTML skills and describe the functionality you implemented.",

        "css":
            "CSS: Mention responsive UI or frontend projects where you used CSS to create and style interfaces.",

        "linux":
            "Linux: Mention practical Linux experience such as command-line usage, system administration, development environments, or deployment.",

        "api":
            "API Development: Add a project that consumes or develops REST APIs and describe the endpoints and functionality you implemented."

    }


    # ========================================================
    # GENERATE MISSING-SKILL RECOMMENDATIONS
    # ========================================================

    if missing_skills:

        for skill in missing_skills:

            skill_name = str(skill).lower().strip()


            if skill_name in skill_recommendations:

                recommendations.append(
                    skill_recommendations[skill_name]
                )

            else:

                recommendations.append(
                    f"{skill}: Consider learning this skill and adding a relevant project or practical experience to your resume."
                )


    # ========================================================
    # SKILL MATCH SCORE RECOMMENDATION
    # ========================================================

    try:

        skill_score = float(skill_score)

    except:

        skill_score = 0


    if skill_score < 50:

        recommendations.append(
            "Your skill match is relatively low. Focus on adding more skills that directly appear in the target job description."
        )

    elif skill_score < 75:

        recommendations.append(
            "Your skill match is moderate. Add a few more job-relevant skills and demonstrate them through projects or experience."
        )

    else:

        recommendations.append(
            "Your skill match is strong. Keep your most relevant skills clearly visible near the top of your resume."
        )


    # ========================================================
    # SEMANTIC SCORE RECOMMENDATION
    # ========================================================

    try:

        semantic_score = float(semantic_score)

    except:

        semantic_score = 0


    if semantic_score < 50:

        recommendations.append(
            "Your resume has a relatively low semantic match with the job description. Use terminology and project descriptions that better reflect the target role."
        )

    elif semantic_score < 75:

        recommendations.append(
            "Your semantic match is moderate. Improve your project and experience descriptions by using terminology relevant to the target position."
        )

    else:

        recommendations.append(
            "Your resume content is semantically well aligned with the job description. Maintain this relevance while keeping the descriptions concise."
        )


    # ========================================================
    # ATS SCORE RECOMMENDATION
    # ========================================================

    ats_score = 0


    if isinstance(ats_result, dict):

        try:

            ats_score = float(
                ats_result.get(
                    "ats_score",
                    0
                )
            )

        except:

            ats_score = 0


    if ats_score < 50:

        recommendations.append(
            "Improve your ATS compatibility by using clear section headings, standard resume formatting, and relevant job-specific keywords."
        )

    elif ats_score < 80:

        recommendations.append(
            "Your ATS score is moderate. Improve keyword relevance and make important technical skills easy for applicant-tracking systems to identify."
        )

    else:

        recommendations.append(
            "Your ATS score is strong. Continue using clear formatting and relevant keywords without unnecessarily repeating them."
        )


    # ========================================================
    # GENERAL RESUME RECOMMENDATION
    # ========================================================

    recommendations.append(
        "Use measurable results wherever possible, such as accuracy improvements, project performance, processing time, or the number of users/features implemented."
    )


    # ========================================================
    # REMOVE DUPLICATES
    # ========================================================

    unique_recommendations = []


    for recommendation in recommendations:

        if recommendation not in unique_recommendations:

            unique_recommendations.append(
                recommendation
            )


    # ========================================================
    # RETURN RESULTS
    # ========================================================

    return unique_recommendations