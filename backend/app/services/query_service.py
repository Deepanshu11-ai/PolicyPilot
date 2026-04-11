from app.services.embedding_service import get_embedding
from app.core.supabase_client import supabase


def retrieve_chunks(question, user_id):

    embedding = get_embedding(question)

    response = supabase.rpc("match_documents", {
        "query_embedding": embedding,
        "match_threshold": 0.3,
        "match_count": 8,
        "user_id_input": user_id
    }).execute()

    return response.data