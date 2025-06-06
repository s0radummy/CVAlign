
from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.utils.cloudinary_upload import upload_to_cloudinary
from app.utils.parser import parse_cv
from app.utils.relevance import get_relevance_score
from app.models import CVUpload
from app.database import SessionLocal
from sqlalchemy.orm import Session
import uuid
from app.rag.generate_feedback import get_feedback

def extract_field(field_name, text):
    import re
    match = re.search(f"{field_name}:(.*?)(\n[A-Z]|$)", text, re.DOTALL)
    return match.group(1).strip() if match else None



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/")
async def upload_cv(
    cv_file: UploadFile = File(...),
    job_description: str = Form(...),
    db: Session = Depends(get_db)
):
    # Extract text 
    contents = await cv_file.read()
    cv_text = parse_cv(cv_file.filename, contents)

    # Score
    score = get_relevance_score(job_description, cv_text)

    # Cloudinary
    cloudinary_url = upload_to_cloudinary(contents, cv_file.filename)


    feedback = get_feedback(cv_text, job_description)


    strengths = extract_field("Strengths", feedback)
    weaknesses = extract_field("Weaknesses", feedback)
    explanation = extract_field("Explanation", feedback)


    # DB
    upload_entry = CVUpload(
        id=str(uuid.uuid4()),
        job_description=job_description,
        cv_url=cloudinary_url,
        score=score
    )
    db.add(upload_entry)
    db.commit()

    return {
    "score": score,
    "cloudinary_url": cloudinary_url,
    "strengths": strengths,
    "weaknesses": weaknesses,
    "explanation": explanation
}
