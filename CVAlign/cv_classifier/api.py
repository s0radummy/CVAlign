from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import torch
from transformers import DistilBertTokenizer
from cv_classifier.train import RelevanceClassifier
from cv_classifier.predict import predict_score


router = APIRouter()


model_path = "cv_classifier/models/classifier.pt"
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = RelevanceClassifier()
model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
model.eval()

class EvalRequest(BaseModel):
    job_description: str
    cv_text: str

class EvalResponse(BaseModel):
    score: int 

@router.post("/evaluate/", response_model=EvalResponse)
def evaluate_cv(request: EvalRequest):
        score = predict_score(request.cv_text, request.job_description)
        return {"score": score}