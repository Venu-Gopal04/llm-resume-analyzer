# AI Resume Analyzer (Backend Project)

A backend-focused web application that analyzes resumes and provides:
- Resume score (0–100)
- Detected technical skills
- AI/ML readiness feedback

Built using FastAPI with a simple frontend and deployed on Render.

---

## 🔗 Live Demo
https://llm-resume-analyzer.onrender.com

---

## 📂 GitHub Repository
https://github.com/Venu-Gopal04/llm-resume-analyzer

---

## 🛠 Tech Stack
- Python 3.10+
- FastAPI
- HTML, CSS, JavaScript
- Render (deployment)

---

## ⚙️ Architecture Overview
1. Frontend UI allows users to upload resumes
2. Resume is sent to FastAPI backend via REST API
3. Backend reads and decodes resume text
4. Keywords are matched using weighted scoring logic
5. Resume score and feedback are returned as JSON
6. UI renders score, skills, and summary

---

## 🔌 API Schema

### POST `/analyze-resume`

**Input**
- Multipart form-data
- Field: `file` (resume file)

**Response**
   json
{
  "resume_score": 70,
  "skills_found": ["python", "fastapi", "ml"],
  "summary": "Good backend / AI foundation"
}


## Resume Scoring Logic

The resume analyzer uses a weighted keyword-based scoring mechanism.

Each important skill contributes a predefined weight to the final score:

- Python: 15 points  
- FastAPI: 10 points  
- SQL: 10 points  
- Machine Learning: 20 points  
- Deep Learning: 20 points  
- NLP: 15 points  
- LLM / AI: 10 points  

The resume text is decoded and converted to lowercase.  
If a keyword is found, its corresponding weight is added to the score.

The final score is capped at **100**.



## Minimal Evaluation

The system was tested using multiple resumes with varying skill sets.

Example evaluation:

| Resume Type | Detected Skills | Score |
|------------|---------------|-------|
| AI-focused resume | Python, ML, DL, NLP | 75 |
| Backend resume | Python, FastAPI, SQL | 35 |
| Non-technical resume | None | 0 |

This demonstrates that the scoring logic differentiates resumes based on relevant skills.

---

## Remarks (Limitations & Trade-offs)

- This version uses **keyword matching**, not semantic understanding.
- No embeddings or vector search are used.
- PDF/DOC formatting noise may affect keyword detection.
- Scoring logic is rule-based, not learned.

These trade-offs were chosen to keep the system **simple, explainable, and production-ready for an internship task**.

---

## Future Improvements

- Add semantic search using embeddings
- Support PDF/DOC parsing with better text extraction
- Introduce role-based scoring (AI Engineer, Backend, Data Scientist)
- Integrate LLM-based feedback generation
- Store historical resume analysis results

---

## Local Setup Instructions

  
git clone https://github.com/Venu-Gopal04/llm-resume-analyzer
cd llm-resume-analyzer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
