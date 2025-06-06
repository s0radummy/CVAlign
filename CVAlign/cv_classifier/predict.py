import torch
from transformers import DistilBertTokenizer
from functools import lru_cache
from cv_classifier.train import RelevanceClassifier 

MODEL_NAME = "distilbert-base-uncased"
MODEL_PATH = "cv_classifier/models/classifier.pt"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@lru_cache()
def get_model_and_tokenizer():
    tokenizer = DistilBertTokenizer.from_pretrained(MODEL_NAME)
    model = RelevanceClassifier()
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval()
    return tokenizer, model

def predict_score(cv_text, job_desc):
    tokenizer, model = get_model_and_tokenizer()
    inputs = tokenizer(
        job_desc + " [SEP] " + cv_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512
    )
    with torch.no_grad():
        logits = model(**inputs)
        relevance_score = logits.item() * 100  
        return round(relevance_score, 2)
