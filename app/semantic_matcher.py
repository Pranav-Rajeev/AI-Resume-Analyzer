import numpy as np
from fastembed import TextEmbedding


model = TextEmbedding("sentence-transformers/all-MiniLM-L6-v2")


def calculate_semantic_similarity(resume_text, job_description):

    vectors = list(
        model.embed([
            resume_text,
            job_description
        ])
    )

    resume_embedding = vectors[0]
    job_embedding = vectors[1]

    similarity = float(
        np.dot(
            resume_embedding,
            job_embedding
        ) / (
            np.linalg.norm(resume_embedding) *
            np.linalg.norm(job_embedding)
        )
    )

    score = similarity * 100

    return round(score, 2)