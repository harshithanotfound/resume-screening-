# 🚀 AI Resume Screening System

## 📌 Overview

The AI Resume Screening System is a web-based application that analyzes a candidate's resume against a job description using Natural Language Processing (NLP) and Machine Learning.

The application predicts the most suitable job role, calculates an ATS (Applicant Tracking System) score, identifies matched and missing skills, and provides personalized recommendations to improve the resume.

This project demonstrates how Machine Learning models can be deployed as a real-world web application using FastAPI.

---

# ✨ Features

* 📄 Analyze resume text
* 💼 Compare resume with a job description
* 🤖 Predict the most suitable job role
* 📊 Generate an ATS Match Score
* ✅ Display matched skills
* ❌ Identify missing skills
* 💡 Provide resume improvement suggestions
* 🌐 Interactive web interface
* ⚡ FastAPI backend
* 🐳 Docker support for deployment

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* FastAPI
* Uvicorn

### Machine Learning

* Scikit-learn
* Logistic Regression
* TF-IDF Vectorizer

### Data Processing

* Pandas
* Joblib

### Deployment

* Docker

---

# 📂 Project Structure

```
AI-Resume-Screening-System/

│
├── app/
│   ├── main.py
│   ├── model.pkl
│   └── static/
│       ├── index.html
│       ├── style.css
│       └── script.js
│
├── train_model.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd AI-Resume-Screening-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the application

```bash
uvicorn app.main:app --reload
```

---

# 🌍 Open in Browser

Main Website

```
http://127.0.0.1:8000
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📥 Input

### Resume Text

```
Python
FastAPI
SQL
Docker
REST API
GitHub
```

### Job Description

```
Backend Developer

Required Skills

Python
FastAPI
SQL
Docker
GitHub
REST API
```

---

# 📤 Sample Output

```
Predicted Role

Backend Developer

ATS Score

100%

Matched Skills

✔ Python
✔ FastAPI
✔ SQL
✔ Docker
✔ GitHub
✔ REST API

Missing Skills

None

Recommendation

Excellent match. Your resume is well aligned with the selected job role.
```

---

# 🧠 Machine Learning Workflow

```
Resume Text
        │
        ▼
Text Cleaning
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Logistic Regression Model
        │
        ▼
Predicted Job Role
        │
        ▼
ATS Score
        │
        ▼
Resume Suggestions
```

---

# 🎯 Learning Outcomes

Through this project I learned:

* Building REST APIs using FastAPI
* Deploying Machine Learning models
* Natural Language Processing using TF-IDF
* Resume classification using Logistic Regression
* Backend development with Python
* API testing using Swagger
* Docker containerization
* Building a complete web application by integrating frontend and backend

---

# 🚀 Future Improvements

* Upload PDF resumes
* Upload DOCX resumes
* Automatic resume parsing
* Skill extraction using Named Entity Recognition (NER)
* Semantic similarity using Sentence Transformers
* Support for multiple job descriptions
* User authentication
* Resume history dashboard
* Cloud deployment

---

# 👨‍💻 Author

**Harshitha**

This project was developed as a hands-on Machine Learning deployment project to understand the complete workflow of converting a trained model into a real-world web application using FastAPI and Docker.
