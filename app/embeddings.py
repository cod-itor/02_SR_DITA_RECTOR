import ollama
from app import config

def get_embedding(text: str) -> list[float]:
    response = ollama.embeddings(
        model=config.EMBED_MODEL,
        prompt=text
    )
    return response['embedding']

def get_embeddings_for_chunks(chunks: list[str]) -> list[list[float]]:
    embeddings = []
    for chunk in chunks:
        embeddings.append(get_embedding(chunk))
    return embeddings
