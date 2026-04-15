# 🚀 AI Resume Screening System with LangChain & LangSmith

---

## 📌 Overview

This project implements an **AI-powered Resume Screening System** that evaluates candidates based on a given job description.

It uses **LangChain** to build a modular pipeline and **LangSmith** for tracing, debugging, and monitoring each step of the LLM workflow.

The system provides:
- ✅ Skill extraction  
- ✅ Resume-job matching  
- ✅ Score calculation (0–100)  
- ✅ Explainable output  

---

## 🎯 Objectives

- Understand LangChain pipeline architecture  
- Build modular LLM workflows  
- Implement resume skill extraction and matching  
- Design scoring logic with explainability  
- Enable tracing using LangSmith  

---

## 🧠 Problem Statement

**Input:**  
- Resume  
- Job Description  

**Process:**  
- Skill Extraction → Matching → Scoring → Explanation  

**Output:**  
- Fit Score (0–100)  
- Explanation of the score  

---

## 🏗️ Architecture

Resume → Extraction → Matching → Scoring (Python Logic) → Explanation → LangSmith Tracing

---

## 🧩 Core Components

### 🔹 Prompt Templates
Reusable prompts for:
- Extraction  
- Matching  
- Explanation  

### 🔹 Chains (LangChain)
- `extract_chain` → Extracts skills & experience  
- `match_chain` → Compares resume with job  
- `explain_chain` → Generates explanation  

### 🔹 Scoring Logic (Hybrid Approach)

Instead of relying only on LLM:
- Python-based scoring ensures accuracy  
- Prevents hallucination  
- Provides deterministic results  

### 🔹 LangSmith Tracing

- Tracks full pipeline execution  
- Shows:
  - Inputs  
  - Outputs  
  - Intermediate steps  
- Helps debugging and monitoring  

---

## ⚙️ Tech Stack

- Python 🐍  
- LangChain  
- LangSmith  
- HuggingFace Transformers (GPT-2)  
- VS Code / Jupyter Notebook  

---

## 💻 Project Structure

resume-screening-ai/
│
├── prompts/
├── chains/
├── resumes/
├── main.py
└── requirements.txt

---

## ▶️ How to Run

### 1️⃣ Clone Repository
git clone https://github.com/your-username/resume-screening-ai.git  
cd resume-screening-ai  

### 2️⃣ Create Virtual Environment
python -m venv .venv  
.\.venv\Scripts\activate  

### 3️⃣ Install Dependencies
pip install -r requirements.txt  

### 4️⃣ Set Environment Variables (PowerShell)
$env:LANGCHAIN_TRACING_V2="true"  
$env:LANGCHAIN_API_KEY="your_api_key"  
$env:LANGCHAIN_PROJECT="resume-project"  

### 5️⃣ Run Project
python main.py  

---

## 📊 Sample Output

--- Evaluating strong.txt ---
Score: 83  
Explanation: Candidate matches most required skills like Python, ML, NLP.  

--- Evaluating average.txt ---
Score: 50  
Explanation: Partial match, missing key skills.  

--- Evaluating weak.txt ---
Score: 16  
Explanation: Candidate lacks required skills.  

---

## 📸 LangSmith Tracing

This project includes full tracing using LangSmith:

- Project Overview  
- Pipeline Runs  
- Detailed Execution Flow  

---

## 📂 Screenshots

- LangSmith_Project_Overview.png  
- LangSmith_Tracing_Runs.png  
- LangSmith_Run_Details.png  

---

## ✅ Advantages

- Modular and scalable design  
- Explainable AI outputs  
- Debuggable pipeline with tracing  
- Hybrid scoring improves accuracy  

---

## ❌ Limitations

- Lightweight models (GPT-2) have limited reasoning  
- Requires prompt tuning  
- Depends on input quality  

---

## ⚠️ When Not to Use

- Simple rule-based filtering systems  
- Real-time ultra-low latency systems  
- Small-scale applications  

---

## 🚀 Future Improvements

- Use advanced LLMs (GPT-4 / Claude)  
- Add structured JSON output  
- Improve scoring using embeddings  
- Multi-agent evaluation system  

---

## 📖 Key Learnings

- LLMs need structured pipelines  
- Hybrid AI + logic gives better results  
- Tracing is essential for debugging LLM apps  
- LangChain simplifies AI system design  

---

## 🔗 Connect with Me

- 💼 LinkedIn: https://www.linkedin.com/in/samyagh/  
- 💻 GitHub: https://github.com/samyaghshetty  

---

## 🙌 Acknowledgment

This project was completed as part of a **GenAI Internship Assignment**, focusing on building real-world AI systems using LangChain and LangSmith.

---

## ⭐ Final Note

This project demonstrates the transition from prompt-based usage to building **production-level AI pipelines with explainability and monitoring** 🚀
