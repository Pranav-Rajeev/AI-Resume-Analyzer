from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(resume_text, job_description):

    # Convert resume and job description into embeddings
    resume_embedding = model.encode(
        resume_text,
        convert_to_numpy=True
    )

    job_embedding = model.encode(
        job_description,
        convert_to_numpy=True
    )

    # Calculate similarity
    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    # Convert similarity to percentage
    score = similarity * 100

    return round(float(score), 2)