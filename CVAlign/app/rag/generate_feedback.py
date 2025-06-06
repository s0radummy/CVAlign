from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Load
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local(
    "rag/vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 4})
llm = Ollama(model="mistral")

# prompt
prompt = PromptTemplate(
    input_variables=["context"],
    template="""
You are a career advisor. Based on the provided CV and job description, analyze the candidate's fit.

{context}

Return this format:
Strengths: <bullet points or short sentences>
Weaknesses: <bullet points or short sentences>
Explanation: <1-2 sentence explanation>
"""
)

# Build RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt}
)

def get_feedback(cv_text, job_desc):
    query = f"CV: {cv_text}\n\nJOB: {job_desc}"
    return qa.run(query)
