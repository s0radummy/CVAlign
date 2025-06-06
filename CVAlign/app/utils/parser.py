import pdfplumber
import docx
from io import BytesIO

def parse_cv(filename, content):
    if filename.endswith(".pdf"):
        with pdfplumber.open(BytesIO(content)) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages])
    elif filename.endswith(".docx"):
        doc = docx.Document(BytesIO(content))
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return "Unsupported format"
