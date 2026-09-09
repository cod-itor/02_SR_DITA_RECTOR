import chromadb
from app import config
from app.ingestion import load_documents
from app.chunking import chunk_documents
from app.embeddings import get_embeddings_for_chunks

def get_collection():
    client = chromadb.PersistentClient(path=config.CHROMA_DB_DIR)
    return client.get_or_create_collection(name=config.COLLECTION_NAME)

def build_database():
    collection = get_collection()
    
    print("Loading documents...")
    documents = load_documents(config.DATA_DIR)
    
    print("Chunking documents...")
    chunks = chunk_documents(documents)
    
    print("Generating embeddings...")
    embeddings = get_embeddings_for_chunks(chunks)
    
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )
    print("Database built successfully.")

if __name__ == "__main__":
    build_database()
