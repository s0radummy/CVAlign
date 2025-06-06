# CVAlign: Smart CV Evaluation Tool

CVAlign is a web app that helps recruiters, hiring managers, and admins evaluate resumes against job descriptions using ML models and RAG-based feedback generation. It offers:

- CV relevance scoring using DistilBERT
- Automatic strengths and weaknesses generation using LLM + RAG (Ollama + FAISS)
- File storage on Cloudinary
- Role-based login system for recruiters, hiring managers, and admins

---

## Author
Sourajit Chowdhury (coolkrish17506@gmail.com)

## Tech Stack

**Backend**:
- FastAPI + SQLAlchemy
- FastAPI Users (JWT auth)
- Cloudinary for file storage
- HuggingFace Transformers (DistilBERT)
- Ollama + LangChain + FAISS (RAG)

**Frontend**:
- React + Tailwind CSS
- Role-based login UI
- Upload and score CVs

---

## Working

### 1. Clone the repository

git clone https://github.com/s0radummy/CVAlign.git
cd cvalign

### 2. Backend Setup

cd cvalign
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt


### 3. Set up .env
Create a .env file with the following:

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret


### 4. Initialize DB

python app/init_db.py

### 5. Start Ollama (if not already running)

ollama run mistral

### 6. Run Backend

uvicorn app.main:app --reload

### Train the Relevance Model (before first run)
Run the following command to train the DistilBERT relevance model and save it to "cv_classifier/models/classifier.pt":

python cv_classifier/train.py


### 7. Frontend Setup

cd cv-align-frontend
npm install
npm start

### Notes
Uploaded CVs are scored, stored on Cloudinary, and feedback is generated.
Uses LangChain RAG pipeline to generate strengths, weaknesses, and a fit summary.


### Folder Structure

cvalign/
│
├── app/
│   ├── auth/         # Authentication logic
│   ├── models/       # SQLAlchemy models
│   ├── routes/       # FastAPI routes
│   ├── utils/        # Parser, relevance scoring, etc.
│   ├── rag/          # RAG vector store + feedback logic
│   └── main.py       # Entry point
│
├── cv_classifier/    # DistilBERT training + inference
├── rag/vectorstore/  # FAISS index files
├── cv-align-frontend/
│   └── src/          # React app








---

