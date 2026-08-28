def calculate_overall_score(skill_score, semantic_score):

    overall_score = (skill_score * 0.5) + (semantic_score * 0.5)

    return round(overall_score, 2)