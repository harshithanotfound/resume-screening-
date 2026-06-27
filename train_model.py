import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = {
    "resume_text": [
        "Python Flask FastAPI Django SQL PostgreSQL Docker REST API backend development",
        "Java Spring Boot MySQL microservices backend server development REST API",
        "Node.js Express MongoDB authentication API backend developer",
        "Python FastAPI SQL Docker database backend engineer",

        "HTML CSS JavaScript React Bootstrap frontend responsive design",
        "React Angular TypeScript UI UX frontend web development",
        "Vue JavaScript HTML CSS website frontend developer",
        "Next.js Tailwind CSS frontend UI components",

        "Python pandas numpy machine learning data analysis statistics",
        "SQL Python Power BI Tableau data visualization analytics",
        "Data cleaning feature engineering regression classification models",
        "Excel SQL Python dashboard data analyst",

        "Deep learning PyTorch TensorFlow CNN NLP computer vision",
        "Machine learning scikit-learn model training deployment MLOps",
        "Neural networks image classification transfer learning AI",
        "NLP transformers deep learning model deployment"
    ],
    "category": [
        "Backend Developer",
        "Backend Developer",
        "Backend Developer",
        "Backend Developer",

        "Frontend Developer",
        "Frontend Developer",
        "Frontend Developer",
        "Frontend Developer",

        "Data Scientist",
        "Data Scientist",
        "Data Scientist",
        "Data Scientist",

        "Machine Learning Engineer",
        "Machine Learning Engineer",
        "Machine Learning Engineer",
        "Machine Learning Engineer"
    ]
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(df["resume_text"], df["category"])

os.makedirs("app", exist_ok=True)
joblib.dump(model, "app/model.pkl")

print("Model trained and saved successfully at app/model.pkl")