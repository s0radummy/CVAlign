
def safe_truncate(text: str, max_words: int = 300) -> str:
    words = text.split()
    return " ".join(words[:max_words])
