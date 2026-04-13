import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from .utils import get_context

BASE_DB_PATH = "vector_db"


# =========================
# 📥 PROCESS PDF (MISSING FUNCTION FIX)
# =========================
def process_pdf(file_path, policy_id):
    db_path = os.path.join(BASE_DB_PATH, f"policy_{policy_id}")
    os.makedirs(db_path, exist_ok=True)

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )

    db.persist()

    print(f"✅ DB created at {db_path}")

    return len(chunks)


# =========================
# ❓ ASK
# =========================
def ask_question(query, policy_id=1):
    context = get_context(query, policy_id)

    if not context:
        return "Not mentioned in policy"

    llm = ChatGroq(
        api_key="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",
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
You are an insurance assistant.

Rules:
- Answer using the context
- If partially available → answer what is known
- If not found → say "Not mentioned in policy"
- Be specific

Context:
{context}

Question:
{query}

Answer:
"""

    return llm.invoke(prompt).content