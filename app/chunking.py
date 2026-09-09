from app import config

def chunk_text(text: str) -> list[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + config.CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start = start + config.CHUNK_SIZE - config.CHUNK_OVERLAP

    return chunks

def chunk_documents(documents: list[str]) -> list[str]:
    all_chunks = []
    for doc in documents:
        all_chunks.extend(chunk_text(doc))
    return all_chunks
