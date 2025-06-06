from cv_classifier.predict import predict_score  

def get_relevance_score(cv_text: str, job_desc: str) -> float:
    return predict_score(cv_text, job_desc)