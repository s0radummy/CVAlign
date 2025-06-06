import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load
with open("cv_classifier/data/dataset.json") as f:
    data = json.load(f)

# Concatenate
documents = [f"CV: {item['cv_text']}\n\nJOB: {item['job_description']}" for item in data]

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
docs = splitter.create_documents(documents)

# Generate
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding_model)

# Save
db.save_local("rag/vectorstore")
print("FAISS vector store saved.")
