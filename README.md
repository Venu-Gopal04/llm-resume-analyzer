# AI Resume Analyzer (Backend Project)

A backend-focused web application that analyzes resumes and provides:
- Resume score (0–100)
- Detected technical skills
- AI/ML readiness feedback

Built using FastAPI with a clean frontend and deployed on Render.

---

## 🔗 Live Demo
https://llm-resume-analyzer.onrender.com

---

## 📂 GitHub Repository
https://github.com/Venu-Gopal04/llm-resume-analyzer

---

## 🛠 Tech Stack
- Python
- FastAPI
- HTML, CSS, JavaScript
- Render (deployment)

---

## ⚙️ Architecture Overview
1. Frontend UI allows users to upload resumes
2. Resume is sent to FastAPI backend
3. Backend extracts text from resume
4. Keywords are matched using weighted scoring logic
5. Resume score and feedback are returned as JSON
6. UI displays score, skills, and summary

---

## 🔌 API Endpoint

**Input:** Resume file  
**Output:**  
- resume_score  
- skills_found  
- summary  

---

## 📈 Resume Scoring Logic
Each skill has a weight:
- Python: 15
- FastAPI: 10
- SQL: 10
- Machine Learning: 20
- Deep Learning: 20
- NLP: 15
- LLM: 20
- AI: 10

Score is capped at 100.

---

## 🧪 Minimal Evaluation
Tested with 5 resumes:
- AI-heavy resumes scored higher
- Non-AI resumes scored lower
- Skill detection matched expected keywords

This confirms acceptable precision for an internship-level project.

---

## ⚠️ Limitations & Trade-offs
- Uses keyword-based analysis (no semantic embeddings)
- No PDF parsing optimizations
- No job-description comparison

---

## 🚀 Future Improvements
- Add embedding-based semantic matching
- Compare resume with job descriptions
- Use LLM-generated personalized feedback
- Add authentication and logging

---

## 👨‍💻 Author
Venu Gopal  
Backend / AI Intern Aspirant
