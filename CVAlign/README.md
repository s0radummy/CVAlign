CVAlign: Smart CV Evaluation Tool
CVAlign is a web app for recruiters and hiring teams to evaluate resumes against job descriptions using machine learning and RAG-based feedback.

Key Features:

Scores CV relevance with DistilBERT

Generates strengths/weaknesses using LLM + RAG (Ollama + FAISS)

Stores files on Cloudinary

Role-based login for recruiters, hiring managers, and admins

Tech Stack
Backend: FastAPI, SQLAlchemy, FastAPI Users (JWT auth), Cloudinary, HuggingFace Transformers, Ollama, LangChain, FAISS
Frontend: React, Tailwind CSS

Quick Start
Clone the repo:

bash
git clone https://github.com/yourusername/CVAlign.git
cd CVAlign
Backend Setup:

Create and activate virtual environment

Install dependencies:

bash
pip install -r requirements.txt
Add Cloudinary credentials in .env

Initialize DB:

bash
python app/init_db.py
Start Ollama:

bash
ollama run mistral
Run backend:

bash
uvicorn app.main:app --reload
(Optional) Train relevance model:

bash
python cv_classifier/train.py
Frontend Setup:

bash
cd cv-align-frontend
npm install
npm start
Folder Structure
app/ – Backend (auth, models, routes, utils, RAG)

cv_classifier/ – DistilBERT model code

rag/vectorstore/ – FAISS index

cv-align-frontend/ – React frontend

Note: Uploaded CVs are scored, stored, and analyzed for feedback using a LangChain RAG pipeline.
