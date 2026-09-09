from app.embeddings import get_embedding
from app.vector_store import get_collection
from app import config

def retrieve_chunks(question: str) -> list[str]:
    question_vector = get_embedding(question)
    collection = get_collection()
    
    results = collection.query(
        query_embeddings=[question_vector],
        n_results=config.TOP_K
    )
    
    return results['documents'][0]
