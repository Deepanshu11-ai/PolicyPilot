import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Base folder for all policy vector DBs
BASE_DB_PATH = "vector_db"


def get_context(query, policy_id=1, k=8):
    """
    Retrieve relevant context from vector DB for a given query and policy.
    This is the core RAG retrieval function used across all services.
    """

    # 📂 Construct DB path
    db_path = os.path.join(BASE_DB_PATH, f"policy_{policy_id}")

    # 🚨 Safety check: DB must exist
    if not os.path.exists(db_path):
        print(f"❌ DB not found for policy {policy_id}")
        return None

    try:
        # 🔹 Load embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        # 🔹 Load vector DB
        db = Chroma(
            persist_directory=db_path,
            embedding_function=embeddings
        )

        # 🔹 Retrieve relevant chunks
        docs = db.similarity_search_with_score(query, k=k)

        if not docs:
            print("⚠️ No documents retrieved")
            return None

        # 🔥 IMPORTANT: DO NOT OVER-FILTER
        # Keep top chunks directly for stability
        context_chunks = [doc.page_content for doc, _ in docs]

        # 🔹 Join into single context
        context = "\n\n".join(context_chunks)

        return context

    except Exception as e:
        print(f"❌ Error in get_context: {e}")
        return None
    print("🔍 Retrieved docs:", len(docs))
    
