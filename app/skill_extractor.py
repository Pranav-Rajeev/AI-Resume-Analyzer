import re


SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "c",

    # Web Development
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "express.js",
    "fastapi",
    "flask",
    "django",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",
    "redis",

    # AI / Machine Learning
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "large language models",
    "llm",

    # ML Libraries
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "keras",
    "opencv",

    # Data
    "data analysis",
    "data science",
    "data visualization",
    "power bi",
    "tableau",

    # Cloud / DevOps
    "aws",
    "azure",
    "google cloud",
    "gcp",
    "docker",
    "kubernetes",

    # Tools
    "git",
    "github",
    "gitlab",
    "linux",
    "rest api",
    "api"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters such as +, # and .
        escaped_skill = re.escape(skill)

        # Use word boundaries for accurate matching
        pattern = r"\b" + escaped_skill + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills